from db import db, users
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        number = request.form['number']
        password = request.form['password']
        address1 = request.form['address1']
        address2 = request.form['address2']
        address3 = request.form['address3']
        name = fname +' '+ lname
        address = address1 + ' ' + address2 + ' ' + address3
        User=users(name, email, password, number , address)
        db.session.add(User)
        db.session.commit()

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
   return render_template('signup.html')
if __name__ == '__main__':
   app.run(debug=True)
