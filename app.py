from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='study_assistant'
db=MySQL(app)
@app.route('/')
def home():
    return "flask is running"    

@app.route('/signup',methods=['POST','GET'])
def signup():
        if request.method=='POST':
            username=request.form.get('name').strip()
            password=request.form.get('password')
        if not username or password:
            flash("enter paassword and username")
            return redirect({url_for('signup')})   
        cursor=db.connection.cursor()
        existing_user=cursor.execute("select id from user where(name,)")
        db.connection.close()
        if existing_user:
            flash("username already exist")
            return redirect({url_for('signup')})
        paassword_hash=generate_password_hashing(paassword)     
        cursor=db.connection.cursor()
        cursor.execute("insert into user (username, password_hash, ) " ,values(%s,%s, )
        (username, password_hash))
        db.connection.commit()
        db.connection.close()
        return render_template("login.html")
    

              
app.run(debug=True)    
