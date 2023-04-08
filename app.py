# Import flask module
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return '<h1>Hello World from Python!<h1>'
 
# main driver function
if __name__ == "__main__":
    app.run()