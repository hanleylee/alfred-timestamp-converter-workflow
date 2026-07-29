SHELL:=/usr/bin/env bash
BINARY_NAME:=alfred-timestamp-converter

.PHONY: all build build-multi-arch run clean pack install update

all: build

build:
	cargo build --release
	@mkdir -p bin
	@cp "target/release/$(BINARY_NAME)" "bin/$(BINARY_NAME)"

build-multi-arch:
	cargo build --release --target aarch64-apple-darwin
	cargo build --release --target x86_64-apple-darwin
	@mkdir -p bin
	lipo -create -output "bin/$(BINARY_NAME)" \
		"target/aarch64-apple-darwin/release/$(BINARY_NAME)" \
		"target/x86_64-apple-darwin/release/$(BINARY_NAME)"

run:
	cargo run -- ts

clean:
	@/bin/rm -rf target bin/$(BINARY_NAME)

# Legacy: vendor Python deps (kept for the previous Python implementation)
pack install:
	shopt -s globstar
	cd py && poetry install
	cd py && poetry export -f requirements.txt --without-hashes > requirements.txt
	pip install -r py/requirements.txt --target ./py/libs

update:
	shopt -s globstar
	cd py && poetry update
	cd py && poetry export -f requirements.txt --without-hashes > requirements.txt
	pip install -r py/requirements.txt --target ./py/libs --upgrade
