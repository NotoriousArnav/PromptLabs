# Block 1: Project Configuration

Setting up the foundation with `uv` - the modern Python package manager.

---

## Why uv?

`uv` is the modern Python package manager written in Rust.

| Feature | Description |
|---------|-------------|
| **Fast** | 10-100x faster than pip |
| **Reliable** | Deterministic dependency resolution |
| **All-in-one** | Replaces pip, venv, pip-tools, pyenv |
| **Project-aware** | Manages virtual environments automatically |

### Installation

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

---

## Project Creation

### Step 1: Initialize Project

```bash
# Create a new Python project
uv init promptlab
cd promptlab

# Add Django
uv add django

# Create Django project
uv run django-admin startproject promptlab .

# Create the prompts app
uv run python manage.py startapp prompts
```

**Key insight:** `uv` handles the virtual environment for you. No more `source venv/bin/activate` dance.

### Step 2: Add Dependencies

```bash
# Core dependencies
uv add djangorestframework
uv add django-rest-knox
uv add django-storages
uv add django-allauth
uv add boto3  # For S3
uv add python-dotenv  # For environment variables
```

---

## Project Structure

After setup, you'll have:

```
promptlab/
├── pyproject.toml      # Project config (uv manages this)
├── uv.lock             # Locked dependencies
├── .python-version     # Python version
├── manage.py           # Django CLI entry point
├── promptlab/
│   ├── __init__.py
│   ├── settings.py     # The brain of your project
│   ├── urls.py         # URL routing
│   ├── asgi.py         # ASGI interface
│   └── wsgi.py         # WSGI interface
└── prompts/
    ├── __init__.py
    ├── models.py       # Your data schemas
    ├── views.py        # Your logic
    ├── admin.py        # Admin configuration
    ├── apps.py         # App configuration
    └── tests.py        # Tests
```

---

## settings.py - The Control Center

### Key Sections

| Setting | Purpose |
|---------|---------|
| `SECRET_KEY` | Cryptographic signing (never commit!) |
| `DEBUG` | Development vs Production mode |
| `INSTALLED_APPS` | Which apps are active |
| `DATABASES` | Database connections |
| `STATIC/MEDIA` | Asset handling |

---

## Environment Variables

### Why Use Environment Variables?

- Keep secrets out of code
- Different configs for dev/staging/prod
- 12-factor app compliance

### Setup with python-dotenv

**1. Create `.env` file (never commit this!):**

```env
SECRET_KEY=your-super-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

# S3/MinIO
AWS_ACCESS_KEY_ID=minioadmin
AWS_SECRET_ACCESS_KEY=minioadmin
AWS_STORAGE_BUCKET_NAME=promptlab
AWS_S3_ENDPOINT_URL=http://localhost:9000
```

**2. Update settings.py:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
```

**3. Add to .gitignore:**

```gitignore
.env
*.sqlite3
__pycache__/
```

---

## Database Configuration

### Development: SQLite

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**Benefits:**
- Zero configuration
- File-based, perfect for local dev
- Ships with Python

### Production: PostgreSQL

```python
# settings.py
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
```

**Benefits:**
- Battle-tested at scale
- Rich features (JSON fields, full-text search)
- Same ORM code works for both!

---

## S3 / MinIO Storage

### The Strategy

- **Locally:** MinIO (S3-compatible, runs on your laptop)
- **Production:** AWS S3, Supabase Storage, or any S3-compatible service

### Running MinIO Locally

```bash
# With Docker
docker run -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin \
  -e MINIO_ROOT_PASSWORD=minioadmin \
  minio/minio server /data --console-address ":9001"
```

Access MinIO Console at `http://localhost:9001`

### Configure Django for S3

```python
# settings.py

# Storage backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# S3 settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')  # For MinIO
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'us-east-1'
```

---

## Static vs Media Files

| Type | What | Example |
|------|------|---------|
| **Static** | Your app's assets | CSS, JS, images in your repo |
| **Media** | User uploads | Profile pictures, attachments |

### Configuration

```python
# settings.py

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**For production:** Static files go to CDN, Media files go to S3.

---

## Installed Apps

```python
# settings.py

INSTALLED_APPS = [
    # Django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for allauth
    
    # Third-party
    'rest_framework',
    'knox',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Your apps
    'prompts',
]

SITE_ID = 1  # Required for allauth
```

**Order matters!** Django loads apps in sequence.

---

## django-allauth Configuration

### What It Gives You

- Registration, login, logout
- Email verification
- Password reset flow
- Social auth (Google, GitHub, etc.)
- Account management pages

### Configuration

```python
# settings.py

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # or 'mandatory'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Template Overrides

To customize allauth templates:

1. Create `templates/account/` directory
2. Copy allauth templates you want to customize
3. Style with Kairo CSS (or just use defaults!)
4. Your templates take precedence

**Override only what you need.**

---

## Running the Project

```bash
# Apply migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Run development server
uv run python manage.py runserver
```

Access:
- Site: `http://localhost:8000`
- Admin: `http://localhost:8000/admin`

---

## Common Commands

```bash
# Run server
uv run python manage.py runserver

# Make migrations
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Django shell
uv run python manage.py shell

# Collect static files (for production)
uv run python manage.py collectstatic
```

---

## Next Steps

Continue to [02-models.md](./02-models.md) to learn about Django models and the ORM.
