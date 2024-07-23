# Development commands

run_dev:
	docker compose -f docker-compose.dev.yml up -d
build_dev:
	docker compose -f docker-compose.dev.yml up -d --build
logs_dev:
	docker compose -f docker-compose.dev.yml logs


# Production

run:
	docker compose up -d
build:
	docker compose up -d --build
logs:
	docker compose logs


# Utils

backup:
	@#!/bin/sh
	@compose_name=$$(basename "$$(pwd)")
	@volumes="$${compose_name}_media $${compose_name}_postgres_data"
	@date=$$(date '+%Y-%m-%d')
	@for volume in $${volumes}; do \
	    echo "### Backing up $${volume}"; \
	    volume_directory=$$(sudo docker inspect $${volume} | grep Mountpoint | awk '{ print $$2 }' | tr -d ',"'); \
	    tar cvf backup/$${volume}-$${date}.tar -C $${volume_directory} .; \
	done
