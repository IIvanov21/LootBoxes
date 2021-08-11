#!/bin/bash
#export the environment variables in the script
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
#Terminate if the script fails
set -e

#Build image
docker-compose build --parallel

#Push images
docker login -u $DOCKER_ID_USR -p $DOCKER_ID_PASSWORD

docker-compose push

exit