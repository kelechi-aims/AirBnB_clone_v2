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

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://github.com/anotibills;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# test that nginx is working fine
sudo nginx -t

# Restart nginx to effect changes
sudo service nginx restart
