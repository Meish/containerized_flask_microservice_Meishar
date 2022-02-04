from flask import Flask # , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
