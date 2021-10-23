
### **` Basic commands`**
```bash
docker run -it centos bash
  cat /etc/redhat-release

docker run centos -d sleep 2000

docker container run busybox 

# To verify the various linux processes inside the container
docker run -it alpine /bin/sh
  $ top 
  $ ip addr
  # df -h
ps aux


docker ps # list all running containers

docker ps -a #

docker stop # Stop a running contianer

docker rm container_id # Remove a contianer

docker container rm $(docker ps -aq) # Removes all containers (stopped and running)

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

docker container -h

docker container ls 

docker container run busybox # busybox is a simple contianer , which runs ssh

docker container run busybox hostname -i

docker run -d -P nginx

docker container top <container_id>

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
