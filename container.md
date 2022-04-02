### **`Container Commands`**

```syntax```:
> * docker docker-object sub-command [options] [arguments]
> * Example: 
>   * docker contianer list

```Pull the Image```
> docker pull ubuntu:16.04

``` Pull + Create the image```
> docker container create httpd


### **` Container  commands`**
```bash

# Pull the image
docker pull ubuntu:16.04

# Pull + Create the Container
docker container create httpd

# Start the container
docker container start <CONTAINER_ID>

# Pull + Create + Start
docker run httpd

# To create the container and get the data for a file
docker run ubuntu cat /etc/*rele*

# Detached mode
docker run -d httpd

#Container Name
docker run -d --name sivahttpd httpd

# To create a container with interactive mode 
docker run -it centos bash
  cat /etc/redhat-release

# To run a container with detached mode
docker run centos -d sleep 2000

# Busybox contianer
docker container run busybox 

docker container run busybox hostname -i

# To verify the various linux processes inside the container
docker run -it alpine /bin/sh
  $ top 
  $ ip addr
  $ df -h

# list all running containers
docker ps 

# List all running and stopped containers
docker ps -a 

# Stop a running contianer
docker stop 

# Stops and Remove a contianer
docker rm container_id 

# list all container ids in all states(running, stopped, exited)
docker ps -aq 

# Removes all containers (stopped and running)
docker container rm $(docker ps -aq) 

# inspecting a object (Container,images,network,volume)
docker container inspect <CONTAINER_ID>

# container Logs
docker container logs <containerID>

# Remove the container once the work is done
docker container run --rm <imagename>

# setting a hostname to a container
docker run -it --name sivaapp --hostname sivaspp ubuntu


# Copying contents to and from Containers
# Copying Contents into Container
docker run -it ubuntu
  create a file by name containerlog.txt
docker container cp <containeID>:/containerlog.txt .
vi hostlog.txt # in host
docker container cp hostlog.txt <containeID>:/
docker exec -it <containeID> /bin/sh

# To get Top containers
docker container top <container_id>
docker images

docker rmi imagename

docker contianer ls

docker container ls -q

docker container ls -aq

docker container run -it ubuntu

docker container run --name myubuntu -it ubuntu

docker container rename myubuntu newubuntu

# Nginx Examples
docker container run -d nginx

docker container run --name nginxbash -it nginx /bin/bash
    nginx -g 'daemon off;'

docker container run -d --name nginxexec nginx

docker container exec -it nginxexec ls /usr/share/nginx/html
docker container exec -it nginxexec /bin/bash

docker container attach newubuntu

```

### Docker Container commands
```bash
docker images

docker image ls -h

docker image pull nginx

docker image inspect <image_id>







docker container attach <container_id> # we will be in the stdout , if we kill the process the container will be killed.

docker container start <container_id>

docker container stats <container_id> # live stats for the usage of the container 

docker exec -it <container_id> /bin/bash
  ls /usr/share/nginx/html/

docker exec -it 7d3c2c4460c6 ls /usr/share/nginx/html/

docker container pause amazing_engelbart # Pause all processes within one or more containers.

docker container unpause <container_id>

docker container prune # Remove all stopped contianers 

docker run busybox # this will be stopped as process is done

docker container run --rm busybox
```
