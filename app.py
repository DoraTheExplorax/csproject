from db import DB
from flask import Flask, render_template, request
app = Flask(__name__)
db=DB()

@app.route('/', methods=['GET','POST'])
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
      address = address1+' '+address2+' '+address3
      db.add_users(Lname=lname,Fname=fname,Add=address,Pass=password,ContactNumber=number,EmailId=email)
   return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   return render_template('signup.html')
if __name__ == '__main__':
   app.run(debug=True)
