from flask import Flask, render_template
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

@app.route('/signup')
def signup():
    return render_template("signup.html")    
app.run(debug=True)    
