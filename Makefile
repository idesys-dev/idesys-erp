DOCKER_COMPOSE = docker-compose

.env:
ifeq (,$(wildcard ./.env))
	cp .env.dist .env
endif

##
## Project
## -------
##
start: .env  ## Start the development server
	$(DOCKER_COMPOSE) up

start-d: .env  ## Start the development server (silent)
	$(DOCKER_COMPOSE) up -d

restart: .env  ## Restart the development server (silent)
	$(DOCKER_COMPOSE) restart

stop: ## Stop the project
	$(DOCKER_COMPOSE) down

lint: ## Linter
	$(DOCKER_COMPOSE) exec -T server python3 -m prospector --profile /code/.prospector.yaml || true

test: ## Launch Test
	$(DOCKER_COMPOSE) exec -T server pytest -v --cov=. --cov-report=html


generate-secret: ## Generate secret token
	$(DOCKER_COMPOSE) exec server python secret.py



##
## Assets
## -----
##

install-assets: ## Install dependencies npm assets
	$(DOCKER_COMPOSE) exec -T server sh -c "cd templates/assets && npm install"

build-assets: install-assets  ## Build assets
	$(DOCKER_COMPOSE) exec -T server sh -c "cd templates/assets && npm run build"

watch-assets: install-assets ## Build & watch assets
	$(DOCKER_COMPOSE) exec -T server sh -c "cd templates/assets && npm run watch"



##
## Utils
## -----
##

kill: ## Kill the project
	$(DOCKER_COMPOSE) kill

build: ## Build the project
	$(DOCKER_COMPOSE) build

console: ## Open a console
	$(DOCKER_COMPOSE) exec server sh



.PHONY: start
.DEFAULT_GOAL := help
help:
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
.PHONY: help
