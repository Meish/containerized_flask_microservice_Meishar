from flask import Flask # , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make addition at route /add'

@app.route("/add/<number1>/<number2>")
def addition(number1, number2):
    """Return a the addition of the two numbers."""
    print("I am inside addition")
    return number1+number2

@app.route("/multi/<number1>/<number2>")
def multiply(number1, number2):
    """Returns the multiplication of the two numbers."""
    print("I am inside multiplication")
    return number1*number2
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
