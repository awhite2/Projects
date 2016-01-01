#!/bin/bash

# source this file to set your python path on the macs

top='/Volumes/TEMPORARY SAVE FOLDER/'
pyopengl="$top/Library/Python/2.7/site_packages"
tw="$top/307/pytw"
export PYTHONPATH="$pyopengl":"tw":"$PYTHONPATH"


echo "PYTHONPATH is $PYTHONPATH"
