#!/usr/bin/env bash
# Script to set up servers to deploy web static

# install nginx if if doesnt exist
sudo apt-get -y update
sudo apt-get -y install nginx

# creating folders and files that are not available
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# creating fake html file
sudo echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test /data/web_static/current

# change owner of /data
sudo chown -R ubuntu:ubuntu /data/

#using sed command
sudo sed -i "41i \\\nlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default

# test that nginx is working fine
sudo nginx -t

# Restart nginx to effect changes
sudo service nginx restart
