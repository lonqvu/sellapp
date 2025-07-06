# SellApp - Django Backend

A Django-based e-commerce backend application with MariaDB database.

## 🚀 Features

- **Django 4.2.7** with REST API
- **MariaDB 10.11** database
- **Celery** for background tasks
- **Redis** for caching and message broker
- **Docker** support for easy deployment
- **Comprehensive testing** setup

## 📋 Prerequisites

- Python 3.8+
- MariaDB 10.11+
- Redis 7+
- Docker & Docker Compose (optional)

## 🛠️ Installation

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sellapp/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your database credentials
   ```

5. **Set up MariaDB**
   ```sql
   CREATE DATABASE sellapp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'sellapp_user'@'localhost' IDENTIFIED BY 'sellapp_password';
   GRANT ALL PRIVILEGES ON sellapp_db.* TO 'sellapp_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

### Option 2: Docker Development

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Run migrations**
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

3. **Create superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## 🗄️ Database Configuration

### MariaDB Settings

The application is configured to use MariaDB with the following settings:

- **Engine**: `django.db.backends.mysql`
- **Character Set**: `utf8mb4`
- **Collation**: `utf8mb4_unicode_ci`
- **Port**: `3306`

### Environment Variables

```env
# Database
DB_NAME=sellapp_db
DB_USER=sellapp_user
DB_PASSWORD=sellapp_password
DB_HOST=localhost
DB_PORT=3306
DATABASE_URL=mysql://sellapp_user:sellapp_password@localhost:3306/sellapp_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

## 🏗️ Project Structure

```
backend/
├── apps/
│   ├── core/           # Core models and utilities
│   └── sale/           # Sales and e-commerce models
├── myproject/
│   ├── settings/       # Environment-specific settings
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI application
├── static/             # Static files
├── media/              # User-uploaded files
├── templates/          # HTML templates
├── requirements.txt    # Production dependencies
├── requirements-dev.txt # Development dependencies
└── docker-compose.yml  # Docker services
```

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=apps

# Run specific app tests
pytest apps/sale/
```

## 🔧 Development Tools

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **pre-commit**: Git hooks

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Format code
black .
isort .

# Run linter
flake8
```

## 📦 Dependencies

### Core Dependencies
- **Django 4.2.7**: Web framework
- **MariaDB 1.1.9**: Database driver
- **mysqlclient 2.2.0**: MySQL/MariaDB connector
- **djangorestframework 3.14.0**: REST API framework
- **celery 5.3.4**: Background task processing
- **redis 5.0.1**: Caching and message broker

### Development Dependencies
- **pytest**: Testing framework
- **black**: Code formatter
- **isort**: Import sorter
- **flake8**: Linter
- **coverage**: Test coverage

## 🚀 Deployment

### Production Settings

1. **Use production settings**
   ```bash
   export DJANGO_SETTINGS_MODULE=myproject.settings.prod
   ```

2. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Use production database**
   - Configure MariaDB with proper security
   - Set up SSL connections
   - Configure backups

### Docker Production

```bash
# Build production image
docker build -t sellapp-backend .

# Run with production settings
docker run -e DJANGO_SETTINGS_MODULE=myproject.settings.prod sellapp-backend
```

## 🔍 API Documentation

The API documentation is available at:
- **Development**: http://localhost:8000/api/
- **Admin Interface**: http://localhost:8000/admin/

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📞 Support

For support and questions, please contact the development team. 