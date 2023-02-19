SHELL:=/usr/bin/env bash
a:
	@echo "a is $$0"
b:
	@echo "b is $$0"
install:
	shopt -s globstar
	poetry install
	poetry export -f requirements.txt --without-hashes > requirements.txt
	pip install -r requirements.txt --target ./src/libs
update:
	shopt -s globstar
	poetry update
	poetry export -f requirements.txt --without-hashes > requirements.txt
	pip install -r requirements.txt --target ./src/libs --upgrade
