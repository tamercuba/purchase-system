export PYTHONPATH=$(shell pwd)/sales_register/
export PYTHONDONTWRITEBYTECODE=1

.PHONY: help
SHELL := /bin/bash

PROJECT_NAME = sales_register
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


# Tests
test: clean ## Run the tests
	@py.test $(PROJECT_NAME)/ -s -vvv -p no:cacheprovider

test-matching: clean  ## Run only tests matching pattern. E.g.: make test-matching test=TestClassName
	@py.test -s -k $(k) -vvv -p no:cacheprovider

coverage: clean  ## Run the test coverage report
	@py.test --cov-config .coveragerc --cov $(PROJECT_NAME) $(PROJECT_NAME)


# Linting
_flake8:
	@flake8 --show-source .

_isort:
	@isort --diff --check-only --profile black .

_black:
	@black --check sales_register/

_isort-fix:
	@isort . --profile black

_black_fix:
	@black .

_dead_fixtures:
	@pytest --dead-fixtures sales_register/tests

_mypy:
	@mypy sales_register/

lint: _flake8 _isort _black _mypy _dead_fixtures   ## Check code lint

format-code: _black_fix _isort-fix  ## Format code


format-check:  ## Check isort and black code style
	@black --check --config ./pyproject.toml $(PROJECT_NAME)/.


# DB
db-up: clean # Run db container
	@docker compose up postgres -d

db-down: clean # Kill db container
	@docker compose down postgres

create-migration: clean ## Create alembic migration
	@alembic revision -m $(comment)

run-migrations: clean ## Run alembic migrations
	@alembic upgrade head

downgrade-migration: clean ## Downgrade alembic migrations
	@alembic downgrade ${target}

# Docker
bash: ## Run bash inside container
	@docker compose run --rm app /bin/bash

build: ## Build container image
	@docker build -t salesregister_app:latest -f Dockerfile.dev . --build-arg UID=$(UID) --build-arg GID=$(GID)

run-dev-without-docker: clean ## Run app outside a container
	@cd ${PROJECT_NAME} && python -m uvicorn adapters.api:app --reload --port ${APP_PORT}

run-dev: clean # Run app
	@docker compose up --remove-orphans


run-dev-no-output: clean # Run app without outputs
	@docker compose up -d --remove-orphans

stop: clean # Stop app
	@docker compose stop


# Local
requirements-pip: clean ## Install the app requirements
	@pip install --upgrade pip && pip install -r requirements/dev.txt

make-env: ## Creates a .env file
	@cp ./contrib/localenv .env

generate-secret: ## Generate password secret
	@openssl rand -hex 32
