# Deployment Guide

This guide covers deploying the Henry Oak Reality Django application to production environments.

## Build Files Overview

The project includes multiple build files for different deployment scenarios:

### 1. `build.sh` (Main Build Script)
- **Used by:** Render.com (primary deployment)
- **Features:**
  - Installs Python dependencies
  - Builds Tailwind CSS for production
  - Collects static files
  - Runs database migrations
  - Creates superuser automatically

### 2. `vercel-build.sh` (Vercel Build Script)
- **Used by:** Vercel deployment
- **Features:**
  - Installs Python dependencies
  - Collects static files
  - Runs database migrations
  - Creates superuser automatically

### 3. `build.py` (Python Build Script)
- **Used by:** Python-based deployments
- **Features:**
  - Collects static files
  - Runs database migrations
  - Creates superuser automatically

### 4. `build_files.sh` (Simple Build Script)
- **Used by:** Basic deployments
- **Features:**
  - Installs Python dependencies
  - Collects static files
  - Runs database migrations
  - Creates superuser automatically

## Admin User Creation

### Automatic Superuser Creation

All build scripts now include automatic superuser creation using the `create_superuser` management command.

### Environment Variables

Set these environment variables in your production environment:

```bash
# Admin credentials (optional - defaults provided)
ADMIN_USERNAME=admin
ADMIN_EMAIL=raj.gupta@kw.com
ADMIN_PASSWORD=your_secure_password_here

# Required Django settings
SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=your_database_url_here
```

### Manual Superuser Creation

If you need to create a superuser manually:

```bash
# Using environment variables
python manage.py create_superuser --noinput

# Using custom credentials
python manage.py create_superuser --username admin --email admin@example.com --password secure_password

# Interactive mode
python manage.py create_superuser
```

## Deployment Platforms

### Render.com

1. **Configuration:** Uses `render.yaml`
2. **Build Command:** `./build.sh`
3. **Start Command:** `gunicorn mysite.wsgi:application`
4. **Environment Variables:** Set in Render dashboard or `render.yaml`

### Vercel

1. **Configuration:** Uses `vercel-build.sh`
2. **Build Command:** `./vercel-build.sh`
3. **Environment Variables:** Set in Vercel dashboard

### Other Platforms

Use the appropriate build script based on your platform's requirements.

## Database Setup

### Production Database

The application automatically:
1. Runs migrations during build
2. Creates necessary database tables
3. Sets up admin user

### Sample Data (Optional)

To populate with sample data after deployment:

```bash
# Create sample properties
python manage.py create_sample_properties

# Create sample blog posts
python manage.py create_sample_blog_posts

# Create sample open houses
python manage.py create_sample_open_houses
```

## Static Files

Static files are automatically collected during build using:
```bash
python manage.py collectstatic --noinput
```

## Security Considerations

1. **SECRET_KEY:** Must be unique and secret in production
2. **DEBUG:** Must be `False` in production
3. **ALLOWED_HOSTS:** Must include your production domain
4. **ADMIN_PASSWORD:** Use a strong password in production

## Monitoring

### Admin Access

After deployment, access the admin panel at:
- URL: `https://your-domain.com/admin/`
- Username: `admin` (or your custom ADMIN_USERNAME)
- Password: Your ADMIN_PASSWORD

### Link Tracking

Monitor link tracking data at:
- URL: `https://your-domain.com/admin/Henry/linktracking/`

### CRM Integration

The application automatically sends data to the Podio CRM webhook:
- URL: `https://workflow-automation.podio.com/catch/8g78a8102321zec`

## Troubleshooting

### Build Failures

1. Check environment variables are set correctly
2. Verify database connection
3. Check Python/Node.js versions

### Admin Access Issues

1. Verify ADMIN_* environment variables
2. Check if superuser was created successfully
3. Try manual superuser creation

### Static Files Issues

1. Ensure `collectstatic` runs during build
2. Check static files configuration
3. Verify file permissions

## Support

For deployment issues, check:
1. Build logs in your deployment platform
2. Django logs for application errors
3. Database connection status
4. Environment variable configuration
