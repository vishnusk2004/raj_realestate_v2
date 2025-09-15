#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Building Tailwind CSS for production..."
cd theme/static_src

# Check if node_modules exists, if not install dependencies
if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies..."
    npm install
else
    echo "Node.js dependencies already installed, updating..."
    npm install
fi

# Update browserslist database to avoid warnings
echo "Updating browserslist database..."
npx update-browserslist-db@latest --yes

# Build Tailwind CSS
echo "Building CSS..."
npm run build

cd ../..

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py create_superuser --noinput

echo "Build completed successfully!"
