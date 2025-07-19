.PHONY: help install test format lint clean run dev

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install pytest pytest-flask black flake8 isort

test: ## Run tests
	pytest

format: ## Format code with black and isort
	black src/ tests/
	isort src/ tests/

lint: ## Lint code with flake8
	flake8 src/ tests/

clean: ## Clean up cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

run: ## Run the application
	python app.py

dev: ## Run in development mode
	FLASK_ENV=development FLASK_DEBUG=1 python app.py

init-db: ## Initialize database
	flask init-db

populate-db: ## Populate database with sample data
	flask populate-db

migrate: ## Run database migrations
	flask db upgrade 