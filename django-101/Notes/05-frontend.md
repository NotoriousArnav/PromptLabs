# Block 5: Frontend

Django Templates + Kairo CSS + Alpine.js

---

## The Frontend Stack

| Tool | Purpose |
|------|---------|
| **Django Templates** | Server-rendered HTML |
| **Kairo CSS** | Classless semantic styling |
| **Alpine.js** | Lightweight reactivity |

**No build step. No npm. No webpack. No classes to memorize.**

---

## Why This Stack?

| Concern | Solution |
|---------|----------|
| SEO | Server-rendered HTML |
| Interactivity | Alpine.js |
| Styling | Kairo CSS (classless) |
| Data | DRF API |
| Auth | Knox tokens in localStorage |

**Full-stack Django without the SPA complexity.**

---

## Django Templates

### What They Are

Django's built-in templating engine:
- Similar to Jinja2
- Template inheritance (base → child)
- Filters and tags
- Context variables from views

### Template Directory Setup

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Directory Structure

```
promptlab/
├── templates/
│   ├── base.html           # Master layout
│   ├── home.html           # Homepage
│   ├── prompts/
│   │   ├── list.html       # Prompt list
│   │   └── detail.html     # Prompt detail
│   └── account/            # Allauth overrides
│       ├── login.html
│       └── signup.html
└── prompts/
    └── templates/
        └── prompts/        # App-specific templates
```

---

## Template Inheritance

### Base Template

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}PromptLab{% endblock %}</title>
    
    <!-- Kairo CSS -->
    <link rel="stylesheet" href="https://unpkg.com/kairocss@latest/dist/kairo.min.css">
    
    <!-- Custom CSS variables -->
    <style>
        :root {
            --primary: #DE9F68;
            --secondary: #361E19;
        }
    </style>
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <nav>
            <a href="{% url 'home' %}"><strong>PromptLab</strong></a>
            <ul>
                <li><a href="{% url 'prompt-list' %}">Prompts</a></li>
                {% if user.is_authenticated %}
                    <li><a href="{% url 'account_logout' %}">Logout</a></li>
                {% else %}
                    <li><a href="{% url 'account_login' %}">Login</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2026 PromptLab. Built with Django.</p>
    </footer>
    
    <!-- Alpine.js -->
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Child Template

```html
<!-- templates/prompts/list.html -->
{% extends 'base.html' %}

{% block title %}Prompts - PromptLab{% endblock %}

{% block content %}
<h1>Prompts</h1>

<section x-data="promptList()">
    <template x-for="prompt in prompts" :key="prompt.id">
        <article>
            <h2 x-text="prompt.title"></h2>
            <p x-text="prompt.content"></p>
            <small>
                By <span x-text="prompt.user.username"></span>
                on <span x-text="formatDate(prompt.created_at)"></span>
            </small>
        </article>
    </template>
</section>
{% endblock %}

{% block extra_js %}
<script>
function promptList() {
    return {
        prompts: [],
        async init() {
            const response = await fetch('/api/prompts/');
            const data = await response.json();
            this.prompts = data.results;
        },
        formatDate(dateStr) {
            return new Date(dateStr).toLocaleDateString();
        }
    }
}
</script>
{% endblock %}
```

---

## Template Tags & Filters

### Common Tags

```html
<!-- Variables -->
{{ variable }}
{{ object.attribute }}

<!-- If/else -->
{% if condition %}
    ...
{% elif other_condition %}
    ...
{% else %}
    ...
{% endif %}

<!-- For loops -->
{% for item in items %}
    {{ item }}
{% empty %}
    No items found.
{% endfor %}

<!-- URLs -->
<a href="{% url 'view-name' %}">Link</a>
<a href="{% url 'prompt-detail' prompt.id %}">{{ prompt.title }}</a>

<!-- Static files -->
{% load static %}
<img src="{% static 'images/logo.png' %}">

<!-- Include other templates -->
{% include 'partials/card.html' with item=prompt %}

<!-- Block definition/override -->
{% block content %}{% endblock %}
```

### Common Filters

```html
<!-- Text -->
{{ text|lower }}
{{ text|upper }}
{{ text|title }}
{{ text|truncatewords:30 }}
{{ text|linebreaks }}
{{ text|safe }}  <!-- Mark as safe HTML -->

<!-- Numbers -->
{{ number|floatformat:2 }}
{{ number|filesizeformat }}

<!-- Dates -->
{{ date|date:"F j, Y" }}
{{ date|timesince }}

<!-- Lists -->
{{ list|length }}
{{ list|first }}
{{ list|last }}
{{ list|join:", " }}

<!-- Default values -->
{{ value|default:"N/A" }}
{{ value|default_if_none:"N/A" }}
```

---

## Kairo CSS

### What It Is

**Classless CSS framework for semantic HTML:**
- Write semantic HTML, get beautiful defaults
- No classes to memorize or look up
- Single file, under 15KB
- Just set `--primary` and `--secondary` colors
- Dark mode built-in

**Philosophy:** *"Good design is as little design as possible."*

### Installation

```html
<!-- CDN -->
<link rel="stylesheet" href="https://unpkg.com/kairocss@latest/dist/kairo.min.css">

<!-- Or download and serve locally -->
<link rel="stylesheet" href="{% static 'css/kairo.min.css' %}">
```

### Customization

```html
<style>
    :root {
        --primary: #DE9F68;    /* Bronze */
        --secondary: #361E19;  /* Dark Coffee */
        --font-family: 'Segoe UI', sans-serif;
    }
</style>
```

### Semantic HTML = Styled

```html
<!-- These all get styled automatically -->
<header>...</header>
<nav>...</nav>
<main>...</main>
<article>...</article>
<section>...</section>
<aside>...</aside>
<footer>...</footer>

<h1>Heading 1</h1>
<p>Paragraph</p>
<a href="#">Link</a>
<button>Button</button>

<form>
    <label>
        Name
        <input type="text" name="name">
    </label>
    <button type="submit">Submit</button>
</form>

<table>
    <thead><tr><th>Header</th></tr></thead>
    <tbody><tr><td>Cell</td></tr></tbody>
</table>
```

[Kairo CSS Documentation](https://kairocss.nnisarg.in/)

---

## Alpine.js

### What It Is

**Reactivity without React:**
- 15kb, no build step
- Declare behavior in HTML attributes
- Works with server-rendered pages
- Perfect for "islands of interactivity"

**The jQuery of the modern era, but better.**

### Installation

```html
<script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

---

## Alpine.js Concepts

### Core Directives

| Directive | Purpose |
|-----------|---------|
| `x-data` | Component state |
| `x-init` | Run on initialization |
| `x-show` | Toggle visibility |
| `x-if` | Conditional rendering |
| `x-for` | Loop over items |
| `x-model` | Two-way binding |
| `x-text` | Set text content |
| `x-html` | Set HTML content |
| `x-bind` | Bind attributes |
| `x-on` / `@` | Event handling |
| `x-ref` | Element reference |

---

## Alpine.js Examples

### Basic Component

```html
<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    <div x-show="open">
        Content here
    </div>
</div>
```

### Counter

```html
<div x-data="{ count: 0 }">
    <button @click="count--">-</button>
    <span x-text="count"></span>
    <button @click="count++">+</button>
</div>
```

### Form with Two-Way Binding

```html
<div x-data="{ name: '', email: '' }">
    <input type="text" x-model="name" placeholder="Name">
    <input type="email" x-model="email" placeholder="Email">
    <p>Hello, <span x-text="name || 'stranger'"></span>!</p>
</div>
```

### Fetching Data

```html
<div x-data="{ prompts: [], loading: true }" x-init="
    fetch('/api/prompts/')
        .then(r => r.json())
        .then(data => { prompts = data.results; loading = false; })
">
    <template x-if="loading">
        <p>Loading...</p>
    </template>
    
    <template x-for="prompt in prompts" :key="prompt.id">
        <article>
            <h2 x-text="prompt.title"></h2>
            <p x-text="prompt.content"></p>
        </article>
    </template>
</div>
```

### With External Function

```html
<div x-data="promptApp()">
    <button @click="loadPrompts">Load Prompts</button>
    
    <template x-for="prompt in prompts">
        <article>
            <h2 x-text="prompt.title"></h2>
        </article>
    </template>
</div>

<script>
function promptApp() {
    return {
        prompts: [],
        async loadPrompts() {
            const response = await fetch('/api/prompts/');
            const data = await response.json();
            this.prompts = data.results;
        }
    }
}
</script>
```

---

## The Full Pattern

1. **Django serves the page** (template)
2. **Alpine handles interactivity** (client-side)
3. **Fetch calls your DRF API** (data)
4. **Alpine updates the DOM** (reactivity)

**Server-rendered shell + API-driven content.**

---

## Complete Example: Prompt List

```html
<!-- templates/prompts/list.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Prompts</h1>

<div x-data="promptList()">
    <!-- Search -->
    <input 
        type="search" 
        x-model="search" 
        @input.debounce.300ms="loadPrompts"
        placeholder="Search prompts..."
    >
    
    <!-- Loading state -->
    <template x-if="loading">
        <p>Loading...</p>
    </template>
    
    <!-- Prompt list -->
    <template x-if="!loading">
        <div>
            <template x-for="prompt in prompts" :key="prompt.id">
                <article>
                    <h2>
                        <a :href="'/prompts/' + prompt.id" x-text="prompt.title"></a>
                    </h2>
                    <p x-text="prompt.content.substring(0, 200) + '...'"></p>
                    <footer>
                        <span x-text="prompt.user.username"></span>
                        &bull;
                        <span x-text="formatDate(prompt.created_at)"></span>
                        &bull;
                        <span x-text="prompt.vote_count + ' votes'"></span>
                    </footer>
                </article>
            </template>
            
            <!-- Pagination -->
            <nav>
                <button @click="prevPage" :disabled="!hasPrev">Previous</button>
                <span x-text="'Page ' + page"></span>
                <button @click="nextPage" :disabled="!hasNext">Next</button>
            </nav>
        </div>
    </template>
</div>
{% endblock %}

{% block extra_js %}
<script>
function promptList() {
    return {
        prompts: [],
        loading: true,
        search: '',
        page: 1,
        hasNext: false,
        hasPrev: false,
        
        async init() {
            await this.loadPrompts();
        },
        
        async loadPrompts() {
            this.loading = true;
            const params = new URLSearchParams({
                page: this.page,
                search: this.search
            });
            
            const response = await fetch(`/api/prompts/?${params}`);
            const data = await response.json();
            
            this.prompts = data.results;
            this.hasNext = !!data.next;
            this.hasPrev = !!data.previous;
            this.loading = false;
        },
        
        async nextPage() {
            this.page++;
            await this.loadPrompts();
        },
        
        async prevPage() {
            this.page--;
            await this.loadPrompts();
        },
        
        formatDate(dateStr) {
            return new Date(dateStr).toLocaleDateString();
        }
    }
}
</script>
{% endblock %}
```

---

## Authenticated Requests

```html
<div x-data="promptForm()">
    <form @submit.prevent="createPrompt">
        <label>
            Title
            <input type="text" x-model="title" required>
        </label>
        <label>
            Content
            <textarea x-model="content" required></textarea>
        </label>
        <button type="submit" :disabled="submitting">
            <span x-text="submitting ? 'Creating...' : 'Create Prompt'"></span>
        </button>
    </form>
    
    <p x-show="error" x-text="error" style="color: red;"></p>
</div>

<script>
function promptForm() {
    return {
        title: '',
        content: '',
        submitting: false,
        error: '',
        
        async createPrompt() {
            this.submitting = true;
            this.error = '';
            
            const token = localStorage.getItem('token');
            if (!token) {
                window.location.href = '/accounts/login/';
                return;
            }
            
            try {
                const response = await fetch('/api/prompts/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Token ${token}`
                    },
                    body: JSON.stringify({
                        title: this.title,
                        content: this.content
                    })
                });
                
                if (response.ok) {
                    const prompt = await response.json();
                    window.location.href = `/prompts/${prompt.id}/`;
                } else if (response.status === 401) {
                    localStorage.removeItem('token');
                    window.location.href = '/accounts/login/';
                } else {
                    const data = await response.json();
                    this.error = Object.values(data).flat().join(', ');
                }
            } catch (e) {
                this.error = 'Something went wrong';
            } finally {
                this.submitting = false;
            }
        }
    }
}
</script>
```

---

## Voting Component

```html
<div 
    x-data="voteComponent({{ prompt.id }}, {{ prompt.vote_count|default:0 }})"
    class="vote-buttons"
>
    <button @click="upvote" :class="{ active: userVote === 1 }">
        👍 Upvote
    </button>
    <span x-text="voteCount"></span>
    <button @click="downvote" :class="{ active: userVote === -1 }">
        👎 Downvote
    </button>
</div>

<script>
function voteComponent(promptId, initialCount) {
    return {
        promptId,
        voteCount: initialCount,
        userVote: 0,
        
        async vote(value) {
            const token = localStorage.getItem('token');
            if (!token) {
                window.location.href = '/accounts/login/';
                return;
            }
            
            const endpoint = value === 1 ? 'upvote' : 'downvote';
            const response = await fetch(`/api/prompts/${this.promptId}/${endpoint}/`, {
                method: 'POST',
                headers: { 'Authorization': `Token ${token}` }
            });
            
            if (response.ok) {
                // Update local state
                if (this.userVote === value) {
                    // Remove vote
                    this.voteCount -= value;
                    this.userVote = 0;
                } else {
                    // Change or add vote
                    this.voteCount += value - this.userVote;
                    this.userVote = value;
                }
            }
        },
        
        upvote() { this.vote(1); },
        downvote() { this.vote(-1); }
    }
}
</script>
```

---

## The Full Stack Loop

```
User Browser
    │
    ▼
Django Template (HTML + Kairo CSS + Alpine)
    │
    ▼ fetch()
DRF API (Knox Auth)
    │
    ▼ ORM
Database + S3 Storage
```

**Everything in one codebase. One deployment.**

---

## Next Steps

Continue to [06-assignment.md](./06-assignment.md) for the assignment details and submission guide.
