#!/bin/bash

# Run Django tests with coverage
echo "Running Django tests..."

# Run tests with coverage
python manage.py test --verbosity=2 --parallel

# Run pytest if available
if command -v pytest &> /dev/null; then
    echo "Running pytest..."
    pytest --cov=. --cov-report=html --cov-report=term-missing
fi

echo "Tests completed!" 