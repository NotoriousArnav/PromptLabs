# Block 4: Knox Authentication

Secure token-based authentication for your API.

---

## Authentication Options

| Method | How It Works |
|--------|--------------|
| **Session** | Cookie-based, server stores state |
| **Basic Auth** | Username:password every request |
| **JWT** | Stateless tokens, complex refresh |
| **DRF Token** | One token per user, no expiry |
| **Knox** | Multiple tokens, expiry, encrypted |

---

## Why Knox?

### DRF's Built-in TokenAuthentication

- One token per user, forever
- Stored in plain text
- No expiration
- Can't revoke individual sessions

### Knox

- Multiple tokens per user
- Token expiration
- Encrypted storage
- Revoke individual or all tokens

---

## Installation & Setup

### Install

```bash
uv add django-rest-knox
```

### Configure

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'knox',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
    ],
}

# Knox settings
from datetime import timedelta

REST_KNOX = {
    'TOKEN_TTL': timedelta(hours=24),  # Token expires after 24 hours
    'AUTO_REFRESH': True,              # Refresh token on each request
    'MIN_REFRESH_INTERVAL': 60,        # Minimum seconds between refreshes
    'TOKEN_LIMIT_PER_USER': 10,        # Max tokens per user
    'USER_SERIALIZER': 'prompts.serializers.UserSerializer',
}
```

### Migrate

```bash
uv run python manage.py migrate
```

---

## Knox Token Model

**One user can have:**
- Token for mobile app
- Token for web browser
- Token for CLI tool
- Token for third-party integration

**Each token:**
- Has its own expiry
- Can be revoked individually
- Is stored encrypted (only prefix visible)

---

## Knox Endpoints

### Setup URLs

```python
# promptlab/urls.py

from django.urls import path, include
from knox import views as knox_views
from .views import LoginView  # Custom login view

urlpatterns = [
    # ...
    path('api/auth/login/', LoginView.as_view(), name='knox_login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
```

### Endpoint Summary

| Endpoint | Purpose |
|----------|---------|
| `/api/auth/login/` | Get a new token |
| `/api/auth/logout/` | Revoke current token |
| `/api/auth/logoutall/` | Revoke ALL user tokens |

**LogoutAll is your security breach response button.**

---

## Custom Login View

```python
# prompts/views.py

from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginView(KnoxLoginView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)
```

### Login Response

```json
{
    "expiry": "2026-01-07T17:00:00.000000Z",
    "token": "abc123def456...",
    "user": {
        "id": 1,
        "username": "john",
        "email": "john@example.com"
    }
}
```

---

## Token Flow

1. **Login** - Send username/password, get token
2. **Store** - Save token (localStorage, secure storage)
3. **Use** - Send token in `Authorization` header
4. **Logout** - Invalidate token on server

### Making Authenticated Requests

```bash
# With curl
curl -H "Authorization: Token abc123def456..." \
  http://localhost:8000/api/prompts/

# With httpie
http localhost:8000/api/prompts/ \
  Authorization:"Token abc123def456..."
```

### In JavaScript

```javascript
// Login
const response = await fetch('/api/auth/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
});
const { token } = await response.json();
localStorage.setItem('token', token);

// Authenticated request
const prompts = await fetch('/api/prompts/', {
    headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`
    }
});

// Logout
await fetch('/api/auth/logout/', {
    method: 'POST',
    headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`
    }
});
localStorage.removeItem('token');
```

---

## Permissions

### Built-in Permission Classes

| Permission | Meaning |
|------------|---------|
| `AllowAny` | No auth required |
| `IsAuthenticated` | Must have valid token |
| `IsAuthenticatedOrReadOnly` | Read = open, write = auth |
| `IsAdminUser` | Must be staff |

### Applying Permissions

```python
# Global (settings.py)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# Per ViewSet
from rest_framework.permissions import IsAuthenticated

class PromptViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

# Per action
class PromptViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
```

---

## Custom Permissions

### IsOwner Permission

```python
# prompts/permissions.py

from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners to edit/delete.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only to owner
        return obj.user == request.user
```

### IsOwnerOrReadOnly

```python
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read: Anyone
    Write: Owner only
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
```

### Using Custom Permissions

```python
from .permissions import IsOwnerOrReadOnly

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

---

## Token Expiration

### Configure Based on Your Needs

| Use Case | TTL |
|----------|-----|
| High security | 1 hour |
| Normal web app | 24 hours |
| Mobile app | 7-30 days |
| Remember me | 90 days |

```python
# settings.py
from datetime import timedelta

REST_KNOX = {
    'TOKEN_TTL': timedelta(hours=24),
}
```

**Expired tokens are automatically rejected.**

### Handling Expired Tokens (Frontend)

```javascript
async function fetchWithAuth(url, options = {}) {
    const token = localStorage.getItem('token');
    
    const response = await fetch(url, {
        ...options,
        headers: {
            ...options.headers,
            'Authorization': `Token ${token}`
        }
    });
    
    if (response.status === 401) {
        // Token expired - redirect to login
        localStorage.removeItem('token');
        window.location.href = '/login/';
        return;
    }
    
    return response;
}
```

---

## Registration Endpoint

Knox doesn't include registration. Create your own:

```python
# prompts/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({
                'password_confirm': "Passwords don't match"
            })
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user
```

```python
# prompts/views.py

from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create token for new user
        _, token = AuthToken.objects.create(user)
        
        return Response({
            'user': UserSerializer(user).data,
            'token': token
        }, status=status.HTTP_201_CREATED)
```

```python
# urls.py
urlpatterns = [
    # ...
    path('api/auth/register/', RegisterView.as_view(), name='register'),
]
```

---

## Current User Endpoint

```python
# prompts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
```

```python
# urls.py
urlpatterns = [
    # ...
    path('api/auth/user/', CurrentUserView.as_view(), name='current_user'),
]
```

---

## Complete Auth URL Setup

```python
# promptlab/urls.py

from django.urls import path, include
from knox import views as knox_views
from prompts.views import LoginView, RegisterView, CurrentUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prompts.urls')),
    
    # Auth endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/auth/user/', CurrentUserView.as_view(), name='current_user'),
]
```

### API Summary

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/api/auth/register/` | POST | No | Create account, get token |
| `/api/auth/login/` | POST | No | Login, get token |
| `/api/auth/logout/` | POST | Yes | Revoke current token |
| `/api/auth/logoutall/` | POST | Yes | Revoke all tokens |
| `/api/auth/user/` | GET | Yes | Get current user |

---

## Security Best Practices

1. **Use HTTPS in production** - Tokens are sensitive
2. **Set reasonable TTL** - Don't use infinite tokens
3. **Implement token refresh** - For long sessions
4. **Limit tokens per user** - Prevent abuse
5. **Use LogoutAll on password change** - Invalidate old sessions
6. **Store tokens securely** - httpOnly cookies or secure storage

---

## Next Steps

Continue to [05-frontend.md](./05-frontend.md) to learn about building the frontend with Django Templates, Kairo CSS, and Alpine.js.
