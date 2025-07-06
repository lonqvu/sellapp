.PHONY: help install install-dev migrate makemigrations runserver test test-coverage shell collectstatic clean docker-build docker-up docker-down

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt

migrate: ## Run database migrations
	python manage.py migrate

makemigrations: ## Create database migrations
	python manage.py makemigrations

runserver: ## Start development server
	python manage.py runserver

test: ## Run tests
	pytest

test-coverage: ## Run tests with coverage
	pytest --cov=apps --cov-report=html

shell: ## Open Django shell
	python manage.py shell

collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

clean: ## Clean Python cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

docker-build: ## Build Docker image
	docker-compose build

docker-up: ## Start Docker services
	docker-compose up -d

docker-down: ## Stop Docker services
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

docker-shell: ## Open shell in Django container
	docker-compose exec web python manage.py shell

docker-migrate: ## Run migrations in Docker
	docker-compose exec web python manage.py migrate

docker-makemigrations: ## Create migrations in Docker
	docker-compose exec web python manage.py makemigrations

docker-createsuperuser: ## Create superuser in Docker
	docker-compose exec web python manage.py createsuperuser

format: ## Format code with black and isort
	black .
	isort .

lint: ## Run linter
	flake8

check: ## Run all checks (format, lint, test)
	black --check .
	isort --check-only .
	flake8
	pytest

setup-db: ## Setup MariaDB database (requires MariaDB to be running)
	@echo "Setting up MariaDB database..."
	@echo "Please run the following SQL commands in your MariaDB client:"
	@echo "CREATE DATABASE sellapp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
	@echo "CREATE USER 'sellapp_user'@'localhost' IDENTIFIED BY 'sellapp_password';"
	@echo "GRANT ALL PRIVILEGES ON sellapp_db.* TO 'sellapp_user'@'localhost';"
	@echo "FLUSH PRIVILEGES;"

setup-dev: ## Complete development setup
	@echo "Setting up development environment..."
	pip install -r requirements-dev.txt
	cp env.example .env
	@echo "Please edit .env file with your database credentials"
	@echo "Then run: make setup-db"
	@echo "Finally run: make migrate"

reset-db: ## Reset database (WARNING: This will delete all data)
	@echo "WARNING: This will delete all data in the database!"
	@read -p "Are you sure? [y/N] " -n 1 -r; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		python manage.py flush --noinput; \
		echo "Database reset complete"; \
	else \
		echo "Database reset cancelled"; \
	fi

backup-db: ## Backup database
	python manage.py dumpdata > backup_$(shell date +%Y%m%d_%H%M%S).json

restore-db: ## Restore database from backup
	@echo "Available backups:"
	@ls -la backup_*.json 2>/dev/null || echo "No backups found"
	@read -p "Enter backup filename: " backup_file; \
	python manage.py loaddata $$backup_file 