
git clone https://github.com/IIvanov21/LootBoxes.git
cd LootBoxes
git checkout dev
git pull
sudo apt install python3 python3-pip python3-pytest
pip3 install -r service_1/requirements.txt -r service_2/requirements.txt -r service_3/requirements.txt -r service_4/requirements.txt
bash scripts/docker.sh
bash scripts/docker-compose.sh
