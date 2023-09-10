#!/bin/bash

echo 'Primo Di Tutto'

YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

printf "${GREEN}I now install dependencies${NC}\n\n"

sudo apt install git python3-tk python3-ttkthemes python3-psutil install xterm -y

clear

cd


if [ -d "$HOME/primo-di-tutto" ] 
then
    printf "${YELLOW}[UPDATE]${NC}I will install the newest version.\n\n" 
    rm -rf $HOME/primo-di-tutto
    git clone https://github.com/actionschnitzel/surface-on-ubuntu-gui.git
    cd primo-di-tutto
else
    printf "${YELLOW}[NEW INSTALL]${NC}I will now install Primo\n\n"
    git clone https://github.com/actionschnitzel/surface-on-ubuntu-gui.git
    cd primo-di-tutto
fi

clear

chmod +x primo.py

DIRECTORY="$(readlink -f "$(dirname "$0")")"
if [ -z "$DIRECTORY" ] || [ "$DIRECTORY" == "$HOME" ] || [ "$DIRECTORY" == bash ];then
  DIRECTORY="$HOME/primo-di-tutto"
fi

echo "[Desktop Entry]
Version=2.1
Exec=${DIRECTORY}/start.sh
Name=Primo
GenericName=Primo
Encoding=UTF-8
Terminal=false
Type=Application
Categories=System
Icon=${DIRECTORY}/icon.png
Path=${DIRECTORY}/" > ~/Desktop/primo.desktop

chmod +x ~/Desktop/primo.desktop


cd
clear

echo 'Primo Di Tutto'

echo  '
 ____ ____ ____ ____ _________ ____ 
||D |||O |||N |||E |||       |||! ||
||__|||__|||__|||__|||_______|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|'

printf "\n${GREEN}You can close this window now\n${NC}"
