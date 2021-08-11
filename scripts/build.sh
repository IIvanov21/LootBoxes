#!/bin/bash
sudo su - jenkins <<EOF


#Terminate if the script fails
set -e

#Build image
docker-compose -f {$WORKSPACE}/LootBoxes/docker-compose.yaml build --parallel

#Push images
docker login -u $DOCKER_ID_USR -p $DOCKER_ID_PASSWORD

docker-compose push

exit
EOF