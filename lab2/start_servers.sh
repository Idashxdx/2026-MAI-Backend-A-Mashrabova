#!/bin/bash

sudo cp lab2/nginx.conf /etc/nginx/sites-available/lab2
sudo ln -s /etc/nginx/sites-available/lab2 /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

gunicorn --workers 4 --bind 127.0.0.1:8000 lab2.wsgi_app:application
