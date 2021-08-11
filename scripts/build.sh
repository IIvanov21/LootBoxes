#!/bin/bash
sudo su - jenkins <<EOF


#Terminate if the script fails
set -e

#Build image
docker-compose -f $WORKSPACE/docker-compose.yaml build --parallel

#Push images
docker login -u $DOCKER_ID_USR -p $DOCKER_ID_PSW

docker-compose push

exit
EOF