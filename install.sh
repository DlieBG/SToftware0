#!/bin/bash
apt update
apt install python3 python3-pip -y
python3 -m pip install sympy regex colorama -U
exit # Uncomment for server installation
apt install python3-venv -y
python3 -m venv .
source bin/activate
python3 -m pip install django sympy regex -U
echo ""
echo "Don't forget to check if the BASE_URL in expr.py i0s correct"
echo "Don't forget to check if debug = False when you go into production"
echo "You need root privilegies to open a port below 1024, if you don't want this choose an other port and change it in the web interface in call.php"
echo "when running the server use the venv python3 especially with sudo"
