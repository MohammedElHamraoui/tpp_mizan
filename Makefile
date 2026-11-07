# Define phony targets (targets that don't represent files)
.PHONY: help sync install test lint format run run-api build clean deep-clean context add add-dev rename

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
format: ## Format code using Ruff
	uv run ruff format .
	uv run ruff check --fix .

lint: ## Lint code using Ruff and Mypy
	uv run ruff check .
	uv run mypy .

# --- Testing ---
test: ## Run tests with pytest
	uv run pytest -v

test-cov: ## Run tests with coverage report
	uv run pytest --cov --cov-report=term-missing

# --- Execution ---
# Define default values that can be overridden from the command line
X ?= 10
Y ?= 2

run: ## Run the main CLI application (Usage: make run X=5 Y=2)
	uv run my-divide $(X) $(Y)

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

# --- CI/CD ---
ci-check: format lint test ## Run all CI checks locally

# --- LLM ---
context: ## Export project source to tpp_mizan.txt for LLM feedback
	@echo "Generating LLM context file..."
	@find . -type f \( -name "*.py" -o -name "*.toml" -o -name "*.md" -o -name "*.yaml" -o -name "Makefile" \) \
		-not -path "./.venv/*" -not -path "./logs/*" -not -path "./.git/*" \
		| sort | while read -r f; do \
			echo "========== $$f =========="; \
			cat "$$f"; \
			echo ""; \
		done > tpp_mizan.txt
	@echo "Done! Saved to tpp_mizan.txt ($$(wc -l < tpp_mizan.txt) lines, $$(du -h tpp_mizan.txt | cut -f1))"

rename: ## Rename the project (Usage: make rename NEW_NAME=tpp_mizan)
	@if [ -z "$(NEW_NAME)" ]; then \
		echo "Error: NEW_NAME is required. Usage: make rename NEW_NAME=tpp_mizan"; \
		exit 1; \
	fi
	@echo "Renaming project to '$(NEW_NAME)' (project: tpp-mizan)..."
	# 1. Update pyproject.toml project name (uses hyphens per PEP 621)
	@sed -i 's/name = "tpp-mizan"/name = "tpp-mizan"/' pyproject.toml
	# 2. Rename source and test directories (uses underscores for Python imports)
	@if [ -d "src/tpp_mizan" ]; then mv src/tpp_mizan src/$(NEW_NAME); fi
	@if [ -d "tests/tpp_mizan" ]; then mv tests/tpp_mizan tests/$(NEW_NAME); fi
	# 3. Replace all internal module references (tpp_mizan -> tpp_mizan)
	@find . -type f \( -name "*.py" -o -name "*.toml" -o -name "*.yaml" -o -name "Makefile" -o -name "*.md" \) \
		-not -path "./.venv/*" -not -path "./.git/*" -exec sed -i "s/tpp_mizan/$(NEW_NAME)/g" {} +
	# 4. Replace all internal project name references (tpp-mizan -> tpp-mizan)
	@find . -type f \( -name "*.py" -o -name "*.toml" -o -name "*.yaml" -o -name "Makefile" -o -name "*.md" \) \
		-not -path "./.venv/*" -not -path "./.git/*" -exec sed -i "s/tpp-mizan/tpp-mizan/g" {} +
	@echo "✅ Rename complete! Run 'make deep-clean && make install' to rebuild the environment."