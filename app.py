from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.secret_key='joo'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='study_assistant'
db=MySQL(app)
bcrypt=Bcrypt(app)
@app.route('/')
def home():
    return "flask is running"    

@app.route('/signup',methods=['POST','GET'])
def signup():
        if request.method=='POST':
            username=request.form.get('name').strip()
            password=request.form.get('password')
            if not username or not password:
                flash("enter paassword and username")
                return redirect(url_for('signup'))   
            cursor=db.connection.cursor()
            cursor.execute("select id from user where name=%s", (username, ))
            existing_user=cursor.fetchone()
        
            if existing_user:
                flash("username already exist")
                return redirect(url_for('signup'))
            password_hash=bcrypt.generate_password_hash(password)     
            cursor=db.connection.cursor()
            cursor.execute("insert into user (name, password) values(%s,%s)",
            (username, password_hash))
            db.connection.commit()
            return render_template("login.html")
        return render_template("signup.html")    
    

              
app.run(debug=True)    
