#!/usr/bin/env make

DEBUG             ?= false
TEST_ENVIRONMENT  ?= testing
TEST_RELEASE_NAME ?= test-release

-include Makefile.mk

.PHONY: dev
dev: lint types test/unit
