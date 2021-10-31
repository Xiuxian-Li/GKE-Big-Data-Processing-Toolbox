# Kubernetes

Container orchestration framework/tool.

Helps manage applications containing hundreds or even thousands of containers in different development environment.



### Basic Architecture

Master node (at least one): run processes used to manage clusters.

​	API Server: the entry to use the Kubernetes cluster.

​	Controller manager: keeps track of what is happening in the cluster.

​	Scheduler: schedules containers on different nodes.

Worker node: each have a <u>kubelet</u> process running on it.

Kubelet allows communication among clusters.

Multiple docker containers can run on a work node. 



### Kubernetes Components

- Pod: an abstraction over container. Only need to interact with the Kubernetes layer.

  Kubernetes runs virtual networks. Each Pod gets its own IP address.

  New IP address is used on re-creation. For convenience purpose, another component service is needed.

- Service: a permanent IP address (a DNS name) attached to each Pod.

  - External service / internal service.

- Ingress: commands go first to Ingress, and then assigned to services.

- ConfigMap: external configuration of the application.

- Secret: store sensitive data in base64 encoded format, e.g. credentials.

  

<img src="/Users/phoebemac/Library/Application Support/typora-user-images/image-20211030120405933.png" alt="image-20211030120405933" style="zoom:50%;" />



### Volumes

If data is just stored on a Pod or container of the DB, when it is restarted, data is gone. This brings the requirement to have data persists in the long term.

K8s doese not manage data persistence.

Volumes attach a physical storage on a hard-drive to your pod (local or remote). 

Remote means the storage is not within the Kubernetes cluster, we only have external references to it.

- Define blueprints for pods -> deployment.
- Configure the number of replica that the pod wants to run.

When one pod is dead, Service could forward the request to a replicated one.

- Deployment
- Statefulset



### Minikube

Have the Master processes and the Worker processes running in one node. The node is encapsulated in a Virtual Box.

- Create Virtual Box on your laptop
- Node runs in that Virtual Box
- 1 Node K8s cluster
- For testing purpose



### Kubectl

Command line tool for K8s cluster to interact with the cluster, e.g. create Pods and other components on the node.

Master processes

- Api Server: the entry point to the K8s cluster. Via UI, API, CLI (kubectl).

  The kubectl submits commands to the Master, and Worker processes work on the comannd when the Master delivered the command to them.



### Installation

```
brew update
brew install minikube
brew install kubectl

# Use the hypervisor to start the minikube K8s cluster
minikube start --vm-driver=hyperkit

# Get status of nodes
kubectl get nodes

minikube status
```



- Kubectl CLI: for configuring the Minikube cluster.
- Minikube CLI: for start up/deleting the cluster.



### Create Deployment

```
kubectl get nodes
kubectl get pod
kubectl get services

# Can create many K8s components 
kubectl create -h 
```

 

However, cannot create Pods using `kubectl create`, because Pods are the smalles units. Pods are not used for creation. 

Deployment is another abstraction over Pods. Therefore, we usually create Deployments. Pods will be created automatically underneathe.

```
# Usage
kubectl create deployment NAME --image=image [--dry-run] [options]

# Will download the latest version of nginx image from docker hub
kubectl create deployment nginx-depl --image=nginx

kubectl get deployment
kubectl get pod
kubectl describe pod [pod name]

kubectl exec -it [pod name] -- bin/bash

kubectl apply -f <name of the configuration file>.yaml
```



![image-20211030140443201](/Users/phoebemac/Library/Application Support/typora-user-images/image-20211030140443201.png)

 ![image-20211030140509805](/Users/phoebemac/Library/Application Support/typora-user-images/image-20211030140509805.png) 



### Deploying MongoDB and MongoExpress

- Create a MongoDB Pod

- Create a Service to talk to the Pod

  -  Internal Service: only components within the same cluster can talk to it.

- Create a Mongo Express deployment

- Create a ConfigMao including the DB Url

- Create a Secret including the authentication information

  DB User

  DB Pwd

- Make Mongo Express accessible through the browser. Therefore, we require an external Service, allowing external requests.

