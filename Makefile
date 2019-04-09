DOCKER ?= docker
DOCKER_COMPOSE ?= docker-compose

all: build
# Docker related commands
up: 
	$(DOCKER_COMPOSE) up -d --build

down:
	$(DOCKER_COMPOSE) down

stop:
	$(DOCKER_COMPOSE) stop	

migrate:
	$(DOCKER_COMPOSE) exec app python manage.py migrate

seed:
	$(DOCKER_COMPOSE) exec app python manage.py seed_data

build: up migrate seed

start:
	$(DOCKER_COMPOSE) up -d
