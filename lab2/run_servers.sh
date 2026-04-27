#!/bin/bash

echo "Starting gunicorn..."
cd /home/aida/2026-MAI-Backend-A-Mashrabova
gunicorn --workers 4 --bind 127.0.0.1:8000 lab2.wsgi_app:application &

echo "Checking nginx..."
sudo nginx -t
sudo systemctl restart nginx

echo "Servers are running:"
echo "  - Public: http://localhost:8080/public/"
echo "  - Gunicorn via nginx: http://localhost:8080/gunicorn"
echo "  - Direct gunicorn: http://127.0.0.1:8000/"
