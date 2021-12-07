#!/bin/sh

ARG=$1

case $ARG in

    local)
        docker-compose up
        ;;
    
    test)
        docker-compose run app django-admin test
        ;;

    *)
        echo "COMMAND NOT FOUND"
        echo "Usage: $0 {local|test}"
        ;;
esac