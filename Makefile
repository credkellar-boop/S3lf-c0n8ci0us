.PHONY: build-rust run test docker-up docker-build clean

build-rust:
	@echo "Compiling Rust Core..."
	cd cognitive_core && maturin develop --release

run: build-rust
	@echo "Launching Reasoning Engine..."
	cd conscious_surface && streamlit run app.py

test: build-rust
	@echo "Running Audits and Logic Tests..."
	pytest tests/

docker-build:
	docker build -t s3lf-engine .

docker-up:
	docker compose up

clean:
	rm -rf cognitive_core/target/
	find . -type d -name "__pycache__" -exec rm -rf {} +
