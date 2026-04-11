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

The application automatically sends data to the Podio CRM webhooks:
- **Form Submissions**: `https://workflow-automation.podio.com/catch/8g78a8102321zec`
- **Link Tracking**: `https://workflow-automation.podio.com/catch/sajz0io9683p7b0`

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

## Direct S3 Uploads (Lambda-safe)

Use this pattern when running Django on serverless infrastructure.

### What was added

1. Staff-only presigned upload endpoint: `/api/uploads/presign/`
2. Route mapping in `Raj/urls.py`
3. Upload size and location settings in `mysite/settings.py`

### Security model

1. AWS credentials are never sent to the browser.
2. Presigned policies expire in 5 minutes.
3. Only authenticated staff users can request presigned uploads.
4. MIME type, extension, and max file size are validated server-side.
5. Object keys are randomized and written under `media/uploads/...`.

### Required environment variables

```bash
S3_MEDIA_LOCATION=media
S3_MAX_IMAGE_UPLOAD_BYTES=10485760
S3_MAX_VIDEO_UPLOAD_BYTES=52428800
```

### Browser upload flow

1. Call `POST /api/uploads/presign/` with JSON payload:
```json
{
  "filename": "tour.mp4",
  "content_type": "video/mp4",
  "size": 41234567,
  "kind": "video",
  "folder": "property-listings"
}
```
2. Use returned `upload.url` and `upload.fields` to submit a `FormData` POST directly to S3.
3. Save returned `file_key` in your model field (this is the storage-relative name).

### Minimal frontend example

```javascript
async function uploadDirectToS3(file, kind = "image", folder = "admin") {
  const presignRes = await fetch("/api/uploads/presign/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCsrfToken(),
    },
    body: JSON.stringify({
      filename: file.name,
      content_type: file.type,
      size: file.size,
      kind,
      folder,
    }),
  });

  const presignData = await presignRes.json();
  if (!presignRes.ok || !presignData.success) {
    throw new Error(presignData.error || "Failed to prepare upload");
  }

  const formData = new FormData();
  Object.entries(presignData.upload.fields).forEach(([k, v]) => formData.append(k, v));
  formData.append("file", file);

  const s3Res = await fetch(presignData.upload.url, {
    method: "POST",
    body: formData,
  });

  if (!s3Res.ok) {
    throw new Error("S3 upload failed");
  }

  return presignData.file_key;
}
```

### S3 CORS example

```json
[
  {
    "AllowedOrigins": ["https://rajtexas.com", "https://www.rajtexas.com"],
    "AllowedMethods": ["POST", "PUT", "GET", "HEAD"],
    "AllowedHeaders": ["*"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 3000
  }
]
```

### IAM permissions for upload signer

Grant only the minimum required:

1. `s3:PutObject`
2. `s3:AbortMultipartUpload`
3. `s3:ListBucket` (optional, if needed by tooling)

Scope access to bucket prefix:

1. `arn:aws:s3:::<bucket>/media/uploads/*`

### Important note on scraping

Public pages can always be scraped at the HTML level. Direct S3 uploads protect credentials and backend limits; they do not make rendered public content undiscoverable.
