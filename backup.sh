#!/bin/sh
compose_name=$(basename "$(pwd)")
volumes="${compose_name}_media ${compose_name}_postgres_data"
date=$(date '+%Y-%m-%d')
for volume in ${volumes}; do \
    echo "### Backing up ${volume}"; \
    volume_directory=$(sudo docker inspect ${volume} | grep Mountpoint | awk '{ print $2 }' | tr -d ',"'); \
    tar cvf backup/${volume}-${date}.tar -C ${volume_directory} .; \
done
