.PHONY: help
SHELL := /bin/bash

PROJECT_NAME = purchase_system
UID=$(shell id -u)
GID=$(shell id -g)

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Clean temporary files
	@docker-compose run --rm app \
	find . -name "*.pyc" | xargs rm -rf \
	&& find . -name "*.pyo" | xargs rm -rf \
	&& find . -name "__pycache__" -type d | xargs rm -rf \
	&& find . -name ".cache" -type d | xargs rm -rf \
	&& find . -name ".coverage" -type f | xargs rm -rf \
	&& find . -name ".pytest_cache" -type d | xargs rm -rf \
	&& rm -rf htmlcov/ \
	&& rm -f coverage.xml \
	&& rm -f *.log \
	&& echo 'Temporary files deleted' 

test:  ## Run the test suite without integration tests
	@docker-compose run --rm app py.test purchase_system/ -s -vvv -p no:cacheprovider

test-matching: clean  ## Run only tests matching pattern. E.g.: make test-matching test=TestClassName
	@docker-compose run --rm app py.test purchase_system/ -k $(test) -s -vvv -p no:cacheprovider 

coverage: clean  ## Run the test coverage report
	@docker-compose run --rm app py.test --cov-config .coveragerc --cov $(PROJECT_NAME) $(PROJECT_NAME) 

lint: clean  ## Run pylint linter
	@printf '\n --- \n >>> Running linter...<<<\n'
	@docker-compose run --rm app pylint --rcfile=.pylintrc $(PROJECT_NAME)/* 
	@printf '\n FINISHED! \n --- \n'

bash: ## Run bash inside container
	@docker-compose run --rm app /bin/bash 

format:  ## Run isort and black auto formatting code style in the project
	@docker-compose run --rm app isort -m 3 --tc . 
	@docker-compose run --rm app black -S -t py37 -l 79 $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|venv|build|dist|\.pyenv)/' 

format-check:  ## Check isort and black code style
	@docker-compose run --rm app black -S -t py37 -l 79 --check $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|venv|build|dist|\.pyenv)/' 

build: ## Build container image
	@docker build -t purchasesystem_app:latest -f Dockerfile.dev . --build-arg UID=$(UID) --build-arg GID=$(GID)

run-dev: clean # Run app
	@docker-compose up --remove-orphans

run-dev-no-output: clean # Run app without outputs
	@docker-compose up -d --remove-orphans

stop: clean # Stop app
	@docker-compose stop

requirements-pip: clean ## Install the app requirements
	@docker-compose run --rm app pip install --upgrade pip 
	@docker-compose run --rm app pip install -r requirements/dev.txt 