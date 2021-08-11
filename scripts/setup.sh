sudo apt install python3 python3-pip python3-pytest
pip3 install -r $WORKSPACE/service_1/requirements.txt -r $WORKSPACE/service_2/requirements.txt -r $WORKSPACE/service_3/requirements.txt -r $WORKSPACE/service_4/requirements.txt
bash $WORKSPACE/scripts/docker.sh
bash $WORKSPACE/scripts/docker-compose.sh