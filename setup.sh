#!/bin/bash

#run this script using source instead of bash

#create .venv if venv does not exist
#otherwise, run the activate .venv
if [ -d ./.venv/ ]; then
  echo "A virtual environment already exist exists."
  source ./.venv/bin/activate
else
  echo "No virtual environment installed"
  sudo apt-get update
  sudo apt install python3.10-venv
  python3 -m venv ./.venv
fi
