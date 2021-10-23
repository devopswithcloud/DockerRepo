## DOCKER DEFAULT BRIDGE NETWORKING

```bash
#List the network
docker network ls
docker network inspect bridge

# Create a network
docker network create network1
docker network ls
docker network inspect network1

# Creating a containers in default bridge network
docker container run -dit --rm --name c1 sivaubuntu bash
docker container run -dit --rm --name c2 sivaubuntu bash
docker container run -dit --rm --name c3 sivaubuntu bash
    # we can ping ip address in default bridge network , but ca't ping using there names

sudo apt-get install bridge-utils
# brctl stands for Bridge Control. In Linux, this command is used to create and manipulate ethernet bridge. This is typically used when you have multiple ethernet networks on your servers, and you want to combine them and present it as one logical network.
brctl show

# Creating a new network
docker network create network1

# docker info > gives Network list we can create

# Creating a containers in new network
 docker container run -dit --rm --name c4 --net network1 sivaubuntu bash
 docker container run -dit --rm --name c5 --net network1 sivaubuntu bash

# Creating a network with custom subnet
docker network create sivanetwork --driver=bridge --subnet=192.168.10.0/24
docker container run --name c6 -dit --network sivanetwork centos:7
docker container run --name c7 -dit --network sivanetwork centos:7

#Attach siva network to c1
docker network connect sivanetwork c1
docker exec -it c7 ping c1

# Disconnect siva network to c1
docker network disconnect sivanetwork c1
```

## Network custom using subnets and gateways
```bash
docker network create --subnet 10.3.0.0/24 --gateway 10.3.0.1 bridgecustom

 docker network create --subnet 10.1.0.0/16 --gateway 10.1.0.1 --ip-range=10.1.4.0/24 --driver=bridge --label=myownnetwork bridgecustom

docker container run --name myownnetcontainer -it --network bridgecustom centos /bin/bash
    yum update -y
    yum install net-tools -y
    ifconfig
    netstat -rn # Gives the gateway address
    cat /etc/resol.conf

# Create a container with specific ip address
docker container run -d --name network-test03 --ip 10.1.4.10 --network bridgecustom nginx

#Create an internal network:
docker network create -d bridge --internal localhost

#Create a Nginx container that is not publicly accessible:
docker container run -d --name private-nginx -p 8081:80 --network localhost nginx

docker network create -d bridge --internal localhost

```



### Docker Host Network

```bash
# Create and start the container as a detached process on Host network
docker run --rm -d --network host --name my_nginx nginx
- docker ps
    * Enter public ip in browser and nginx should load
- sudo netstat -tulpn | grep :80
    * TcpUdpListPortNumbers
- docker container stop my_nginx
```


