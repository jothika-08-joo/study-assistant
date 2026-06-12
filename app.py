from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "flask is running"    
app.run(debug=True)    