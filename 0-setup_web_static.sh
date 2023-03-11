#!/usr/bin/env bash
# a script that setup server deployment
sudo apt-get update -y
sudo apt-get nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
echo "
<html>
  <head>
    </head>
      <body>
          Holberton School
	    </body>
	    </html>
	   " > /data/web_static/releases/test/index.html

ln -fs /data/web_static/releases/test/ /data/web_static/current

chown ubuntu:ubuntu /data/

sed '39 i \ \t location /hbnb_static{\n\t alias /data/web_static/current/; \n\t}' /etc/nginx/sites-available/default

sudo nginx restart
