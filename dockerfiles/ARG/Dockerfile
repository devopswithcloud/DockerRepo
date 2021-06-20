FROM ubuntu:18.04
RUN apt update -y && apt install openjdk-8-jdk -y && apt install wget -y
ARG SRC_DIR=/tmp/java
RUN mkdir -p $SRC_DIR
WORKDIR $SRC_DIR
ADD https://storage.googleapis.com/sivak8dpublicrepo/spring-petclinic-2.4.5.jar $SRC_DIR/spring-petclinic.jar 
EXPOSE 8080
CMD ["java", "-jar", "spring-petclinic.jar"]

