#!/bin/sh

compose_name=$(basename "$(pwd)")
volumes="${compose_name}_media ${compose_name}_postgres_data"

for volume in ${volumes}; do
    volume_directory=$(docker volume inspect "${volume}" | jq '.[0].Mountpoint')
    tar cvf backup/${volume}.tar -C $volume_directory .
done
