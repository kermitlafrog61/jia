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
