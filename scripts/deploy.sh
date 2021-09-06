#!/bin/bash
scp $WORKSPACE/docker-compose.yaml jenkins@swarm-manager
ssh -i ~/.ssh/id_rsa  jenkins@swarm-manager  "export DATABASE_URI=$DATABASE_URI && docker stack deploy --compose-file ~/LootBoxes/docker-compose.yaml loot-boxes"