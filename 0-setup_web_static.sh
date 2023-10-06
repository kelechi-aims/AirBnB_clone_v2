#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx
# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
str_con="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$str_con" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
