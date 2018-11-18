#!/bin/bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd lab_build
Vagrant up
cd ..
