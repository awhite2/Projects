#!/bin/bash

# source or run this file to refresh TW.py and our demos
top='/Volumes/TEMPORARY SAVE FOLDER/'
pyopengl="$top/Library/Python/2.7/site_packages"
tw="$top/307/pytw"

cd "$top/307"

echo "install pytw stuff"
curl -O http://cs.wellesley.edu/~cs307/pytw.tgz

# if we don't remove the old stuff, old files stay around.
rm -rf pytw
tar xzf pytw.tgz
