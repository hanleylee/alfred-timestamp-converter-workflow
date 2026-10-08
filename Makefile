SHELL:=/usr/bin/env bash
BINARY_NAME:=alfred-timestamp-converter

.PHONY: all build build-multi-arch run clean pack install update

all: build

build:
	cargo build --release

build-multi-arch:
	cargo build --release --target aarch64-apple-darwin
	cargo build --release --target x86_64-apple-darwin
	lipo -create -output "target/release/$(BINARY_NAME)" \
		"target/aarch64-apple-darwin/release/$(BINARY_NAME)" \
		"target/x86_64-apple-darwin/release/$(BINARY_NAME)"

run:
	cargo run -- ts

clean:
	cargo clean
