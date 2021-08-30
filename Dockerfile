FROM jenkins/jenkins:lts-jdk11
user root
RUN apt-get update -y  && apt-get -y upgrade 
RUN apt-get install python python3-pip -y 
COPY requirement.txt .
RUN pip install -r requirement.txt