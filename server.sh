#! /bin/bash

echo "starting docker deployment"

docker build -t todoapp .

docker tag todoapp brymopaul/todoapi

docker push brymopaul/todoapi

echo "finished docker deployment and deploying to kubernetes"

#kubectl apply -f deployment/*
