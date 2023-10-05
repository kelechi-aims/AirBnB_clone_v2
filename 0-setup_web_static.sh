#!/usr/bin/env bash
# Script to set up servers to deploy web static

# install nginx if if doesnt exist
sudo apt-get -y update
sudo apt-get -y install nginx

# creating folders and files that are not available
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# creating fake html file
sudo echo "<html>
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test /data/web_static/current

# change owner of /data to ubuntu
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu:ubuntu /data/

# Update the Nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx to effect changes
sudo service nginx restart
