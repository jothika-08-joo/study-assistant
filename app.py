from flask import Flask, render_template, request, redirect, flash, url_for, session
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
 
def is_logged_in():
    return user_id in session    

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
            return redirect(url_for('login'))
        return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username=request.form.get('name').strip()
        password=request.form.get('password')

        if not username or not password:
            flash("kindly enter your name and password")
            return redirect(url_for('login'))
        cursor=db.connection.cursor()
        cursor.execute("select id,password from user where name=%s", (username,))    
        already_signedin=cursor.fetchone()
        if already_signedin:
            s=already_signedin[1]
            if bcrypt.check_password_hash(s,password):
                session['user_id']=already_signedin[0]
                return redirect(url_for('dashboard'))
                
            else:
                flash("enter your username or password correctly")  
                return redirect(url_for('login'))
        flash("first signin")
        return redirect(url_for("signup"))
    return render_template("login.html")

            

    

              
app.run(debug=True)    
