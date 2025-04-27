#!/usr/bin/env bash

rm /var/lib/dpkg/lock
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y wine  
wget https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe
echo "[+]Download Python in Drive_c of wine"
wine msiexec /i python-3.12.9-amd64.exe
sudo pip install pynput==1.6.8 pyinstaller==3.3.1 
sudo pip install rich==13.3.1 pyfiglet==0.8.post0
echo "[+]Go in ~/.wine/drive_c/ in Python Folder and download Pyinstaller there with python.exe -m pip install pyinstaller"

