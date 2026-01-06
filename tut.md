Commands used to start the project
```bash
uv init project_name
uv add django
uv run django-admin startproject project_name .
```

Commands to run the Project:
```bash
uv run manage.py migrate #If there is the Migrate message
uv run runserver
```

Commands to install django-allauth:
```bash
uv pip install "django-allauth[socialaccount]"
```
