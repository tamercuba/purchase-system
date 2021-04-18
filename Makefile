.PHONY: help
SHELL := /bin/bash

PROJECT_NAME = purchase_system
API_NAME = api
UID=$(shell id -u)
GID=$(shell id -g)

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Clean temporary files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@echo 'Temporary files deleted'

test: clean ## Run the tests
	@py.test tests/ -s -vvv -p no:cacheprovider

test-matching: clean  ## Run only tests matching pattern. E.g.: make test-matching test=TestClassName
	@py.test tests/ -k $(test) -s -vvv -p no:cacheprovider 

coverage: clean  ## Run the test coverage report
	@py.test --cov-config .coveragerc --cov $(PROJECT_NAME) tests

lint: clean  ## Run pylint linter
	@printf '\n --- \n >>> Running linter...<<<\n'
	@pylint --rcfile=.pylintrc $(API_NAME)/. $(PROJECT_NAME)/. tests/.
	@printf '\n FINISHED! \n --- \n'

bash: ## Run bash inside container
	@docker-compose run --rm app /bin/bash 

format:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 --tc . && black --config ./pyproject.toml .

format-check:  ## Check isort and black code style
	@black --check --config ./pyproject.toml $(PROJECT_NAME)/.
	@black --check --config ./pyproject.toml $(API_NAME)/.

build: ## Build container image
	@docker build -t purchasesystem_app:latest -f Dockerfile.dev . --build-arg UID=$(UID) --build-arg GID=$(GID)

run-dev-without-docker: clean ## Run app outside a container
	python -m uvicorn api.main:app --reload --port ${APP_PORT}

run-dev: clean # Run app
	@docker-compose up --remove-orphans

run-dev-no-output: clean # Run app without outputs
	@docker-compose up -d --remove-orphans

stop: clean # Stop app
	@docker-compose stop

requirements-pip: clean ## Install the app requirements
	@pip install --upgrade pip && pip install -r requirements/dev.txt

make-env: ## Creates a .env file
	@cp ./contrib/localenv .env

generate-secret: ## Generate password secret
	openssl rand -hex 32