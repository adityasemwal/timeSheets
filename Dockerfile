FROM jenkins/jenkins
user root
RUN apt-get update -y && apt-get install python python-pip -y && pip install xlrd