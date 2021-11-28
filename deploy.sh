# Hadoop master
kubectl apply -f yaml/hadoop_master/master-deployment.yaml
kubectl apply -f yaml/hadoop_master/master-service.yaml
kubectl apply -f yaml/hadoop/master/master-lb.yaml

sleep 10

# Hadoop worker
kubectl apply -f yaml/hadoop_worker/worker0-deployment.yaml
kubectl apply -f yaml/hadoop_worker/worker0-service.yaml
kubectl apply -f yaml/hadoop_worker/worker1-deployment.yaml
kubectl apply -f yaml/hadoop_worker/worker1-service.yaml

# Jupyter Notebook
kubectl apply -f yaml/jupyter/jupyter-deployment.yaml
kubectl apply -f yaml/jupyter/jupyter-service.yaml
kubectl apply -f yaml/jupyter/jupyter-lb.yaml

# Sonarscanner
kubectl apply -f yaml/sonar/sonarscanner-deployment.yaml
kubectl apply -f yaml/sonar/sonarscanner-service.yaml
kubectl apply -f yaml/sonar/sonarscanner-lb.yaml

# Spark Master
kubectl apply -f yaml/spark/master-deployment.yaml
kubectl apply -f yaml/spark/master-service.yaml
kubectl apply -f yaml/spark/master-lb.yaml

sleep 10

# Spark workers
kubectl apply -f yaml/spark/worker0-deployment.yaml
kubectl apply -f yaml/spark/worker1-deployment.yaml

#Driver
kubectl apply -f yaml/toolbox-deployment.yaml
kubectl apply -f yaml/driver/driver-lb.yaml

