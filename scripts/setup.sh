sudo su - jenkins <<EOF
git c
sudo apt install python3 python3-pip python3-pytest
pip3 install -r ${WORKSPACE}/LootBoxes/service_1/requirements.txt -r ${WORKSPACE}/LootBoxes/service_2/requirements.txt -r ${WORKSPACE}/LootBoxes/service_3/requirements.txt -r ${WORKSPACE}/LootBoxes/service_4/requirements.txt
bash scripts/docker.sh
bash scripts/docker-compose.sh
exit
EOF