#!/bin/bash

set -e

#Build image
docker-compose build --parallel

#Push images
#docker login -u $DOCKER_ID_USR -p $DOCKER_ID_PASSWORD
docker-compose push