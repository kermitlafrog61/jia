run_dev:
	docker compose -f docker-compose.dev.yml up -d

build_dev:
	docker compose -f docker-compose.dev.yml up -d --build

run_prod:
	docker compose -f docker-compose.prod.yml up -d --build

create_superuser_dev:
	docker compose -f docker-compose.dev.yml exec backend ./manage.py createsuperuser

logs:
	docker compose -f docker-compose.prod.yml logs
