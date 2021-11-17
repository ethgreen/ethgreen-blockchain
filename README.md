Welcome to ETHGreen Blockchain

ETHGreen blockchain is a fork from STAI and Chia blockchain including features implemented by Covid blockchain.

About the project :
1/10 of all miner rewards will go to a donation wallet, which earnings will be donated to charitable causes worldwide. In addition, as compensate for mining and its consequences, the CO2 emissions, we´ll buy land anywhere in the world and leave it back to nature.
Block reward: 20 XETH

Full node :
dns-introducer.eth-green.com
or
84.150.173.139
Port : 6262

Join our Community : https://discord.gg/uWnhFbMJTn
Twitter: https://twitter.com/ethgreenproject
Website : https://eth-green.com


Install instruction for UBUNTU/DEBIAN:
UBUNTU 21.04 not tested. Working on 20.04 fine. 
If you want to install on Ubuntu 18.04 LTS you should use Python 3.7 instead: 
sudo apt-get install python3.7-venv python3.7-distutils python3.7-dev git lsb-release -y

HOW TO INSTALL:

sudo apt-get update
sudo apt-get upgrade -y

# Install Git
sudo apt install git -y

# Checkout the source and install
git clone https://github.com/ethgreen/ethgreen-blockchain.git
cd ethgreen-blockchain

sh install.sh

. ./activate

# Install and run timelord
cd ethgreen-blockchain
. ./activate
sh install-timelord.sh
ethgreen init
ethgreen start timelord
ethgreen show -a dns-introducer.eth-green.com:6262

# The GUI requires you have Ubuntu Desktop or a similar windowing system installed.
# You can not install and run the GUI as root

sh install-gui.sh

cd ethgreen-blockchain-gui
npm run electron &


# The GUI requires to have Ubuntu Desktop or a similar windowing system installed.
# You can not install and run the GUI as root user.
./install-gui.sh

cd ethgreen-blockchain-gui
npm run electron &

INSTALL FOR MAC

# Checkout the source and install
git clone https://github.com/ethgreen/ethgreen-blockchain.git
cd ethgreen-blockchain

sh install.sh

. ./activate

ethgreen init

# install gui
sh install-gui.sh

# activate GUI
cd ethgreen-blockchain-gui
npm run electron &
