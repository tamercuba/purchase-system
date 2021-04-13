.PHONY: help

PROJECT_NAME = purchase_system

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:
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

test: clean  ## Run the test suite without integration tests
	py.test $(PROJECT_NAME) -s -vvv

test-ci: clean	## Run the test suite in CI
	py.test $(PROJECT_NAME) -s -vvv -m "not not_run_ci"

test-matching: clean  ## Run only tests matching pattern. E.g.: make test-matching test=TestClassName
	py.test $(PROJECT_NAME)/ -k $(test) -s -vvv

coverage: clean  ## Run the test coverage report
	@mkdir -p logs
	py.test --cov-config .coveragerc --cov $(PROJECT_NAME) $(PROJECT_NAME) --cov-report term-missing

lint: clean  ## Run pylint linter
	@printf '\n --- \n >>> Running linter...<<<\n'
	@pylint --rcfile=.pylintrc $(PROJECT_NAME)/*
	@printf '\n FINISHED! \n --- \n'

style:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 --tc .
	@black -S -t py37 -l 79 $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'

style-check:  ## Check isort and black code style
	@black -S -t py37 -l 79 --check $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'

run-dev: clean  # Run app
	@docker-compose up

run-dev-no-output: clean # Run app without outputs
	@docker-compose up -d

stop: clean # Stop app
	@docker-compose stop

