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

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if user_id is None:
        return redirect(url_for('login'))
    else:
        sql = ""#sql query for finding user's books in their cart
        books_in_cart = ""#sql_query(sql)

        #should turn the list from sql_query into a dict, depending on if books_in_cart is a list of tuples (hopefully)
        #tuple should be (book.title, book.duedate)
        books_in_cart = dict(books_in_cart)
        return render_template('checkout.html', books=books_in_cart)
    pass

def on_checkout():
    #book's cart id gets set to null
    #book's user id is populated by user_id
    #insert back into database
    #redirect to profile
    pass

@app.route('/createuser', methods=['GET', 'POST'])
def createuser():
    #Take data from the field
    #check if data from username field is already in databse
    #if yes: flash "already in use" and redirect to login page
    #if no: flash "user created" add in
    pass


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
        return render_template('profile.html', profile_info = profile_info, books = books_info)

@app.route('/results', methods=['GET', 'POST'])
def results():
    return

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global my_user
    my_user = None
    return redirect(url_for('home'))
#@app.route('/', methods=['GET', 'POST'])
def template_response_with_data():
    print(request.form)
    if "buy-book" in request.form:
        book_id = int(request.form["buy-book"])
        sql = "delete from book where id={book_id};".format(book_id=book_id)
        sql_execute(sql)
    template_data = {}
    sql = "select id, title from book order by title"
    books = sql_query(sql)
    template_data['books'] = books
    return render_template('login.html', template_data=template_data)

if __name__ == '__main__':
    app.run(**config['app'])
{}
