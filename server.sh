#! /bin/bash

echo "starting docker deployment"

docker build -t todoapp .

docker tag todoapp brymopaul/todoapp

docker push brymopaul/todoapp

echo "finished docker deployment and deploying to kubernetes"

kubectl apply -f deployment/*