#!/bin/bash

# check if python is installed
if [[ "$(python3 -V)" =~ "Python 3" ]]
	then echo "Python 3 is installed"
	else echo "Installing Python 3" && sudo apt-get update && sudo apt-get install python3
fi
# python3 -m venv wordle-venv
WORDLE_VENV=./wordle-venv
if [[ -e "$WORDLE_VENV" ]]
	then echo "Wordle VENV exists"
	else echo "Wordle VENV does not exist" 
fi
# check if venv already exists
source wordle-venv/bin/activate
#pip3 install -r requirements.txt
