# SellApp Django Backend - Cấu trúc Project

## 📁 Tổng quan cấu trúc

```
backend/
├── 📄 manage.py                    # Django management script
├── 📄 requirements.txt             # Production dependencies
├── 📄 requirements-dev.txt         # Development dependencies
├── 📄 env.example                  # Environment variables template
├── 📄 README.md                    # Hướng dẫn chi tiết
├── 📄 STRUCTURE.md                 # File này - tóm tắt cấu trúc
├── 📄 Makefile                     # Development commands
├── 📄 Dockerfile                   # Production Docker image
├── 📄 docker-compose.yml           # Development Docker setup
├── 📄 docker-compose.prod.yml      # Production Docker setup
├── 📄 nginx.conf                   # Nginx configuration
├── 📄 .pre-commit-config.yaml      # Pre-commit hooks
├── 📄 pytest.ini                   # Pytest configuration
├── 📄 .flake8                      # Flake8 configuration
├── 📄 .gitignore                   # Git ignore rules
│
├── 📁 myproject/                   # Main Django project
│   ├── 📄 __init__.py
│   ├── 📄 settings.py              # Settings entry point
│   ├── 📄 urls.py                  # Main URL configuration
│   ├── 📄 wsgi.py                  # WSGI application
│   ├── 📄 asgi.py                  # ASGI application
│   ├── 📄 celery.py                # Celery configuration
│   └── 📁 settings/                # Settings by environment
│       ├── 📄 __init__.py
│       ├── 📄 base.py              # Base settings
│       ├── 📄 dev.py               # Development settings
│       └── 📄 prod.py              # Production settings
│
├── 📁 apps/                        # Django applications
│   ├── 📄 __init__.py
│   ├── 📁 core/                    # Core application
│   │   ├── 📄 __init__.py
│   │   ├── 📄 apps.py
│   │   ├── 📄 models.py            # Core models (User, Configuration)
│   │   ├── 📄 views.py             # Core views (health check, API info)
│   │   ├── 📄 urls.py              # Core URL patterns
│   │   ├── 📄 admin.py             # Admin interface
│   │   ├── 📄 tasks.py             # Celery tasks
│   │   └── 📁 migrations/
│   │       └── 📄 __init__.py
│   └── 📁 sale/                    # Sale application
│       ├── 📄 __init__.py
│       ├── 📄 apps.py
│       ├── 📄 models.py            # Sale models (Category, Product, Order, OrderItem)
│       ├── 📄 views.py             # Sale API views
│       ├── 📄 serializers.py       # DRF serializers
│       ├── 📄 urls.py              # Sale URL patterns
│       ├── 📄 admin.py             # Admin interface
│       ├── 📄 tasks.py             # Celery tasks
│       ├── 📄 signals.py           # Django signals
│       └── 📁 migrations/
│           └── 📄 __init__.py
│
├── 📁 static/                      # Static files
│   └── 📄 .gitkeep
├── 📁 media/                       # User uploaded files
│   └── 📄 .gitkeep
├── 📁 templates/                   # Django templates
│   └── 📄 .gitkeep
├── 📁 logs/                        # Application logs
│   └── 📄 .gitkeep
├── 📁 backups/                     # Database backups
└── 📁 scripts/                     # Utility scripts
    ├── 📄 .gitkeep
    ├── 📄 setup.sh                 # Initial setup script
    ├── 📄 deploy.sh                # Production deployment
    ├── 📄 backup.sh                # Database backup
    └── 📄 run_tests.sh             # Test runner
```

## 🏗️ Kiến trúc hệ thống

### 1. **Settings Management**
- **base.py**: Cấu hình chung cho tất cả môi trường
- **dev.py**: Cấu hình development (DEBUG=True, SQLite, console email)
- **prod.py**: Cấu hình production (DEBUG=False, PostgreSQL, SMTP email)

### 2. **Applications**
- **core**: Chức năng cơ bản (health check, user management, system config)
- **sale**: Quản lý bán hàng (categories, products, orders)

### 3. **API Structure**
```
/api/
├── /health/           # Health check endpoint
├── /info/            # API information
└── /sale/
    ├── /categories/   # Category CRUD
    ├── /products/     # Product CRUD
    ├── /orders/       # Order CRUD
    └── /order-items/  # OrderItem CRUD
```

### 4. **Database Models**

#### Core Models
- **User**: Custom user model
- **Configuration**: System configuration key-value pairs
- **TimeStampedModel**: Abstract base model with timestamps

#### Sale Models
- **Category**: Product categories
- **Product**: Products with stock management
- **Order**: Customer orders with status tracking
- **OrderItem**: Order line items with automatic subtotal calculation

### 5. **Background Tasks (Celery)**
- **Email notifications**: Order confirmations, status updates
- **Stock management**: Low stock alerts
- **Reports**: Daily sales reports
- **Maintenance**: Log cleanup, health checks

### 6. **Security Features**
- Environment variables for sensitive data
- HTTPS redirect in production
- HSTS headers
- XSS protection
- CSRF protection
- Rate limiting (nginx)
- Secure content type headers

## 🚀 Deployment Options

### Development
```bash
# Local development
make install-dev
make migrate
make runserver

# Docker development
docker-compose up
```

### Production
```bash
# Docker production
docker-compose -f docker-compose.prod.yml up -d

# Manual deployment
./scripts/deploy.sh
```

## 🔧 Development Tools

### Code Quality
- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **pre-commit**: Git hooks
- **pytest**: Testing framework

### Database
- **Development**: SQLite
- **Production**: PostgreSQL
- **Migrations**: Automatic migration management

### Monitoring
- **Health checks**: `/api/health/`
- **Logging**: Structured logging with rotation
- **Backup**: Automated database backups

## 📊 Features

### ✅ Đã hoàn thành
- [x] Cấu trúc Django chuẩn với settings tách biệt
- [x] Quản lý môi trường với django-environ
- [x] API REST với Django REST Framework
- [x] Models cho hệ thống bán hàng
- [x] Admin interface đầy đủ
- [x] Background tasks với Celery
- [x] Email notifications
- [x] Database migrations
- [x] Code quality tools
- [x] Testing setup
- [x] Docker configuration
- [x] Production deployment
- [x] Security configurations
- [x] Logging system
- [x] Backup scripts

### 🔄 Có thể mở rộng
- [ ] Authentication system (JWT, OAuth)
- [ ] Payment integration
- [ ] Inventory management
- [ ] Customer management
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] API documentation (Swagger)
- [ ] Caching (Redis)
- [ ] Search functionality (Elasticsearch)
- [ ] File upload optimization
- [ ] WebSocket support
- [ ] Mobile API endpoints

## 🎯 Next Steps

1. **Setup môi trường**: Chạy `./scripts/setup.sh`
2. **Cấu hình database**: Chỉnh sửa `.env` file
3. **Tạo superuser**: `make createsuperuser`
4. **Chạy development server**: `make runserver`
5. **Viết tests**: Tạo test cases cho models và views
6. **Deploy production**: Sử dụng Docker hoặc manual deployment

## 📞 Support

Xem file `README.md` để biết thêm chi tiết về cách sử dụng và troubleshooting. 