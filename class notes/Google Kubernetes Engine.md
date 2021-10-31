# Google Kubernetes Engine

- Login to Google Cloud.

- Search in GCP, and enable "Container Registry". 

  Billing is required. Check which project is this service is enabled on.

  

- Open the Cloud Shell.

  The Cloud Shell has its own persistent volume.

- Set the project we will work on.

  ```
  gloud config set project <project id>
  ```

  

- Run the docker image to create the container.

  ```
  # nginx is running on 80
  
  docker run -p 8080:80 -d nginx:latest
  ```

  

- Clock the 'preview' button and select the port to open localhost:8080.

- Copy the customized file into the docker container.

  ```
  cd <host directory of the target file>
  docker cp index.html <container id>:/usr/share/nginx/html/
  ```

  

- Build a new image with the latest changes.

  ```
  docker commit <container id> <image name>:<tag>
  
  docker images
  ```



- Push the image to Google's registry (GCR).

  ```
  # Before push the image, tag it first
  # us.gcr.io is the host name
  docker tag <image name>:<tag> us.gcr.io/<project id>/<repo name>:<tag>
  
  docker push us.gcr.io/<project id>/<repo name>:<tag>
  ```



- Navigate to Container Registry.

- Click into the container.

- In the drop down list of "Deploy", we can find "Deploy to GKE/Cloud run".

  We can deploy to GKE from UI as above, but we can also do it via CLI.



- Enable Kubernetes Cluster and related service

  If do not know which services to enable, can try to create the cluster and find out from the error log.

  ```
  gcloud services enable <service name>
  
  container.googleapis.com
  ```

  

- Configure the project id of the following configuration.

  ```
  gcloud config set project <project id>
  
  # Configure the zone of the VM
  gcloud config set compute/zone us-central1-a
  ```



- Create a GKE cluster

  ```
  # gk-cluster is the cluster name with just 1 node
  gcloud container clusters create gk-cluster --num-nodes=1
  ```

- Search and navigate to "Kubernetes Engine", we can find the cluster is being created or running.



- Deploy the containers to the Kubernetes Cluster just created.

  ```
  # Configures kubectl to use and interact with the cluster. Kubectl will talk to the Api Server in the Master of cluster. The Api Server will do all the delivery and management work.
  
  # Generate and authenticate to use the kubectl.
  
  gcloud container clusters get-credentials gk-cluster 
  ```



- Deploy an application to the cluster.

  ```
  kubectl create deployment <name of App> --image=us.gcr.io/<project id>/<repo name>:<tag>
  ```

  

- Expose the application to the internet.

  Can expose the app by creating a Service, a Kubernetes resource that exposes your application to external traffic.

  ```
  # Create in the LoadBalancer mode 
  # port specifies the public internet accesing port, and this port is mapped to nginx pre-configured service port.
  
  kubectl expose deployment <name of App> --type LoadBalancer --port 80 --target-port 80
  
  kubectl get pods
  kubectl get service <app name>
  ```

  

- Fetch the EXTERNAL-IP from the returned result of `kubectl get service <app name>`, and access the web page with the IP.

- When connection is refused, try to check the Service and Pod status.

```
kubectl describe services <service name>

# If the status is notmal, and the external ip is configured, then check the Pod status.
# Try forward Pod.
kubectl get pods
kubectl port-forward <pod name> 8080:80
```



- If the Pod is always in pending state, check what is going on.

  ```
  kubectl get events
  ```

  



### Case Study

- EXTERNAL-IP is not accessible: connection refuse when do `crul http://<external ip>:<host port>`.

- Service problem? Check service configuration `kubectl describe services <name>`. -> Normal

- Pod problem? Try to forward port `kubectl port-forward <pod name> <host port>:<service port>`. 

  -> Cannot forward port. Port is not running, still in the pending state.

- Deployment problem? Check events `kubectl get events`.

  - **Event log:** failed to resolve reference.

  - **Reason:** when do deployment, forgot to add the tag.

    The tag is "version1", while when this field is not configured, it automatically map to "latest". However, this customized image does not have "latest" version.

    Therefore, although the Deployment is created, upcoming configurations failed. Pod underneath is always in pending mode.

  - **Solution:** delete the Deployment and reconfigure it.

    ```
    kubectl get deploy
    kubectl delete deploy <deply name>
    ```

    Expose again with a new service created.

    Access using the new external IP.

