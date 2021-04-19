#!/bin/bash

echo "Running app..."

while ! nc -z $POSTGRES_PORT_5432_TCP_ADDR $POSTGRES_PORT_5432_TCP_PORT; do
sleep 5;
echo "DB not running yet..."
done

cd purchase_system && python -m uvicorn adapters.api.main:app --reload --host $APP_HOST --port $APP_PORT