# Define phony targets (targets that don't represent files)
.PHONY: help sync install add add-dev remove lock format format-check lint \
        test test-cov run run-add run-subtract run-multiply run-api build \
        clean deep-clean context ci-check rename

# Default target
help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# --- Dependency Management ---
sync: ## Create venv, resolve lockfile, and install project
	uv sync

install: sync ## Ensure project is installed (runs sync)
	@echo "Project synced and installed successfully."

add: ## Add a new dependency (Usage: make add PKG=requests)
	uv add $(PKG)

add-dev: ## Add a dev dependency (Usage: make add-dev PKG=httpx2)
	uv add --dev $(PKG)

remove: ## Remove a dependency (Usage: make remove PKG=requests)
	uv remove $(PKG)

lock: ## Update the lockfile without installing to the venv
	uv lock

# --- Code Quality ---
format: ## Format code locally (mutates files)
	uv run ruff format .
	uv run ruff check --fix .

format-check: ## Check formatting without mutating (for CI)
	uv run ruff format --check .
	uv run ruff check .

lint: ## Lint code using Mypy
	uv run mypy .

# --- CI/CD ---
ci-check: format-check lint test ## Run all CI checks locally (non-mutating)

# --- Testing ---
test: ## Run tests with pytest
	uv run pytest -v

test-cov: ## Run tests with coverage report
	uv run pytest --cov --cov-report=term-missing

# --- Execution ---
# Define default values that can be overridden from the command line
X ?= 10
Y ?= 2

run: ## Run the default CLI command (divide). Usage: make run X=5 Y=2
	uv run tpp-mizan divide $(X) $(Y)

run-add: ## Run addition. Usage: make run-add X=5 Y=2
	uv run tpp-mizan add $(X) $(Y)

run-subtract: ## Run subtraction. Usage: make run-subtract X=5 Y=2
	uv run tpp-mizan subtract $(X) $(Y)

run-multiply: ## Run multiplication. Usage: make run-multiply X=5 Y=2
	uv run tpp-mizan multiply $(X) $(Y)

run-api: ## Run the FastAPI application with hot-reloading
	uv run uvicorn tpp_mizan.app:app --reload --host 127.0.0.1 --port 8000

# --- Maintenance ---
clean: ## Clean up caches and virtual environments
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache .coverage dist build
	find . -type d -name "__pycache__" -exec rm -rf {} +
	uv cache clean

deep-clean: clean ## Nuclear clean: removes logs, context file, and lockfile
	rm -rf logs/
	rm -f tpp_mizan.txt
	rm -f uv.lock
	@echo "Deep clean complete. (Next 'make install' will re-resolve dependencies)"

# --- Packaging ---
build: ## Build wheel + sdist
	uv build
	
# --- LLM ---
context: ## Export project source to tpp_mizan.txt for LLM feedback
	@echo "Generating LLM context file..."
	@find . -type f \( -name "*.py" -o -name "*.toml" -o -name "*.md" -o -name "*.yaml" -o -name "Makefile" \) \
		-not -path "./.venv/*" -not -path "./.git/*" -not -path "./logs/*" \
		-not -path "./.pytest_cache/*" -not -path "./.mypy_cache/*" -not -path "./.ruff_cache/*" \
		-not -path "./dist/*" -not -path "./build/*" -not -path "./htmlcov/*" \
		-not -name "tpp_mizan.txt" \
		| sort | while read -r f; do \
			echo "========== $$f =========="; \
			cat "$$f"; \
			echo ""; \
		done > tpp_mizan.txt
	@echo "Done! Saved to tpp_mizan.txt ($$(wc -l < tpp_mizan.txt) lines, $$(du -h tpp_mizan.txt | cut -f1))"

rename: ## Rename project (Usage: make rename NEW_NAME=my_app NEW_PROJECT=my-app)
	@if [ -z "$(NEW_NAME)" ] || [ -z "$(NEW_PROJECT)" ]; then \
		echo "Usage: make rename NEW_NAME=my_app NEW_PROJECT=my-app"; exit 1; fi
	@uv run python - "$(NEW_NAME)" "$(NEW_PROJECT)" <<'PY'
	import pathlib, re, sys
	pkg, prj = sys.argv[1], sys.argv[2]
	assert re.fullmatch(r"[a-z_][a-z0-9_]*", pkg), "NEW_NAME must be a valid Python identifier"
	for old, new in [("src/tpp_mizan", f"src/{pkg}"), ("tests/tpp_mizan", f"tests/{pkg}")]:
	    if pathlib.Path(old).exists():
	        pathlib.Path(old).rename(new)
	for ext in ("*.py", "*.toml", "*.yaml", "*.md", "Makefile", "*.yml"):
	    for p in pathlib.Path(".").rglob(ext):
	        if any(x in p.parts for x in (".venv", ".git", "logs", ".pytest_cache", ".mypy_cache", ".ruff_cache")):
	            continue
	        p.write_text(p.read_text().replace("tpp_mizan", pkg).replace("tpp-mizan", prj))
	PY
	@echo "✅ Rename complete! Run 'make deep-clean && make install' to rebuild."