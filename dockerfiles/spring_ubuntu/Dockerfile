FROM ubuntu:18.04
RUN apt update && apt install openjdk-8-jdk -y && apt install wget -y
RUN wget https://storage.googleapis.com/sivak8dpublicrepo/spring-petclinic-2.4.5.jar
# EXPOSE 8080
CMD ["java", "-jar", "spring-petclinic-2.4.5.jar"]
# CMD java -jar target/*.jar


# java -jar target/*.jar 

 
