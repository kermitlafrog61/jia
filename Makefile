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


# Certification

check_docker:
	@#!/bin/bash
	@if ! [ -x "$$(command -v docker compose)" ]; then \
	  echo 'Error: docker compose is not installed.' >&2; \
	  exit 1; \
	fi


tls_params:
	@#!/bin/bash
	@data_path="./docker/nginx/certbot"
	@if [ ! -e "$$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$$data_path/conf/ssl-dhparams.pem" ]; then \
	  echo "### Downloading recommended TLS parameters ..."; \
	  mkdir -p "$$data_path/conf"; \
	  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$$data_path/conf/options-ssl-nginx.conf"; \
	  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "$$data_path/conf/ssl-dhparams.pem"; \
	  echo; \
	fi

create_dummy_cert:
	@#!/bin/bash
	@domains=(jia.kg www.jia.kg)
	@data_path="./docker/nginx/certbot"
	@path="/etc/letsencrypt/live/$${domains[0]}"
	@mkdir -p "$$data_path/conf/live/$${domains[0]}"
	@docker compose run --rm --entrypoint "\
	  openssl req -x509 -nodes -newkey rsa:1024 -days 1 \
	    -keyout '$$path/privkey.pem' \
	    -out '$$path/fullchain.pem' \
	    -subj '/CN=localhost'" certbot
	@echo

start_nginx:
	@docker compose up --force-recreate -d nginx
	@echo

delete_dummy_cert:
	@#!/bin/bash
	@domains=(jia.kg www.jia.kg)
	@docker compose run --rm --entrypoint "\
	  rm -Rf /etc/letsencrypt/live/$${domains[0]} && \
	  rm -Rf /etc/letsencrypt/archive/$${domains[0]} && \
	  rm -Rf /etc/letsencrypt/renewal/$${domains[0]}.conf" certbot
	@echo

request_cert:
	@#!/bin/bash
	@domains=(jia.kg www.jia.kg)
	@rsa_key_size=4096
	@data_path="./docker/nginx/certbot"
	@email="association.jia.business@gmail.com"
	@staging=0
	# Join $domains to -d args
	@domain_args=""
	@for domain in "$${domains[@]}"; do \
	  domain_args="$$domain_args -d $$domain"; \
	done
	# Select appropriate email arg
	@case "$$email" in \
	  "") email_arg="--register-unsafely-without-email" ;; \
	  *) email_arg="--email $$email" ;; \
	esac
	# Enable staging mode if needed
	@if [ $$staging != "0" ]; then staging_arg="--staging"; fi
	@docker compose run --rm --entrypoint "\
	  certbot certonly --webroot -w /var/www/certbot \
	    $$staging_arg \
	    $$email_arg \
	    $$domain_args \
	    --rsa-key-size $$rsa_key_size \
	    --agree-tos \
	    --force-renewal" certbot
	@echo

reload_nginx:
	@docker compose exec nginx nginx -s reload

certbot_setup: check_docker tls_params create_dummy_cert start_nginx delete_dummy_cert request_cert reload_nginx
