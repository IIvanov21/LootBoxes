apt-get update
apt install curl -y
curl https://get.docker.com | sudo bash
usermod -aG docker $(whoami)
newgrp docker