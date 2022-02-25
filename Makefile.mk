#!/usr/bin/env make

.DEFAULT_GOAL     := help
.DEFAULT_SHELL    := /bin/bash

PACKAGE_NAME      := httpd-logs
SOURCE_DIRECTORY  := httpd_logs
TESTS_DIRECTORY   ?= tests
FLAKE8_OPTS       ?=
PYTEST_OPTS       ?= -vv


define assert-set
	@$(if $($1),,$(error $(1) environment variable is not defined))
endef

define assert-command
	@$(if $(shell command -v $1 2>/dev/null),,$(error $(1) command not found))
endef

define assert-file
	@$(if $(wildcard $($1) 2>/dev/null),,$(error $($1) does not exist))
endef

.PHONY: all
all: help

.PHONY: help
help: ## Shows this pretty help screen
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <target>\n\nTargets:\n"} /^[a-z0-9//_-]+:.*?##/ { printf " %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: setup
setup:
	@pip install --quiet poetry
	@poetry config virtualenvs.in-project true
	@poetry install --quiet

.PHONY: clean
clean:
	@rm -fr dist/{*.tar.gz,*.whl} .pytest_cache $(SOURCE_DIRECTORY)/__pycache__ $(TESTS_DIRECTORY)/__pycache__

.PHONY: lint
lint: ## Python code linting
	@poetry run flake8 $(FLAKE8_OPTS) $(SOURCE_DIRECTORY) $(TESTS_DIRECTORY)

.PHONY: types
types: ## Check for the types
	@poetry run mypy $(SOURCE_DIRECTORY) $(TESTS_DIRECTORY)

.PHONY: fmt
fmt: ## Python code check
	@poetry run black --diff --color $(SOURCE_DIRECTORY) tests

.PHONY: test
test: ## Python tests suite coverage
	@poetry run pytest -v
