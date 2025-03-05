#!/bin/sh
set -e

host="db"
port="5432"

echo "Waiting for PostgreSQL to start..."

while ! nc -z $host $port; do
  sleep 1
done

echo "PostgreSQL is up - executing command"
exec "$@"
