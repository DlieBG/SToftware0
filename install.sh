#!/bin/bash
apt install python3 -y
apt install python3-sympy -y
if [ $? -eq 1 ] ; then
    echo "It looks your Linux has no python3-sympy package\n please look under dependencies an install it yourself"
fi
