.PHONY: build-rust run test docker-up docker-build

build-rust:
	cd cognitive_core && maturin develop --release

run: build-rust
	cd conscious_surface && streamlit run app.py

test: build-rust
	pytest tests/

docker-build:
	docker compose build

docker-up:
	docker compose up
