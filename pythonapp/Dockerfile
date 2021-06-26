FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python python-pip
RUN pip install flask
RUN useradd -ms /bin/bash siva
USER siva
COPY . /opt/
EXPOSE 8080
# CMD
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host 0.0.0.0 --port 8080
