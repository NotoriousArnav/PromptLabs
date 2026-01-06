# Block 3: Django REST Framework

Turning your models into APIs.

---

## What is DRF?

**Django REST Framework** = Django's API toolkit

### What It Gives You

| Feature | Description |
|---------|-------------|
| **Serializers** | Model to JSON translation |
| **ViewSets** | CRUD in one class |
| **Routers** | Automatic URL generation |
| **Browsable API** | Test in your browser |
| **Auth & Permissions** | Built-in security |

---

## Without DRF vs With DRF

### Without DRF

```python
# views.py - Manual approach
import json
from django.http import JsonResponse
from django.views import View

class PromptListView(View):
    def get(self, request):
        prompts = Prompt.objects.all()
        data = []
        for p in prompts:
            data.append({
                'id': p.id,
                'title': p.title,
                'content': p.content,
                'user': p.user.username,
                'created_at': p.created_at.isoformat(),
            })
        return JsonResponse({'prompts': data})
    
    def post(self, request):
        data = json.loads(request.body)
        # Manual validation...
        # Manual error handling...
        # Manual response formatting...
```

### With DRF

```python
# serializers.py
from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'title', 'content', 'user', 'created_at']

# views.py
from rest_framework import viewsets
from .models import Prompt
from .serializers import PromptSerializer

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
```

**That's it.** Full CRUD API with validation, error handling, and pagination.

---

## Installation & Setup

### Install

```bash
uv add djangorestframework
```

### Configure

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

---

## Serializers

### What They Do

- Convert Model instances to JSON (serialization)
- Convert JSON to Model instances (deserialization)
- Validate incoming data
- Handle nested relationships

**Think of them as:** The contract between your API and the outside world.

### Serializer Types

| Type | Use Case |
|------|----------|
| `Serializer` | Full manual control |
| `ModelSerializer` | Auto-generates from model |
| Nested Serializers | Include related data |

---

## ModelSerializer

```python
# prompts/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Prompt, Attachment, Vote, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PromptSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Prompt
        fields = [
            'id', 'user', 'title', 'content', 
            'expected_output', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'prompt', 'file', 'filename', 'uploaded_at']
        read_only_fields = ['uploaded_at']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'prompt', 'value', 'created_at']
        read_only_fields = ['user', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'prompt', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
```

### Key Options

| Option | Purpose |
|--------|---------|
| `fields` | Which fields to include |
| `exclude` | Which fields to exclude |
| `read_only_fields` | Fields that can't be written |
| `extra_kwargs` | Additional field options |

---

## Nested Serializers

### Include Related Data

```python
class PromptDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    vote_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Prompt
        fields = [
            'id', 'user', 'title', 'content', 'expected_output',
            'attachments', 'comments', 'vote_count',
            'created_at', 'updated_at'
        ]
    
    def get_vote_count(self, obj):
        return obj.votes.aggregate(
            score=Sum('value')
        )['score'] or 0
```

### SerializerMethodField

Use `SerializerMethodField` for computed values:

```python
class PromptSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    
    def get_vote_count(self, obj):
        return obj.votes.count()
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.user == request.user
        return False
```

---

## Custom Validation

```python
class PromptSerializer(serializers.ModelSerializer):
    # Field-level validation
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Title must be at least 5 characters"
            )
        return value
    
    # Object-level validation
    def validate(self, data):
        if 'content' in data and len(data['content']) < 10:
            raise serializers.ValidationError({
                'content': "Content must be at least 10 characters"
            })
        return data
```

---

## ViewSets

### What They Do

- Combine related views into one class
- Handle list, create, retrieve, update, delete
- `ModelViewSet` gives you full CRUD

### Basic ViewSet

```python
# prompts/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Prompt, Attachment, Vote, Comment
from .serializers import (
    PromptSerializer, AttachmentSerializer,
    VoteSerializer, CommentSerializer
)

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

### Key Methods

| Method | Purpose |
|--------|---------|
| `get_queryset()` | What data to return |
| `get_serializer_class()` | Which serializer to use |
| `perform_create()` | Custom creation logic |
| `perform_update()` | Custom update logic |
| `perform_destroy()` | Custom deletion logic |

### Different Serializers for Different Actions

```python
class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PromptListSerializer
        if self.action == 'retrieve':
            return PromptDetailSerializer
        return PromptSerializer
```

### Filter Queryset

```python
class PromptViewSet(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    
    def get_queryset(self):
        queryset = Prompt.objects.all()
        
        # Filter by user
        user_id = self.request.query_params.get('user')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        
        # Search
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search)
            )
        
        return queryset.select_related('user')
```

---

## Routers

### What They Do

- Auto-generate URL patterns from ViewSets
- RESTful conventions out of the box

### Setup

```python
# prompts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PromptViewSet, AttachmentViewSet, VoteViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'prompts', PromptViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

```python
# promptlab/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prompts.urls')),
]
```

### Generated URLs

```
GET    /api/prompts/      → List all prompts
POST   /api/prompts/      → Create a prompt
GET    /api/prompts/1/    → Retrieve prompt #1
PUT    /api/prompts/1/    → Update prompt #1
PATCH  /api/prompts/1/    → Partial update prompt #1
DELETE /api/prompts/1/    → Delete prompt #1
```

---

## The Browsable API

**DRF's killer feature:**

- Visit your API in a browser
- See formatted JSON responses
- Test POST/PUT/DELETE with forms
- Authenticate and test protected endpoints

Access at: `http://localhost:8000/api/`

**Perfect for development and debugging.**

---

## Custom Actions

Add custom endpoints to your ViewSet:

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class PromptViewSet(viewsets.ModelViewSet):
    # ... standard stuff ...
    
    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        prompt = self.get_object()
        vote, created = Vote.objects.update_or_create(
            user=request.user,
            prompt=prompt,
            defaults={'value': 1}
        )
        return Response({'status': 'upvoted'})
    
    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        prompt = self.get_object()
        vote, created = Vote.objects.update_or_create(
            user=request.user,
            prompt=prompt,
            defaults={'value': -1}
        )
        return Response({'status': 'downvoted'})
    
    @action(detail=False, methods=['get'])
    def my_prompts(self, request):
        prompts = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(prompts, many=True)
        return Response(serializer.data)
```

**URLs generated:**
- `POST /api/prompts/1/upvote/`
- `POST /api/prompts/1/downvote/`
- `GET /api/prompts/my_prompts/`

---

## Pagination

### Configuration

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
```

### Custom Pagination

```python
# pagination.py
from rest_framework.pagination import PageNumberPagination

class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# views.py
class PromptViewSet(viewsets.ModelViewSet):
    pagination_class = StandardPagination
```

### Response Format

```json
{
    "count": 100,
    "next": "http://localhost:8000/api/prompts/?page=2",
    "previous": null,
    "results": [
        {"id": 1, "title": "..."},
        {"id": 2, "title": "..."}
    ]
}
```

---

## Filtering

### Install django-filter

```bash
uv add django-filter
```

### Configure

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'django_filters',
]

REST_FRAMEWORK = {
    # ...
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

### Use in ViewSet

```python
class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    filterset_fields = ['user', 'created_at']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
```

**Usage:**
- `/api/prompts/?user=1` - Filter by user
- `/api/prompts/?search=django` - Search
- `/api/prompts/?ordering=-created_at` - Order by

---

## API Testing Options

| Tool | Type | Best For |
|------|------|----------|
| Browser | GUI | Quick exploration |
| curl | CLI | Scripts, automation |
| httpie | CLI | Human-friendly CLI |
| Postman | GUI | Complex workflows |
| DRF Browser | Built-in | Development |

### curl Examples

```bash
# GET all prompts
curl http://localhost:8000/api/prompts/

# GET single prompt
curl http://localhost:8000/api/prompts/1/

# POST create prompt (with auth)
curl -X POST http://localhost:8000/api/prompts/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Prompt", "content": "Content here"}'

# PUT update prompt
curl -X PUT http://localhost:8000/api/prompts/1/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title", "content": "Updated content"}'

# DELETE prompt
curl -X DELETE http://localhost:8000/api/prompts/1/ \
  -H "Authorization: Token your-token-here"
```

### httpie Examples

```bash
# Install httpie
pip install httpie

# GET
http localhost:8000/api/prompts/

# POST
http POST localhost:8000/api/prompts/ \
  Authorization:"Token your-token" \
  title="My Prompt" \
  content="Content here"
```

---

## Next Steps

Continue to [04-authentication.md](./04-authentication.md) to learn about Knox token authentication.
