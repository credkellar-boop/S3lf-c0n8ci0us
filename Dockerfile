# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies and Rust toolchain
RUN apt-get update && apt-get install -y curl build-essential \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

# Copy the entire project
COPY . .

# Install Python dependencies and Maturin for Rust compilation
RUN pip install --no-cache-dir -r conscious_surface/requirements.txt maturin pytest

# Compile the Rust PyO3 module
WORKDIR /app/cognitive_core
RUN maturin develop --release

# Set up the frontend entry point
WORKDIR /app/conscious_surface
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
