# Put your app in here.
from flask import Flask
from flask import request
import operations

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <html>
        <body>
            <h1>Welcome to 19.1 Flask Calc Exercise!</h1> 
        </body>
    </html>
    """
    return html

@app.route('/add')
def add():
    a = request.args["a"]
    b = request.args["b"]
    num1 = int(a)
    num2 = int(b)
    
    return f"{operations.add(num1,num2)}"

@app.route('/sub')
def sub():
    a = request.args["a"]
    b = request.args["b"]
    num1 = int(a)
    num2 = int(b)
    
    return f"{operations.sub(num1,num2)}"

@app.route('/mult')
def mult():
    a = request.args["a"]
    b = request.args["b"]
    num1 = int(a)
    num2 = int(b)
    
    return f"{operations.mult(num1,num2)}"

@app.route('/div')
def div():
    a = request.args["a"]
    b = request.args["b"]
    num1 = int(a)
    num2 = int(b)
    
    return f"{int(operations.div(num1,num2))}"
