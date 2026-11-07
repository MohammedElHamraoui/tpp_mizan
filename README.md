# My Project

A modern, production-ready Python template featuring FastAPI, Typer CLI, and structured JSON logging, managed by `uv`.

## ✨ Features
- ⚡ **Ultra-fast dependency management** with `uv`
- 🚀 **FastAPI** for high-performance, auto-documented REST APIs
- 💻 **Typer** for type-safe, intuitive CLI tools
- 📝 **Structured JSON Logging** with dynamic path resolution and log rotation
- ✅ **Bulletproof CI/CD** via `make ci-check` (Ruff, Mypy, Pytest)

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   make install
   ```

2. **Run the CLI**:
   ```bash
   make run X=10 Y=2
   # or directly: uv run my-divide 10 2
   ```

3. **Start the API**:
   ```bash
   make run-api
   # Visit http://127.0.0.1:8000/docs for the interactive Swagger UI
   ```

4. **Run CI Checks**:
   ```bash
   make ci-check
   ```

## 🛠️ Development
- Add a dependency: `make add PKG=requests`
- Add a dev dependency: `make add-dev PKG=httpx2`
- Clean up: `make clean` (or `make deep-clean` for a total reset)
