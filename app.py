from email.policy import default
from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

from datetime import datetime
# rm -rf .git
# git add .gitignore
# git commit -m "message" .gitignore
# .gitignore. => you end up with .gitignore



app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    phone_number = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=True)
    # datatime = db.Column(db.DateTime, default=datatime.now)
    def __repr__(self):
        return f'Contact info : {self.id}, {self.username}, {self.phone_number}, {self.email}'  
        #{self.datetime}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username 

# try:
#     <use session>
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()  # optional, depends on use case
# c3  = Contact(username = 'iman', phone_number = '09121234562', email='ali_matin16@yahoo.com')
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

@app.route('/') 
def home():
    contacts = Contact.query.all()

    return render_template('home.html', contact_list = contacts)
    # print(contacts)
    # return contacts
    # return 'My name is AliReza ___ ali' 
 
@app.route('/<contact_id>') 
def detail(contact_id): 
    c_info = Contact.query.get(contact_id) 
    print(c_info)
    return render_template('detail.html', info=c_info)      

@app.route('/test') 
def test():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">  <!--https://www.w3schools.com/tags/att_meta_charset.asp-->
        <title> 
            {% block title %} {% endblock %}
        </title> 
        </head>
        <body>
            <a href='#'>alal </a>
            My name is AliReza ___ ali
            My name is AliReza ___ ali
        <!-- <h1>My Name is AliReza</h1> -->


        </body>
        </html>
    ''' 

@app.route('/home')
def homepage():
    return render_template('home.html', name = 'Alireza') 

@app.route('/insert')
def insert_record():
    return render_template('insert_form.html')

# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         return '--'#render_template('data_form.html', form_data = form_data) 

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST': 
        form_data = request.form
        return render_template('data_form.html', form_data = form_data)


@app.route('/about')
def about():
    return render_template('about.html') 


if __name__ == '__main__':
    app.run(debug=True)




