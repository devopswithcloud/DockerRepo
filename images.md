``` bash
docker pull imagename

docker image pull alpine:3.6 # Just pulls the image, doens't run (dont create a contianer)

docker images --no-trunc
docker images --filter=reference='alpine'



# List image name by tag
docker images alpine:3.6

# List full length Image ID:
docker images --no-trunc

# List out Images with Filter
docker images --filter=reference='alpine'

# Inspect image details
docker inspect alpine:3.6

# Custom ubuntu  Image >> commit
$ docker container run -it --rm --name ubuntucon ubuntu:16.04 /bin/bash

Inside the docker container run the check if ipconfing, ping are available, if now execute the below commands

$ apt update -y
$ apt install iputils-ping wget curl net-tools -y

After installation test with ping and curl , ifconfig commands

Now ctrl + p +q to come out of the container 

$ docker container commit <contianer_id> devopswithcloudhub/ubuntucustom:<tag_name>

docker export <container_id> > customubuntu.tar
docker import - sivaimage < customubuntu.tar

# Custom Image >> Ubuntu VM > Springboot app

Docker can build images by reading instructions from a Dockerfile

Lets take one more application as an example
    * This application is based on java
    * This application runs on port 8080


sudo apt update -y
sudo apt install maven
sudo apt-cache search openjdk
apt install openjdk-8-jdk
java -jar target/*.jar

# Spring boot inside container 
docker run -it -p 8080:8080 --name springubuntu ubuntu:18.04

apt update 
apt install openjdk-8-jdk -y
ctrl p+q
docker container cp *.jar springubuntu:/
docker attach springubuntu 
java -jar *.jar
ctrl p+q

# Creating an image now out of container 
docker commit springubuntu springubuntuimage:new

docker run -it -p 8090:8080 --name springnew springubuntuimage:new 
    docker attach springnew
    java -jar *.jar

# Exporting a container to a tar file
docker export <container_id> > springcontainer.tar

# Importing tar as an image
docker import - springimage < springcontianer.tar

#Creating an image from the above image
docker run -dit -p 8090:8080 --name tarcontainer springimage /bin/bash

# Creting an tar file from an image
docker save -o mynginx1.tar nginx

docker rmi nginx

loading image back from tar dfile
docker load < mynginx1.tar
```



```bash
# image diffence
FROM ubuntu:18.04
RUN apt update
```
