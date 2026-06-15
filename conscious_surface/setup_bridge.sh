#!/bin/bash
echo "📦 Initializing S3lf-c0n8ci0us PyO3 Native Bridge Build..."

# Ensure maturin (Rust/Python build coordinator) is installed
pip install maturin

# Move into the native rust crate directory
cd ../cognitive_core

# Compile Rust package into an active development package inside your python workspace
maturin develop --release

echo "🚀 Rust extensions compiled. 'cognitive_core' is now natively importable in Python!"
