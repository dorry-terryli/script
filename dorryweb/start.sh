#!/bin/bash

sudo docker-compose up
sudo python insert.py
sudo service docker stop 
sudo docker daemon -H unix:///var/run/docker.sock -H tcp://0.0.0.0:10000 --api-enable-cors=true
