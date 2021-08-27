FROM jenkins/jenkins
user root
RUN apt-get update -y && apt-get install python python3-pip -y && pip install xlrd
