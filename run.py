import configparser
from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')
user_id = None #will hold user id whene logged in
# Set up application server.
app = Flask(__name__)

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
    error=None
    if request.method == 'POST':
        search = request.form['search_input']
        search_sql = "select id from book where title = '{search}' or author = '{search}';".format(search = search)
        search_info = sql_query(search_sql)
        return str(search_info)
    return render_template('homeretry.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email'].strip()
        sql = "select password from library.user where email='{email}';".format(email = email)
        correct_password = sql_query(sql)
        if request.form['password'] != correct_password[0][0]:
            return str(correct_password[0][0])
        else:
            user_id_sql = "select id from library.user where email='{email}';".format(email=email)
            user_id = sql_query(user_id_sql)[0][0]
            return redirect(url_for('home'))

    return render_template('login.html', error=error)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    pass

def on_checkout():
    pass

@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    pass

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if user_id is None:
        return redirect(url_for('login'))
    else:
        profile_info_sql = "select name, email, address from library.user where user_id = '{user_id}'';".format(user_id = user_id)
        profile_info_list= sql_query(profile_info_sql)[0]
        books_sql = "select title, status from books where status = 'checked_out' and owner  = '{user_id}';".format(user_id= user_id)
        books_info = sql_query(books_sql)
        return str(profile_info_list, " ", books_info)
        #profile_info = {"name": profile_info_list[0], 'email': profile_info_list[1], 'address': profile_info_list[2]}
        #return render_template('profile.html', profile_info = profile_info)

@app.route('/results', methods=['GET', 'POST'])
def results():
    pass

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
