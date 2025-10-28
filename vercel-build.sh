#!/bin/bash
# Vercel build script for Django

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py create_superuser --noinput

echo "Build completed successfully!"
