# Hello World Python App
This is a Hello World Python app mini project that we are are going to dockerise and deploy 
using Kubernetes Minikube.

# Steps
1. create app.py file
2. create Dockerfile
3. build a docker image
4. create pod-hello-app definition file
5. create replicaset-hello-app definition file
6. create service-hello-app definition file

# app.py
copy the following contents into app.py file

from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
   return 'Hello World from Python!'

if __name__ == "__main__":
   app.run()

# Dockerfile
Here we create a new directory named hello-app using the mkdir
command. This directory will be the context for our Docker image. Context
is the directory that contains all the files needed to successfully build an image:

# From
The FROM command is used to state what OS you intend to use as the base image. In this line we are inheriting our image from alpine 3.7 python image, As we will deploy a python app, so we have used alpine python image.

# RUN


# COPY
To copy files from your Docker host to a Docker image, you can use the COPY command. We are copying all the files from our directory to docker images at /app


# CMD
Docker can run only one CMD command. Therefore, if you insert two or more CMD instructions, Docker would only run the last one i.e. the most recent one.

# Build Docker image
Build a docker image and push to docker hub

# Create a Pod
Here we create a pod service file that will create a pod object. The pod will be a wraper for our container running on the node. After creating the pod definition file run the following command to create the pod.
kubectl create pod -f pod-hello-app.yaml

# Create ReplicaSet
We create a replicaset-hello-app.yaml file which we use to create a ReplicaSet object.
The ReplicaSet object defines the desired number of pods to create and keep them running at every time. In this case we defined 3 replicas by using the following command.
kubectl create replicaset -f replicaset-hello-app.yaml

# Create Service of NodePort type
To loadbalance traffic coming to our pods we define a Service type of NodePort. This will distribute traffic to all the pods running in our cluster. Minikube cannot run Loadbalancer service as this can only run on cloud service platforms such as AWS, AZURE, Google etc.



