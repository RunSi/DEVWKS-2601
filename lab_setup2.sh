#!/bin/bash

mkdir -p ~/workspace/devnet-2595
cd ~/workspace/devnet-2595

# create python virtual environment
$(pyenv root)/versions/3.6.7/bin/pyvenv .
#python3.4 -m venv .

source bin/activate
pip install --upgrade pip setuptools

pip install -r requirements.txt
git clone https://github.com/RunSi/DEVWKS-2601
