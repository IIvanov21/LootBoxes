#!/bin/bash
sudo su - jenkins <<EOF


#Terminate if the script fails
set -e

export DATABASE_URI=${DATABASE_URI}
#Build image
docker-compose -f $WORKSPACE/docker-compose.yaml build --parallel

#Push images
docker login -u $DOCKER_ID_USR -p $DOCKER_ID_PSW

docker-compose -f $WORKSPACE/docker-compose.yaml push

EOF