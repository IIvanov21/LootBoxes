#!/bin/bash
scp $WORKSPACE/docker-compose.yaml ansible@swarm-manager
ssh -i ~/.ssh/ansible_id  ansible@swarm-manager  "export DATABASE_URI=$DATABASE_URI && docker stack deploy --compose-file docker-compose.yaml loot-boxes"