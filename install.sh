#!/bin/bash
apt update
apt install python3-pip -y
pip3 install sympy --upgrade
if [ $? -eq 1 ] ; then
    echo "sympy could not be installed"
fi
#uncomment for sserver installation
exit

pip3 install django --upgrade
if [ $? -eq 1 ] ; then
    echo "django could not be installed"
fi
