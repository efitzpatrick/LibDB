import configparser
from flask import Flask, render_template, redirect, url_for, request, flash
import mysql.connector
from User import User

# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')
my_user = None #will hold user id whene logged in
# Set up application server.
app = Flask(__name__)
app.secret_key = 'my_key_is_set_here'

# Create a function for fetching data from the database.
def sql_query(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def sql_execute(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

# For this example you can select a handler function by
# uncommenting one of the @app.route decorators.

@app.route('/')
def basic_response():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    global my_user
    if request.method == 'POST':
        email = request.form['email'].strip()
        sql = "select password from library.user where email='{email}';".format(email = email)
        correct_password = sql_query(sql)
        if not correct_password or request.form['password'] != correct_password[0][0]:
            flash("incorrect password")
            #return str(correct_password[0][0])
        else:
            user_id_sql = "select id, privilege from library.user where email='{email}';".format(email=email)
            user_id_result = sql_query(user_id_sql)[0]
            user_id = user_id_result[0]
            privilege = user_id_result[1]
            my_user = User(user_id, email, privilege)
            return redirect(url_for('home'))

    return render_template('login.html', error=error, privilege = my_user.get_privilege())

@app.route('/home', methods=['GET', 'POST'])
def home():
    global my_user
    if my_user is None:
        return redirect(url_for('login'))
    else:
        error=None
        if request.method == 'POST':
            search = request.form['search_input']
            search_sql = "select id from book where title = '{search}' or author = '{search}';".format(search = search)
            search_info = sql_query(search_sql)
            return str(search_info)
    return render_template('homeretry.html', error=error, privilege = my_user.get_privilege())

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global my_user
    if my_user is None:
        return redirect(url_for('login'))
        #redirect(url_for('login'))
    else:
        user_id = my_user.get_id()
        profile_info_sql = "select name, email, address from library.user where id = '{user_id}';".format(user_id = user_id)
        profile_info_list= sql_query(profile_info_sql)[0]
        books_sql = "select title, return_date from book b inner join status s on b.sku = s.book_sku where availability = 'unavailable' and b.owner  = '{user_id}';".format(user_id= user_id)
        books_info = sql_query(books_sql)
        result = str(profile_info_list), " ", str(books_info)
        #return str(result)
        # ("(u'Ellie Fitzpatrick', u'eef33@case.edu', u'1234 Juniper rd, Cleveland, OH')", ' ', '[]')
        profile_info = {"name": profile_info_list[0], 'email': profile_info_list[1], 'address': profile_info_list[2]}
        return render_template('profile.html', profile_info = profile_info, books = books_info, privilege = my_user.get_privilege())

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global my_user
    if my_user is None:
        return redirect(url_for('login'))
    elif !my_user.get_privilege:
        return redirect(url_for('home'))
    else:
        return render_template('admin.html', privilege = my_user.get_privilege())

@app.route('/checkout', methods=['GET', 'POST', 'remove'])
def checkout():
    global my_user
    if my_user is None:
        return redirect(url_for('login'))
    else:
        sql = "select title, return_date, sku from book b inner join status s on b.sku = s.sku inner join cart c on b.cart_id = c.id where c.user_id = '{user_id}';".format(user_id = user_id)  #sql query for finding user's books in their cart
        books_in_cart = sql_query(sql)

        #new plan: return a tuple of 3 items
        #tuple should be (book.title, book.duedate, book.sku)
        #return this as a list, so we can iterate through it.
        return render_template('checkout.html', books=books_in_cart, privilege = my_user.get_privilege())
    pass

@app.route('/remove',methods='POST')
def remove_from_cart():
    global my_user
    book_to_checkout =request.format['checkout_button']
    sql = "update book set cart_id = null where sku = '{sku}';".format(sku = book_to_checkout)
    sql2 = "update status set availability = 'available' where and book_sku = '{sku}';".format(sku = book_to_checkout)
    sql_execute(sql)
    sql2(sql_execute)

    pass

@app.route('/checkout',methods=['GET', 'POST'])
def on_checkout():
    global my_user
    user_id = my_user.get_id()
    sql = "select sku from book b inner join status s on b.sku = s.sku inner join cart c on b.cart_id = c.id where c.user_id = '{user_id}';".format(user_id = user_id)  #sql query for finding user's books in their cart
    books_in_cart = sql_query(sql)
    for sku in books_in_cart:
        sql = "update book set owner = '{user_id}', cart_id = null where sku = '{sku}';".format(user_id = user_id, sku=sku)  #sql query for finding user's books in their cart
    return redirect(url_for('home'))
    pass

@app.route('/results', methods=['GET', 'POST'])
def results():
    return

@app.route('/createuser', methods=['GET', 'POST'])
def createuser():
    #Take data from the field
    email = request.form['email'].strip()
    password = request.form['email'].strip()
    #check if data from username field is already in databse
    id = email.split["@"]
    id = id[0][3:]
    #if yes: flash "already in use" and redirect to login page
    #if no: flash "user created" add in database
    pass

@app.route('/admin/create_book', methods=['GET', 'POST'])
def create_book():
    global my_user
    if request.method == 'POST':
        # Get all details from form
        id = request.form['id'].strip()
        sku = request.form['sku'].strip()
        title = request.form['title'].strip()
        author = request.form['author'].strip()

        # Update database
        sql = "insert into book(id, sku, title, author) values ('{id}', '{sku}', '{title}', '{author}');".format(id=id, sku=sku, title=title, author=author)
        sql_execute(sql)
        return redirect(url_for('admin'))

    return render_template('createbook.html', privilege = my_user.get_privilege)

@app.route('/admin/delete_book', methods['POST'])
def delete_book():
    global my_user
    if request.method == 'POST':
        #get sku from form
        sku = request.form['booksku'].strip()

        #update database
        #sql = sql to delete book from database
        #sql_execute(sql)
        return str(sku)
        #return redirect(url_for('admin'))

@app.route('/admin/get_statistics', methods['POST'])
def get_statistics():
    global my_user

    

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global my_user
    my_user = None
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(**config['app'])
{}
