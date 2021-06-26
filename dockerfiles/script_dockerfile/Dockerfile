# nginx , nginx base image  or ubuntu : n
FROM ubuntu
RUN apt-get update 
RUN apt-get install nginx -y
COPY index.html /var/www/html
COPY ["script.sh", "/root/script.sh"]
# RUN chmod +x /root/script.sh
EXPOSE 80
#script.sh
ENTRYPOINT /root/script.sh
# CMD ["nginx", "-g", "daemon off;"]
