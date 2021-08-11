if [-x "$(command -v docker)"]; then
    echo "Docker is installed!"
else
    echo "Installing Docker"
    sudo apt-get update
    sudo apt install curl -y
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker $(whoami)
    newgrp docker
fi