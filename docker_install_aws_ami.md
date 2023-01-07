## Install Docker on AMI Instance in EC2 
* Update the packages
```bash
sudo yum update -y
```
* Install the most recent Docker CE edition
 ```bash
 sudo yum install docker -y
```
* Start the docker service 
```bash
sudo service docker start 
```
* Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
```bash
sudo usermod -a -G docker ec2-user
```
