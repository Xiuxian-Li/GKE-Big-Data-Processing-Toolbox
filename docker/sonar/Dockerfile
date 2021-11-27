FROM sonarqube:latest
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472.zip
RUN unzip sonar-scanner-cli-4.6.2.2472.zip
RUN export PATH=$PATH:sonar-scanner-4.6.2.2472/bin
EXPOSE 9000