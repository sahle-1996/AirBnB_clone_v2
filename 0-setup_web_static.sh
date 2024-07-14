#!/usr/bin/env bash
# This script sets up the web server for deployment of web_static

# Install Nginx if it's not already installed
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

# Create directory structure for web_static deployment
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# Create a simple HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to /data/web_static/releases/test/
sudo ln -sfn /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply the configuration changes
sudo systemctl restart nginx
