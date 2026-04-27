#!/bin/bash

echo "Testing public location..."
ab -n 1000 -c 10 http://localhost:8080/public/test.jpg

echo "Testing gunicorn location..."
ab -n 1000 -c 10 http://localhost:8080/gunicorn

echo "Testing WSGI directly..."
ab -n 1000 -c 10 http://localhost:8000/
