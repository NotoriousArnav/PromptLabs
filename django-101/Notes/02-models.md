# Block 2: Models

Defining your data schema with Django's ORM.

---

## Django ORM Philosophy

**Models = Tables**
**Python = SQL**

You describe your data in Python classes. Django translates that to database tables.

### Benefits

- **Database-agnostic** - Switch from SQLite to Postgres freely
- **Migrations** - Track every schema change
- **Querysets** - Lazy and chainable
- **Relationships** - Feel natural in Python

---

## The PromptLab Models

### Model Relationships

```
User (Django built-in)
  │
  ├── Prompt (one user → many prompts)
  │     ├── Attachment (one prompt → many attachments)
  │     ├── Vote (one prompt → many votes)
  │     └── Comment (one prompt → many comments)
  │
  ├── Vote (one user → many votes)
  └── Comment (one user → many comments)
```

---

## The Prompt Model

```python
# prompts/models.py

from django.db import models
from django.contrib.auth.models import User

class Prompt(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='prompts'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    expected_output = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
```

**Key concepts:**
- `ForeignKey` to User = "belongs to a user"
- `related_name='prompts'` = access via `user.prompts.all()`
- `auto_now_add` = set on creation
- `auto_now` = update on every save

---

## The Attachment Model

```python
class Attachment(models.Model):
    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name='attachments'
    )
    file = models.FileField(upload_to='attachments/')
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.filename
```

**Key insight:** `FileField` with S3 backend = files go directly to your bucket.

---

## The Vote Model

```python
class Vote(models.Model):
    VOTE_CHOICES = [
        (1, 'Upvote'),
        (-1, 'Downvote'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    value = models.SmallIntegerField(choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'prompt']  # One vote per user per prompt
    
    def __str__(self):
        return f"{self.user.username} -> {self.prompt.title}: {self.value}"
```

**Constraint:** `unique_together` ensures one vote per user per prompt.

---

## The Comment Model

```python
class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
    
    def __str__(self):
        return f"{self.user.username} on {self.prompt.title}"
```

---

## Key Relationship Concepts

| Concept | Meaning |
|---------|---------|
| `ForeignKey` | Many-to-One relationship |
| `related_name` | Reverse lookup name |
| `on_delete=CASCADE` | Delete children when parent deleted |
| `unique_together` | Compound unique constraint |
| `ManyToManyField` | Many-to-Many relationship |
| `OneToOneField` | One-to-One relationship |

### on_delete Options

| Option | Behavior |
|--------|----------|
| `CASCADE` | Delete related objects |
| `PROTECT` | Prevent deletion |
| `SET_NULL` | Set to NULL (requires `null=True`) |
| `SET_DEFAULT` | Set to default value |
| `DO_NOTHING` | Do nothing (can break integrity) |

---

## Field Types

### Common Fields

| Field | Use Case |
|-------|----------|
| `CharField` | Short text (max_length required) |
| `TextField` | Long text |
| `IntegerField` | Whole numbers |
| `FloatField` | Decimal numbers |
| `DecimalField` | Precise decimals (money) |
| `BooleanField` | True/False |
| `DateField` | Date only |
| `DateTimeField` | Date and time |
| `EmailField` | Email validation |
| `URLField` | URL validation |
| `FileField` | File uploads |
| `ImageField` | Image uploads |
| `JSONField` | JSON data |

### Field Options

| Option | Purpose |
|--------|---------|
| `null=True` | Allow NULL in database |
| `blank=True` | Allow empty in forms |
| `default=value` | Default value |
| `choices=list` | Limit to choices |
| `unique=True` | Must be unique |
| `db_index=True` | Add database index |
| `verbose_name` | Human-readable name |
| `help_text` | Help text for forms |

---

## Migrations

### What They Are

- Version control for your database schema
- Generated automatically from model changes
- Applied incrementally

### The Workflow

```bash
# 1. Change your models in models.py

# 2. Generate migration files
uv run python manage.py makemigrations

# 3. Review the migration (optional)
uv run python manage.py showmigrations

# 4. Apply migrations to database
uv run python manage.py migrate
```

**Migrations are checked into git.** Your schema history travels with your code.

### Useful Migration Commands

```bash
# See all migrations and their status
uv run python manage.py showmigrations

# See SQL that would be executed
uv run python manage.py sqlmigrate prompts 0001

# Rollback to a specific migration
uv run python manage.py migrate prompts 0001

# Rollback all migrations for an app
uv run python manage.py migrate prompts zero
```

---

## Django Admin

### Register Your Models

```python
# prompts/admin.py

from django.contrib import admin
from .models import Prompt, Attachment, Vote, Comment

@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['filename', 'prompt', 'uploaded_at']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'prompt', 'value', 'created_at']
    list_filter = ['value']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'prompt', 'created_at']
    search_fields = ['content']
```

### What You Get for Free

- Full CRUD interface for all your models
- Search, filter, sort
- Bulk actions
- User management

**This alone saves weeks of development time.**

---

## Why Admin Panel Matters

- **Free back-office** - Customer support can access data
- **Non-technical users** - Product managers, ops, marketing
- **Production-ready** - Permissions, audit logs, search
- **Quick debugging** - See what's in your database
- **Client demos** - Show data without building UI

**Every Django project gets this for free.** Laravel Nova costs $199/year.

---

## ORM Deep Dive

### Key Concepts

| Concept | What It Means |
|---------|---------------|
| **Lazy Querysets** | Query doesn't run until you need data |
| **Chainable** | `.filter().exclude().order_by()` |
| **Managers** | Custom query methods on models |
| **select_related** | JOIN in one query (ForeignKey) |
| **prefetch_related** | Separate query, Python join (M2M) |
| **F() expressions** | Database-level operations |
| **Q() objects** | Complex OR/AND queries |

### Basic Queries

```python
# Get all prompts
Prompt.objects.all()

# Filter
Prompt.objects.filter(user=user)
Prompt.objects.filter(title__icontains='django')

# Exclude
Prompt.objects.exclude(votes__value=-1)

# Order
Prompt.objects.order_by('-created_at')

# Chain
Prompt.objects.filter(user=user).exclude(title='').order_by('-created_at')

# Get single object
Prompt.objects.get(id=1)  # Raises DoesNotExist if not found
Prompt.objects.filter(id=1).first()  # Returns None if not found

# Count
Prompt.objects.count()
Prompt.objects.filter(user=user).count()

# Exists
Prompt.objects.filter(user=user).exists()
```

### Advanced Queries

```python
from django.db.models import Q, F, Count, Sum, Avg

# OR queries with Q objects
Prompt.objects.filter(
    Q(title__icontains='django') | Q(content__icontains='django')
)

# AND with Q
Prompt.objects.filter(
    Q(user=user) & Q(created_at__year=2026)
)

# F expressions (database-level)
# Increment all vote values by 1
Vote.objects.update(value=F('value') + 1)

# Aggregation
Prompt.objects.aggregate(total_prompts=Count('id'))
Vote.objects.filter(prompt=prompt).aggregate(score=Sum('value'))

# Annotation (add computed fields)
prompts = Prompt.objects.annotate(
    vote_count=Count('votes'),
    score=Sum('votes__value')
)
for p in prompts:
    print(p.title, p.vote_count, p.score)
```

---

## Query Optimization

### I Learned This the Hard Way

| Problem | Symptom | Solution |
|---------|---------|----------|
| **N+1 queries** | Slow page loads | `select_related`, `prefetch_related` |
| **Fetching unused fields** | High memory | `.only()`, `.defer()` |
| **Large result sets** | Timeout | Pagination, `.iterator()` |
| **Missing indexes** | Slow filters | `db_index=True`, compound indexes |
| **No caching** | Repeated queries | Django cache, `@cached_property` |
| **Fat models** | Complex logic | Move to services/managers |

### select_related vs prefetch_related

```python
# BAD: N+1 problem (1 query + N queries for each user)
prompts = Prompt.objects.all()
for p in prompts:
    print(p.user.username)  # Each access = new query!

# GOOD: select_related for ForeignKey (single JOIN query)
prompts = Prompt.objects.select_related('user').all()
for p in prompts:
    print(p.user.username)  # No extra query!

# GOOD: prefetch_related for reverse FK / M2M
prompts = Prompt.objects.prefetch_related('comments', 'votes').all()
for p in prompts:
    for c in p.comments.all():  # No extra query!
        print(c.content)
```

### Only/Defer

```python
# Only fetch specific fields
Prompt.objects.only('title', 'created_at')

# Defer expensive fields
Prompt.objects.defer('content', 'expected_output')
```

---

## Common ORM Pitfalls

**Mistakes I've made (so you don't have to):**

1. **Querying in loops** - Use `prefetch_related` instead
2. **Forgetting `select_related`** - Every ForeignKey access = new query
3. **Not indexing filter fields** - Database scans entire table
4. **Calling `.count()` after `.all()`** - Two queries instead of one
5. **Using `.get()` without try/except** - Crashes on missing data
6. **Saving in loops** - Use `bulk_create`, `bulk_update`

### Examples

```python
# BAD: Saving in loop
for data in data_list:
    Prompt.objects.create(**data)  # N queries

# GOOD: Bulk create
Prompt.objects.bulk_create([
    Prompt(**data) for data in data_list
])  # 1 query

# BAD: Get without exception handling
prompt = Prompt.objects.get(id=999)  # Crashes!

# GOOD: Handle DoesNotExist
try:
    prompt = Prompt.objects.get(id=999)
except Prompt.DoesNotExist:
    prompt = None

# BETTER: Use filter().first()
prompt = Prompt.objects.filter(id=999).first()  # Returns None
```

---

## Custom Managers

```python
# prompts/models.py

class PromptManager(models.Manager):
    def published(self):
        return self.filter(is_published=True)
    
    def by_user(self, user):
        return self.filter(user=user)
    
    def with_vote_count(self):
        return self.annotate(vote_count=Count('votes'))

class Prompt(models.Model):
    # ... fields ...
    
    objects = PromptManager()

# Usage
Prompt.objects.published()
Prompt.objects.by_user(user)
Prompt.objects.with_vote_count()
```

---

## Next Steps

Continue to [03-django-rest-framework.md](./03-django-rest-framework.md) to learn about building APIs with DRF.
