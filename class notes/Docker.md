# Docker

A tool for running applications in an isolated environment.



### Containers

**Share the OS, but run in isolation.**

Does not require that much memory and an entire operating system like a virtual machine.

An abstraction at <u>the app layer</u> that packages code and dependencies together.

Multiple containers can run on the same machine and <u>share OS kernel</u> with other  containers, each running as isolated processes in user space.  



### Virtual Machines

<u>An abstraction of physical hardware</u> turning one server into many servers.

The <u>hypervisor</u> allows multiple VMs to run on a single machine.

Each VM includes <u>a full copy of an operating system, the application, necessary binaries and libraries.</u>  



![image-20211029123009356](/Users/phoebemac/Library/Application Support/typora-user-images/image-20211029123009356.png)



### Docker Image

Image: a template for creating an environment -> snapshots.

Contains OS, required software, app code.



### Docker Container

Running instance of an image.

Download an image -> run a container from the image.

If an image changes or is updated, the next download will not drag down every layer. Layers are cached and piped up.

```
# See all images we have
docker images
```



After downloading an image, create a container, which is a running instance of an image.

```
docker run jupyter/base-notebook:latest

# Seel all containers and status we have
docker container ls

# Example output 
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS NAMES
e29a4715b09f  jupyter/base-notebook:latest  "tini -g -- start-no…"  10 seconds ago  Up 9 seconds   8888/tcp  elastic_dubinsky
```

Run the container in the detached mode `-d`, not making the process hanging (stuck in the terminal).

```
docker run -d jupyter/base-notebook:latest
```



Exposing port, add `-p 8080:8888` before running the container. When ever we run 8080 on localhost, we want it to be mapped to port 80 on the container.

The port on the container should be checked first (usually specified by the service). The localhost port is customizable, while the container port is pre-configured.

```
# Stop container 
docker stop <container id>

# If not expose port, we have no way to access the service
docker run -d -p 8080:8888 jupyter/base-notebook:latest
```

Can map to multiple ports, making the container accessible to many ports.

```
docker run -d -p 3000:8888 -p 8080:8888 jupyter/base-notebook:latest
```



#### Manage Containers

##### 1. Deletion

```
# Get the info of running containers
docker ps

# Stop docker
docker stop <container id>

# Get the container that are not running (-a all)
docker ps -a
```

Every time we start a container, we are actually creating a new container with a new name. Instances are never reused. With many previously used, while currently out-dated containers of the same image, it can bring waste. Therefore, deleting unused containers is necessary.

```
# Delete container
docker rm <docker is> 

# This instance will no longer exits in the "docker ps -a" list

# Get only info about the id (numeric list)
# q stands for quiet mode
docker ps -aq

# Delete all containers - use embedded commands
docker rm $(docker ps -aq)

# Force removal, even when it is running and not recommended to be removed
docker rm -f $(docker ps -aq)
```



##### 2. Naming

A random name will be assigned, if do not specify name in `docker run` command.

Use `--name` to assign a name.

```
docker run --name test-jupyter -d -p 8080:8888 jupyter/base-notebook:latest


docker ps
docker stop test-jupyter
docker start test-jupyter
```



##### 3. Format

Format `docker ps` results.

```
docker ps --format="ID\t{{.ID}}\nNAME\t{{.Names}}\nIMAGE\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"

export FORMAT="ID\t{{.ID}}\nNAME\t{{.Names}}\nIMAGE\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"

docker ps --format=$FORMAT
```



#### Volumes

Allow us to share data between containers, or hosts and containers.

Through the Container and the Filesystem (Docker area is allocated as portion of the Filesystem), we create a volume.

Files or folders are added to the volume inside the container.



<img src="/Users/phoebemac/Library/Application Support/typora-user-images/image-20211029145357001.png" alt="image-20211029145357001" style="zoom:50%;" />



##### 1. Share files between a container and a host

How to override the Nginx welcome page by mounting a volume?

Create a volume between the host and the container. Have a file on the host machine, mount it to the container.

1. Create and write the file on the host machine.

2. Start the container.

3. Mount the file to the container.

   

```
cd <the folder hosting the target files>

# Mount the file with read-only mode (ro)
docker run --name test-volume -v $(pwd):/usr/share/nginx/html:ro -d -p 8080:80 nginx
```

Note: path after `$(pwd)` is the required path by the service. Need to check on the home page on Docker. This path is pre-configured, not customized.

Do not need to start the container again, if the file is modified, it will automatically be updated in the container.

If we have a file updated inside the container, it will also show on the host.

```
# Execute the bash command in interactive mode in the container
docker exec -it <container name> bash

# After entering the container, check the structure
ls -al

# Run again with ro flag removed, so that the container can modify the folder
docker run --name test-volume -v $(pwd):/usr/share/nginx/html -d -p 8080:80 nginx

cd /usr/share/nginx/html
touch about.html
# When check the folder where $pwd direct to on the host, a file about.html exists.
```



##### 2. Share files between containers

With tag `--volumes-from <container list to be shared from>`, a container can access files of the target container. Both should be in the running mode.

```
docker run --name test-volume2 --volumes-from test-volume -d -p 8081:80 nginx
```



### Dockerfile

Defines how images are built, used to create our own images. In addition, do not have to mount any volumes.

Use a Dockerfile to create an image, and run it to get a customized container.

`FROM baseImage`: usually never build an image form scratch. Always, build something from existing one.

```
# The base image should be pulled or downloaded first.
FROM nginx:latest
# The working directory, if not specified, then create a new one. Every command after it, will be operate in /app.
WORKDIR /app
# Add everything under the folder to the pre-confirgured destination path 
ADD . /usr/share/nginx/html
```



#### Docker Build

Have to specify a tag for reference in format of "name:tag".

`.` Is used to specify the parent directory to find the Dockerfile.

```
docker build --tag test-build:mlatest .
docker image ls
```





```
docker run --name repo alpine/git clone <git repo link>

docker cp repo:/git/getting-started/ .

cd getting-started

docker build -t docker101tutorial .

docker run -d -p 80:8888 --name docker-tutorial docker101tutorial 

docker tag docker101tutorial xiuxianli/docker101tutorial 

docker push xiuxianli/docker101tutorial
```



#### .dockerignore

Like .gitignore.

Example content of .dockerignore:

```
node_modules
# Dockerfile is only used to build image, not needed elsewhere. It can be ignored.
Dockerfile 
.git
<folder/*>
```



### Alpine

Significantly reduce the size of the container.

```
# Pull the latest alpine version
docker pull node:lts-alpine
```





### Docker Registreis

Highly scalable server side application that stores and lets you distribute Docker images.

Want we need is not build and use on the host machine. This does not need distribution to the docker. In stead, we usually need to push the configured image, and let it run on a remote machine. Therefore, we need a place to share and distribute.

Host ----push----> Docker Registry

Docker registry provider:

- Docker Hub
- Quay.io
- Amazon ECR



#### Docker Push

When configuring, always use the identifier remotely. If it does not have, `docker tag` it first.

```
docker push <hub username>/<repo name>:<tagname>

# Login to the docker hub first
docker login

# Tag the image first
docker tag <local name>:<local tag> <username>/<repo name>:<tag>

docker push <username>/<repo name>:<tag>

# Inpect an image info in the json format
docker inpect <name/id>

docker logs <container id>
```



#### Docker Exec

Sometime we want to get inside the container, and see what is happening there.

`-i` --interactive Keep    STDIN open even if not attached

`-t` --tty    Allocate a pseudo-TTY

```
docker inpect <container id>

# Search 'cmu' to find the command or location of bash

docker exec -it <container id> /bin/sh

# Then we can get inside the container
```

