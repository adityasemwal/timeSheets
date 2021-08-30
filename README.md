# Running via virtual env locally
###  python integrate.py T002,T006,T017,T007,multi jan21

# Running via Docker
### docker pull jenkins/jenkins:lts-jdk11
### docker build -t timesheets .
### docker run -p 8088:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home timesheets
### check http://localhost:8088/

