#!/bin/bash
echo "Installing openjdk"
sudo yum install -y java-1.8.0-openjdk-devel
echo "Configuring Java"
sudo alternatives --set java /usr/lib/jvm/jre-1.8.0-openjdk.x86_64/bin/java
echo "Removing old version"
sudo yum remove -y java-1.7.0-openjdk-devel
echo "Downloading Maven"
sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo 
sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
echo "Installing Apache Maven"
sudo yum install -y apache-maven
export JAVA_HOME=/usr/lib/jvm/java
echo "Downloading Maven SDK"
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install gradle 6.5
