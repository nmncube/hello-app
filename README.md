# Hello World Python App
This is a Hello World Python app mini project that we are are going to dockerise and deploy 
using Kubernetes Minikube.

# Steps
1. create app.py file
2. create Dockerfile
3. create a docker image
4. create hello-app pod definition file
5. create hello-app service definition file

# app.py
copy the following contents into app.py file

from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return '<h1>Hello World from Python!<h1>'
 
if __name__ == "__main__":
    app.run()
