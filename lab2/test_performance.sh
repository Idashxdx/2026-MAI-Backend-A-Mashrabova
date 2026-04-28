#!/bin/bash
echo -e "\nPicture"
curl -I http://localhost:8080/public/test.jpg
echo "Password"
curl http://localhost:8080/gunicorn
echo -e "\nDirect access"
curl http://127.0.0.1:8000/

echo -e "\n\nTesting public location..."
wrk -t8 -c972 -d20s http://127.0.0.1:8080/public/test.jpg
sleep 3
echo -e "\n+10%"
wrk -t8 -c1069 -d20s http://127.0.0.1:8080/public/test.jpg
sleep 3
echo -e "\n\nTesting gunicorn location..."
wrk -t8 -c150 -d15s http://127.0.0.1:8080/gunicorn
sleep 3
echo -e "\n+10%"
wrk -t8 -c165 -d15s http://127.0.0.1:8080/gunicorn
sleep 3
echo -e "\n\nTesting WSGI directly..."
wrk -t8 -c150 -d15s http://127.0.0.1:8000/
sleep 3
echo -e "\n+10%"
wrk -t8 -c165 -d15s http://127.0.0.1:8000/

