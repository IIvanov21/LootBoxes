#!/bin/bash
scp ~/LootBoxes/docker-compose.yaml ansible@swarm-manager
ssh -i ~/.ssh/ansible_id  ansible@swarm-manager  "docker stack deploy --compose-file docker-compose.yaml loot-boxes"