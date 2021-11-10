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
git clone https://github.com/ethgreen/ethgreen-blockchain.git -b latest --recurse-submodules
cd ethgreen-blockchain

sh install.sh

. ./activate

# The GUI requires you have Ubuntu Desktop or a similar windowing system installed.
# You can not install and run the GUI as root

sh install-gui.sh

cd ethgreen-blockchain-gui
npm run electron &



To Update/Upgrade from previous version
cd ethgreen-blockchain
. ./activate
ethgreen stop -d all
deactivate
git fetch
git checkout latest
git reset --hard FETCH_HEAD --recurse-submodules

# If you get RELEASE.dev0 then delete the package-lock.json in ethgreen-blockchain-gui and install.sh again

git status

# git status should say "nothing to commit, working tree clean", 
# if you have uncommitted changes, RELEASE.dev0 will be reported.

sh install.sh

. ./activate

ethgreen init

# The GUI requires to have Ubuntu Desktop or a similar windowing system installed.
# You can not install and run the GUI as root user.
./install-gui.sh

cd ethgreen-blockchain-gui
npm run electron &

INSTALL FOR MAC

# Checkout the source and install
git clone https://github.com/ethgreen/ethgreen-blockchain.git -b latest --recurse-submodules
cd ethgreen-blockchain

sh install.sh

. ./activate

ethgreen init

# install gui
sh install-gui.sh

# activate GUI
cd ethgreen-blockchain-gui
npm run electron &
