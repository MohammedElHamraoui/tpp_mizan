# TPP Mizan

A production-ready Python template from Tech Print Pack featuring FastAPI REST API, Typer CLI, and structured JSON logging, managed by `uv`.

## ✨ Features
- ⚡ **Ultra-fast dependency management** with `uv`
- 🚀 **FastAPI** for high-performance, auto-documented REST APIs
- 💻 **Typer** for type-safe, intuitive CLI tools
- 📝 **Structured JSON Logging** with dynamic path resolution and log rotation
- ✅ **Bulletproof CI/CD** via GitHub Actions running `make ci-check` (Ruff, Mypy, Pytest)

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   make install
   ```

2. **Run the CLI** (supports `add`, `subtract`, `multiply`, `divide`):
   ```bash
   make run-add X=10 Y=2        # → 12.0
   make run-subtract X=10 Y=2   # → 8.0
   make run-multiply X=10 Y=2   # → 20.0
   make run X=10 Y=2            # → 5.0 (divide is the default)
   ```

3. **Start the API**:
   ```bash
   make run-api
   # Visit http://127.0.0.1:8000/docs for the interactive Swagger UI
   # Endpoints: /add/{x}/{y}, /subtract/{x}/{y}, /multiply/{x}/{y}, /divide/{x}/{y}
   ```

4. **Run CI Checks**:
   ```bash
   make ci-check
   ```

## ⚙️ Environment Variables
You can configure the application by setting these variables in your shell or a `.env` file:

| Variable | Default | Description |
|---|---|---|
| `LOG_LEVEL` | `INFO` | Sets the logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`). |
| `TPP_MIZAN_LOG_DIR` | `./logs` | Overrides the directory where JSON and timed log files are written. |

## 🛠️ Development
- Add a dependency: `make add PKG=requests`
- Add a dev dependency: `make add-dev PKG=httpx2`
- Clean up: `make clean` (or `make deep-clean` for a total reset)
- Generate LLM context: `make context`
