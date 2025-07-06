#!/bin/bash

# Production deployment script for SellApp Django Backend
echo "🚀 Deploying SellApp Django Backend to production..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create it from env.example"
    exit 1
fi

# Load environment variables
source .env

# Check if DEBUG is set to False
if [ "$DEBUG" = "True" ]; then
    echo "⚠️  Warning: DEBUG is set to True. This is not recommended for production."
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Install production dependencies
echo "📦 Installing production dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Check for any pending migrations
if python manage.py showmigrations | grep -q "\[ \]"; then
    echo "⚠️  Warning: There are pending migrations. Please review them."
    python manage.py showmigrations
fi

# Restart services (if using systemd)
if command -v systemctl &> /dev/null; then
    echo "🔄 Restarting services..."
    sudo systemctl restart sellapp-backend
    sudo systemctl restart sellapp-celery
    sudo systemctl restart sellapp-celerybeat
fi

# Health check
echo "🏥 Performing health check..."
sleep 5
if curl -f http://localhost:8000/api/health/ > /dev/null 2>&1; then
    echo "✅ Deployment successful! Application is healthy."
else
    echo "❌ Health check failed. Please check the logs."
    exit 1
fi

echo "🎉 Deployment completed successfully!" 