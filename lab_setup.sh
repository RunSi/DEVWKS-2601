#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd lab_build
Vagrant up
cd ..
