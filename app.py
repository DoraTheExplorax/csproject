from flask import Flask,render_template,request,redirect
from flask_login import login_required, current_user, login_user, logout_user
from models import UserModel, BookModel, db, load_books,login
import json 

app = Flask(__name__)
app.secret_key = 'xyz'
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db.init_app(app)
login.init_app(app)
login.login_view = 'login'
def to_dict(self):
    result = {}
    for key in self.__mapper__.c.keys():
        if getattr(self, key) is not None:
            result[key] = str(getattr(self, key))
        else:
            result[key] = getattr(self, key)
    return result
@app.before_first_request
def create_all():
    db.create_all()

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/available')
def availablebooks():
    data = load_books()
    data_dict={}
    for i in range(len(data)):
        data_dict[i]=[data[i].book1, data[i].name, data[i].cnumber]
    print(data_dict)
    return render_template("availablebooks.html",data=data_dict)
    
     
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/profile')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/profile')
     
    return render_template('login.html')
 
@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/profile')
     
    if request.method == 'POST':
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        contactnumber = request.form['contactnumber']
        add1 = request.form['add1']
        add2 = request.form['add2']
        add3 = request.form['add3']
        password = request.form['password']
 
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
             
        user = UserModel(email=email, firstname=firstname, lastname=lastname, contactnumber=contactnumber, add1=add1, add2=add2, add3=add3)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html')
 
 
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/submit', methods=['POST', 'GET'])
def submitbooks():
    if request.method == 'POST':
        book1 = request.form['book1']
        name = request.form['name']
        cnumber = request.form['cnumber']
        book = BookModel(book1=book1, name=name, cnumber=cnumber)
        db.session.add(book)
        db.session.commit()
        return redirect('/available')
    return render_template("submitbooks.html")

if __name__ == '__main__':
 app.run(debug=True)