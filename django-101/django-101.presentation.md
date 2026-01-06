---
marp: true
theme: default
paginate: true
header: "BroCode Protocols: Django & API Bootcamp"
style: |
  :root {
    --color-bronze: #DE9F68;
    --color-sandy: #EEB086;
    --color-white: #F9F9F0;
    --color-coffee: #361E19;
    --color-mocha: #362A2A;
  }
  section {
    background: var(--color-coffee);
    color: var(--color-white);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 24px;
  }
  h1 {
    font-size: 1.8em;
  }
  h2 {
    font-size: 1.4em;
  }
  h3 {
    font-size: 1.2em;
  }
  h1, h2, h3 {
    color: var(--color-bronze);
  }
  a {
    color: var(--color-sandy);
  }
  code {
    background: var(--color-mocha);
    color: var(--color-sandy);
    padding: 2px 8px;
    border-radius: 4px;
  }
  header {
    color: var(--color-sandy);
    font-size: 14px;
  }
  footer {
    color: var(--color-sandy);
  }
  strong {
    color: var(--color-bronze);
  }
  blockquote {
    border-left: 4px solid var(--color-bronze);
    background: var(--color-mocha);
    padding: 10px 20px;
    margin: 20px 0;
  }
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th {
    background: var(--color-mocha);
    color: var(--color-bronze);
    padding: 12px;
    border: 1px solid var(--color-bronze);
  }
  td {
    background: var(--color-mocha);
    color: var(--color-white);
    padding: 10px;
    border: 1px solid var(--color-coffee);
  }
  tr:nth-child(even) td {
    background: var(--color-coffee);
  }
  .title-slide {
    text-align: center;
  }
---

<!-- slide-id: 499ebdcb-c4c5-4eec-a030-e230636dcb7c -->

<!-- _class: title-slide -->
<!-- _paginate: false -->
<!-- _header: "" -->

# BroCode Protocols
## The Django & API Bootcamp

**Building PromptLab: A Data-Centric Application**

January 6, 2026 | 17:00 - 20:00 IST

![w:150](logo.jpg)

---

<!-- slide-id: 699693b8-007a-4620-8c41-edbed70eee83 -->

# What You'll Walk Away With

- A working understanding of **Django's data-centric approach**
- **PromptLab** - a complete reference project you can learn from
- An **assignment** to build your own project (1 week)
- **Personalized certificate** upon successful submission

*This is a builder's bootcamp. You will leave with something real.*

---

<!-- slide-id: 67b868ce-a092-4510-a595-d783fc1d745e -->

# About Me

## Arnav Ghosh

- **Founder** - BroCode Tech Community
- **Full Stack Developer** - Python, Django, React, and beyond
- Building tools that solve real problems
- Believer in learning by building

**Find me:**
- GitHub: [@NotoriousArnav](https://github.com/NotoriousArnav)
- Website: [arnavg.netlify.app](https://arnavg.netlify.app)

---

<!-- slide-id: e2fca5ea-7250-4451-ae31-c22f25daa0f1 -->

# BroCode Tech Community

> "For Developers, By Developers"

**What we do:**
- Community-driven learning and collaboration
- Hands-on bootcamps and workshops
- Open source projects

**Join us:**
- WhatsApp Group for real-time discussions
- GitHub: [BroCode501](https://github.com/BroCode501/)
- Blog Platform: [Bromine](https://bromine.vercel.app/)
- Events: [Event Horizon](https://events.neopanda.tech)

![bg right:30% w:200](logo.jpg)

---

<!-- slide-id: da51620c-8f6c-4dfc-a0dc-e8a6f9b797a8 -->

# Thank You - Global Response

I expected **~25 from India**. You gave me **54 from 7+ countries.**

| Region | Countries |
|--------|-----------|
| South Asia | India, Nepal |
| East Africa | Kenya, Burundi |
| West Africa | Nigeria |
| Middle East | Saudi Arabia |
| Europe | Portugal |

**This is bigger than I imagined. Thank you for believing in this.**

---

<!-- slide-id: 4bd736fc-4aab-4e61-9c20-2669c9cf332f -->

# What We're Building: PromptLab

A **data-centric** application for storing and organizing AI prompts.

**Core Features:**
- Store prompts with attachments and expected outputs
- Upvotes, downvotes, and comments
- User authentication with Knox tokens
- S3-compatible storage (MinIO locally, AWS/Supabase in prod)

**The Dream:** Collect data now, build analytics later.
*Just like Instagram started with photos, Spotify with music catalogs.*

---

<!-- slide-id: f49f7192-7429-4d56-b4e7-3b96e63ec9ca -->

# Why Django?

**Alternatives exist and they're valid:**
- **Pocketbase** - SQLite-based, single binary, great for MVPs
- **Supabase** - Postgres + Auth + Storage, open source Firebase
- **Firebase** - Google's BaaS, real-time database
- **Appwrite** - Self-hosted BaaS alternative

These are excellent for quick prototypes and MVPs.

**But we're here to learn the source.**

---

<!-- slide-id: b4b38ae6-db4d-46b5-a68a-79e242e4b360 -->

# My Mental Model

| Use Case | My Choice | Why |
|----------|-----------|-----|
| ML Model API | FastAPI | Speed, async, minimal overhead |
| Data-Centric App | **Django** | ORM, Admin, relationships |

*If someone asks me to build a Google Photos clone, I pick Django.*
*If someone asks me to serve their ML model, I pick FastAPI.*

**Django thinks in data relationships. That's its superpower.**

---

<!-- slide-id: 12a26fb5-276d-44f7-a648-541efa57cf3c -->

<!-- slide-id: new-django-at-scale -->

# Django at Scale - Proof It Works

**Companies built on Django:**

| Company | Scale | What They Do |
|---------|-------|--------------|
| **Instagram** | 2B+ users | Photo sharing, stories, reels |
| **Pinterest** | 450M+ users | Visual discovery engine |
| **Disqus** | 50M+ comments/month | Comment system |
| **Eventbrite** | 4M+ events/year | Event management |
| **Mozilla** | 100M+ users | Firefox add-ons, support |

*If it's good enough for Instagram, it's good enough for your side project.*

---

<!-- slide-id: a16350ad-4223-4779-9c63-1464237dc087 -->

<!-- slide-id: new-framework-comparison -->

# Framework Comparison - Honest Take

| Framework | Language | Strength | Weakness |
|-----------|----------|----------|----------|
| **Django** | Python | Admin, ORM, batteries | Can feel heavy |
| **Laravel** | PHP | Elegant DX, ecosystem | PHP's reputation |
| **Rails** | Ruby | Convention over config | Ruby less popular now |
| **Express** | JS | Minimal, flexible | DIY everything |
| **Next.js** | JS | React SSR, edge | Full-stack is new |
| **FastAPI** | Python | Speed, async, types | No admin, minimal |
| **No framework** | Any | Full control | Full responsibility |

*There's no "best." Only "best for this job."*

---

<!-- slide-id: e406985c-34aa-4deb-b7ec-0cb7855e02d1 -->

<!-- slide-id: new-when-django -->

# When Django?

**Django excels when:**

- **Data-heavy CRUD** - Forms, models, relationships
- **Admin panel needed** - Non-technical users need access
- **Python ecosystem** - ML, data science, scripting
- **Rapid prototyping** - Get to MVP fast
- **Content sites** - Blogs, CMS, wikis
- **Multi-tenant apps** - SaaS platforms

**Django's DNA:** Collect, organize, and serve data.

---

<!-- slide-id: 523946fe-7aa3-45e8-8a87-f51a56bbde90 -->

<!-- slide-id: new-right-tool -->

# Right Tool for the Job

**When NOT Django:**

| Need | Better Choice | Why |
|------|---------------|-----|
| Real-time heavy | Node.js, Elixir | Event loop, channels |
| Edge computing | Next.js, Remix | Edge runtime support |
| Pure microservice | FastAPI, Go | Lighter footprint |
| Extreme throughput | Go, Rust | Raw performance |
| Mobile app backend | Firebase, Supabase | Built-in SDKs |
| Static site | Hugo, Astro | No server needed |

*Using Django for everything is like using a hammer for screws.*

---

<!-- slide-id: 575c11c8-05a3-46f8-a77c-6270de99455d -->

<!-- slide-id: new-django-vs-laravel -->

# Django vs Laravel - Quick Gist

| Aspect | Django | Laravel |
|--------|--------|---------|
| **Language** | Python | PHP |
| **Philosophy** | Explicit, batteries included | Elegant, expressive |
| **ORM** | Django ORM (tight integration) | Eloquent (beautiful API) |
| **Admin** | Free, built-in | Nova (paid) or Filament |
| **Ecosystem** | DRF, Celery, Channels | Forge, Vapor, Livewire |
| **Learning** | Steeper, more concepts | Smoother onboarding |

**Both are excellent.** Django has free admin + data-centric DNA.
Laravel has DX focus + modern PHP renaissance.

*Pick based on your team's language preference.*

---

<!-- slide-id: 203bc6fa-3f29-4ca5-96df-37b8ac5da920 -->

# What Django Gives You

- **ORM** - Think in Python, not SQL
- **Admin Panel** - Free CRUD interface for your data
- **Auth System** - Battle-tested, extensible
- **Migrations** - Version control for your database
- **"Batteries Included"** - Everything you need, nothing you don't

---

<!-- slide-id: 4a873e7b-2421-473b-9b06-6a6357bc25c9 -->

<!-- slide-id: new-design-philosophy -->

# Django's Design Philosophy

**The Zen of Django:**

| Principle | Meaning |
|-----------|---------|
| **Explicit > Implicit** | No magic. You know what's happening. |
| **DRY** | Don't Repeat Yourself. One source of truth. |
| **Loose Coupling** | Components work together, not dependent. |
| **Consistency** | Same patterns everywhere. Learn once, use everywhere. |
| **Less Code** | Do more with less. Framework handles boilerplate. |

*Django is opinionated so you don't have to make every decision.*

---

<!-- slide-id: 790391de-95ab-4bac-ad21-efa91f3b1f40 -->

<!-- _class: title-slide -->

# Block 1: Project Configuration

Setting up the foundation with `uv`

**Duration: ~22 minutes**

---

<!-- slide-id: f28d4ac7-5d4f-42b9-8125-8d1b6e27b63b -->

# Why uv?

**The modern Python package manager**

- **Fast** - Written in Rust, 10-100x faster than pip
- **Reliable** - Deterministic dependency resolution
- **All-in-one** - Replaces pip, venv, pip-tools, pyenv
- **Project-aware** - Manages virtual environments automatically

We'll use `uv` throughout this bootcamp.

---

<!-- slide-id: 5a2d1a2b-4390-4ee1-9026-2b347e31ffb5 -->

# Project Creation

**What we'll do:**

1. Initialize a new Python project with `uv`
2. Add Django as a dependency
3. Create the Django project structure
4. Create our first app: `prompts`

**Key insight:** `uv` handles the virtual environment for you. No more `source venv/bin/activate` dance.

---

<!-- slide-id: de146150-0301-488e-bac3-c1ac96f183a7 -->

# Project Structure

**After setup, you'll have:**

```
promptlab/
├── pyproject.toml      # Project config (uv manages this)
├── manage.py           # Django CLI entry point
├── promptlab/
│   ├── settings.py     # The brain of your project
│   ├── urls.py         # URL routing
│   └── wsgi.py         # Server interface
└── prompts/
    ├── models.py       # Your data schemas
    ├── views.py        # Your logic
    └── admin.py        # Admin configuration
```

---

<!-- slide-id: 628087c5-7aee-4db1-b96c-41bfe137c799 -->

# settings.py - The Control Center

**Key sections we'll configure:**

| Setting | Purpose |
|---------|---------|
| `SECRET_KEY` | Cryptographic signing (never commit!) |
| `DEBUG` | Development vs Production mode |
| `INSTALLED_APPS` | Which apps are active |
| `DATABASES` | Database connections |
| `STATIC/MEDIA` | Asset handling |

---

<!-- slide-id: a821f9fb-58e5-4944-9856-eaedc8bea0c5 -->

# Environment Variables

**Why?**
- Keep secrets out of code
- Different configs for dev/staging/prod
- 12-factor app compliance

**What we'll configure:**
- `SECRET_KEY` - From `.env` file
- `DEBUG` - Toggle for environments
- Database credentials
- S3/MinIO credentials

---

<!-- slide-id: a497fd57-06e5-49f3-b6d8-01438e6f1e20 -->

# Database Configuration

**Development:** SQLite
- Zero configuration
- File-based, perfect for local dev
- Ships with Python

**Production:** PostgreSQL
- Battle-tested at scale
- Rich features (JSON fields, full-text search)
- Same ORM code works for both!

---

<!-- slide-id: 6236428a-e6be-4ef6-9300-acad4652ede6 -->

# S3 / MinIO Storage

**The Strategy:**
- **Locally:** MinIO (S3-compatible, runs on your laptop)
- **Production:** AWS S3, Supabase Storage, or any S3-compatible service

**Why this matters:**
- Same code, different environments
- Just change the endpoint URL
- User uploads go to object storage, not your server

---

<!-- slide-id: fc677573-0275-4857-adec-b7a1f0d3ccae -->

# Static vs Media Files

| Type | What | Example |
|------|------|---------|
| **Static** | Your app's assets | CSS, JS, images in your repo |
| **Media** | User uploads | Profile pictures, attachments |

**Static:** Collected and served (often via CDN)
**Media:** Stored in S3/MinIO, served via signed URLs

---

<!-- slide-id: dbb3266c-572e-4281-ad2e-8b48762dd41b -->

# Installed Apps

**We'll register:**
- `rest_framework` - Django REST Framework
- `knox` - Token authentication
- `storages` - S3 backend
- `allauth` - User management
- `prompts` - Our app

**Order matters!** Django loads apps in sequence.

---

<!-- slide-id: d8d1dd8d-3489-482c-a53c-41f422bb613d -->

<!-- slide-id: new-allauth-overview -->

# django-allauth Overview

**What it gives you:**
- Registration, login, logout
- Email verification
- Password reset flow
- Social auth (Google, GitHub, etc.)
- Account management pages

**All with templates you can override.**

---

<!-- slide-id: 733b3ddb-bce8-42ca-8f31-ae399eca14de -->

<!-- slide-id: new-allauth-template-overrides -->

# Template Overrides

**The pattern:**
1. Create `templates/account/` directory
2. Copy allauth templates you want to customize
3. Style with Kairo CSS (or just use defaults!)
4. Your templates take precedence

**Override only what you need.**

---

<!-- slide-id: 2df940b4-29e5-4e89-b001-9e7ad4c3e704 -->

<!-- _class: title-slide -->

# Break Time

**5 minutes - Hydrate and stretch**

*Next: Models - The Data Schema*

---

<!-- slide-id: 3e847666-101f-46ad-8cd6-1bc66f55272c -->

<!-- _class: title-slide -->

# Block 2: Models

Defining your data schema

**Duration: ~30 minutes**

---

<!-- slide-id: ed35482e-7523-4a17-b308-fcaa3d92dec7 -->

# Django ORM Philosophy

**Models = Tables**
**Python = SQL**

You describe your data in Python classes.
Django translates that to database tables.

**Benefits:**
- Database-agnostic (switch from SQLite to Postgres freely)
- Migrations track every schema change
- Querysets are lazy and chainable
- Relationships feel natural

---

<!-- slide-id: c3bc59a5-5782-472d-8bd1-6e634ff7b1cf -->

# The Prompt Model

**What it stores:**
- Which **user** created it
- **Title** and **content** of the prompt
- **Expected output** (optional)
- **Timestamps** (created, updated)

**Key concept:** `ForeignKey` to User = "belongs to a user"

---

<!-- slide-id: edc0816d-0179-4963-949d-b310aa5ee452 -->

# The Attachment Model

**What it stores:**
- Which **prompt** it belongs to
- The **file** itself (stored in S3)
- Original **filename**
- Upload **timestamp**

**Key insight:** `FileField` with S3 backend = files go directly to your bucket.

---

<!-- slide-id: 7e05b307-a930-4fdd-b4b6-be80ef232c4a -->

# The Vote Model

**What it stores:**
- Which **user** voted
- Which **prompt** they voted on
- **Value**: +1 (upvote) or -1 (downvote)
- **Timestamp**

**Constraint:** One vote per user per prompt (unique together)

---

<!-- slide-id: d75fe184-eddb-4b6a-b7da-15e368ad85d2 -->

# The Comment Model

**What it stores:**
- Which **user** commented
- Which **prompt** they commented on
- The **content** of the comment
- **Timestamps** (created, updated)

**Ordering:** Newest first by default

---

<!-- slide-id: 113c11fa-1bc8-4df1-9eed-5faa59b9b703 -->

# Model Relationships

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

**This is why Django excels at data-centric apps.**

---

<!-- slide-id: 1f5a6f6d-79ef-40e7-9fe1-f8e309498b4e -->

# Key Relationship Concepts

| Concept | Meaning |
|---------|---------|
| `ForeignKey` | Many-to-One relationship |
| `related_name` | Reverse lookup name |
| `on_delete=CASCADE` | Delete children when parent deleted |
| `unique_together` | Compound unique constraint |

---

<!-- slide-id: d313b4ab-96a2-44f7-a4fb-2760db804a53 -->

# Migrations

**What they are:**
- Version control for your database schema
- Generated automatically from model changes
- Applied incrementally

**The workflow:**
1. Change your models
2. Generate migration files
3. Apply migrations to database

**Migrations are checked into git.** Your schema history travels with your code.

---

<!-- slide-id: 12fe3060-5929-4e61-a725-dd247078fa4c -->

# Django Admin

**What you get for free:**
- Full CRUD interface for all your models
- Search, filter, sort
- Bulk actions
- User management

**Just register your models** and you have a complete back-office tool.

*This alone saves weeks of development time.*

---

<!-- slide-id: 8f8d146a-07b3-4c0b-841b-a526aa95b3ae -->

<!-- slide-id: new-why-admin-matters -->

# Why Admin Panel Matters

**More than just CRUD:**

- **Free back-office** - Customer support can access data
- **Non-technical users** - Product managers, ops, marketing
- **Production-ready** - Permissions, audit logs, search
- **Quick debugging** - See what's in your database
- **Client demos** - Show data without building UI

**Every Django project gets this for free.** Laravel Nova costs $199/year.

---

<!-- slide-id: c4786bed-eaee-4465-9459-429a9db52968 -->

<!-- slide-id: new-orm-deep-dive -->

# ORM Deep Dive

**Key concepts:**

| Concept | What It Means |
|---------|---------------|
| **Lazy Querysets** | Query doesn't run until you need data |
| **Chainable** | `.filter().exclude().order_by()` |
| **Managers** | Custom query methods on models |
| **select_related** | JOIN in one query (ForeignKey) |
| **prefetch_related** | Separate query, Python join (M2M) |
| **F() expressions** | Database-level operations |
| **Q() objects** | Complex OR/AND queries |

---

<!-- slide-id: c12b2269-8359-4ea2-9e4a-2bb6a782dbd0 -->

<!-- slide-id: new-query-optimization -->

# Query Optimization - I Learned This the Hard Way

| Problem | Symptom | Solution |
|---------|---------|----------|
| **N+1 queries** | Slow page loads | `select_related`, `prefetch_related` |
| **Fetching unused fields** | High memory | `.only()`, `.defer()` |
| **Large result sets** | Timeout | Pagination, `.iterator()` |
| **Missing indexes** | Slow filters | `db_index=True`, compound indexes |
| **No caching** | Repeated queries | Django cache, `@cached_property` |
| **Fat models** | Complex logic | Move to services/managers |

*Profile with Django Debug Toolbar. Always.*

---

<!-- slide-id: 8f2a2bd3-a547-430d-b022-dd491dfaa0a6 -->

<!-- slide-id: new-common-pitfalls -->

# Common ORM Pitfalls

**Mistakes I've made (so you don't have to):**

- **Querying in loops** - Use `prefetch_related` instead
- **Forgetting `select_related`** - Every ForeignKey access = new query
- **Not indexing filter fields** - Database scans entire table
- **Calling `.count()` after `.all()`** - Two queries instead of one
- **Using `.get()` without try/except** - Crashes on missing data
- **Saving in loops** - Use `bulk_create`, `bulk_update`

*The ORM is powerful. But power requires responsibility.*

---

<!-- slide-id: 0c9418d1-6f7f-455c-98bd-b2a6d0d9f735 -->

<!-- _class: title-slide -->

# Break Time

**5 minutes - Hydrate and stretch**

*Next: Django REST Framework*

---

<!-- slide-id: 1822aae9-49e3-4e83-837f-a7a68e981320 -->

<!-- _class: title-slide -->

# Block 3: Django REST Framework

Turning your models into APIs

**Duration: ~30 minutes**

---

<!-- slide-id: f2942b2f-7058-4d89-8e58-6724ac0ed3da -->

# What is DRF?

**Django REST Framework** = Django's API toolkit

**What it gives you:**
- **Serializers** - Model to JSON translation
- **ViewSets** - CRUD in one class
- **Routers** - Automatic URL generation
- **Browsable API** - Test in your browser
- **Auth & Permissions** - Built-in security

---

<!-- slide-id: f599288d-2d13-4d61-a351-dea2aaa8fa5e -->

# Without DRF vs With DRF

**Without DRF:**
- Write JSON responses manually
- Validate input yourself
- Build pagination from scratch
- Handle errors case by case

**With DRF:**
- Declare your serializer
- Declare your viewset
- Everything else is automatic

---

<!-- slide-id: 2f4502c8-ea8c-4b7f-965f-16fb0ceec739 -->

# Serializers

**What they do:**
- Convert Model instances to JSON (serialization)
- Convert JSON to Model instances (deserialization)
- Validate incoming data
- Handle nested relationships

**Think of them as:** The contract between your API and the outside world.

---

<!-- slide-id: d6eb833b-54c4-4e2a-baf4-c7ffc32172d2 -->

# Serializer Types

| Type | Use Case |
|------|----------|
| `Serializer` | Full manual control |
| `ModelSerializer` | Auto-generates from model |
| Nested Serializers | Include related data |

**We'll use `ModelSerializer`** - it reads your model and creates fields automatically.

---

<!-- slide-id: 4f959061-c737-4eee-91cd-fc1546fb3cae -->

# ViewSets

**What they do:**
- Combine related views into one class
- Handle list, create, retrieve, update, delete
- `ModelViewSet` gives you full CRUD

**Key methods:**
- `get_queryset()` - What data to return
- `get_serializer_class()` - Which serializer to use
- `perform_create()` - Custom creation logic

---

<!-- slide-id: e83b39a9-fc1a-4965-9f9c-d43f3e80e5f8 -->

# Routers

**What they do:**
- Auto-generate URL patterns from ViewSets
- RESTful conventions out of the box

**Result:**
```
GET    /api/prompts/      → List
POST   /api/prompts/      → Create
GET    /api/prompts/1/    → Retrieve
PUT    /api/prompts/1/    → Update
DELETE /api/prompts/1/    → Delete
```

---

<!-- slide-id: 2d8ef04e-a994-495e-aa4c-9012599aa3f1 -->

# The Browsable API

**DRF's killer feature:**

- Visit your API in a browser
- See formatted JSON responses
- Test POST/PUT/DELETE with forms
- Authenticate and test protected endpoints

**Perfect for development and debugging.**

---

<!-- slide-id: 66def6d3-0acf-4bfd-98ce-5a3bd1d43569 -->

# API Testing Options

| Tool | Type | Best For |
|------|------|----------|
| Browser | GUI | Quick exploration |
| curl | CLI | Scripts, automation |
| httpie | CLI | Human-friendly CLI |
| Postman | GUI | Complex workflows |
| DRF Browser | Built-in | Development |

---

<!-- slide-id: 811db5eb-25e3-4560-9f84-201809048a20 -->

<!-- _class: title-slide -->

# Break Time

**5 minutes - Hydrate and stretch**

*Next: Knox Authentication*

---

<!-- slide-id: 91fd2b5a-7249-4fcd-9ee7-7a9ab7579ac5 -->

<!-- _class: title-slide -->

# Block 4: Knox Authentication

Secure token-based auth

**Duration: ~30 minutes**

---

<!-- slide-id: 3b744e9c-b66a-49aa-86cd-e3eea1e1d25f -->

# Authentication Options

| Method | How It Works |
|--------|--------------|
| **Session** | Cookie-based, server stores state |
| **Basic Auth** | Username:password every request |
| **JWT** | Stateless tokens, complex refresh |
| **DRF Token** | One token per user, no expiry |
| **Knox** | Multiple tokens, expiry, encrypted |

---

<!-- slide-id: e9d9c54d-014f-4a88-a726-2a3d0620d592 -->

# Why Knox?

**DRF's built-in TokenAuthentication:**
- One token per user, forever
- Stored in plain text
- No expiration
- Can't revoke individual sessions

---

<!-- slide-id: 1fb3c8f5-2008-4366-b1b6-3973750a3c2c -->

**Knox:**
- Multiple tokens per user
- Token expiration
- Encrypted storage
- Revoke individual or all tokens

---

<!-- slide-id: ab1f6981-0293-4310-865d-5a8ef6c9c0ec -->

# Knox Token Model

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

<!-- slide-id: ec7431c0-31d2-40f6-b586-a77526334a9a -->

# Knox Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/auth/login/` | Get a new token |
| `/auth/logout/` | Revoke current token |
| `/auth/logoutall/` | Revoke ALL user tokens |

**LogoutAll is your security breach response button.**

---

<!-- slide-id: 3576a2b9-d769-4bc3-8af7-6b09ccc9ce87 -->

# Token Flow

1. **Login** - Send username/password, get token
2. **Store** - Save token (localStorage, secure storage)
3. **Use** - Send token in `Authorization` header
4. **Logout** - Invalidate token on server

**The token is your proof of identity.**

---

<!-- slide-id: f90b7aaf-b927-4125-8cd6-42d5de7cf09f -->

# Protected Endpoints

**Permission classes control access:**

| Permission | Meaning |
|------------|---------|
| `AllowAny` | No auth required |
| `IsAuthenticated` | Must have valid token |
| `IsAuthenticatedOrReadOnly` | Read = open, write = auth |
| `IsOwner` | Only owner can modify |

---

<!-- slide-id: 79360124-3774-4bb5-9cba-3eadb321a921 -->

# Custom Permissions

**The pattern:**
1. Check if it's a "safe" method (GET, HEAD, OPTIONS)
2. If safe, allow
3. If not safe, check ownership

**Example:** Anyone can read prompts. Only the creator can edit/delete.

---

<!-- slide-id: bb4d0ce1-c0fe-4a25-a125-50a571df125c -->

# Token Expiration

**Configure based on your needs:**

| Use Case | TTL |
|----------|-----|
| High security | 1 hour |
| Normal web app | 24 hours |
| Mobile app | 7-30 days |
| Remember me | 90 days |

**Expired tokens are automatically rejected.**

---

<!-- slide-id: dbc64d93-0df7-4046-99cd-25e580e3face -->

<!-- _class: title-slide -->

# Break Time

**5 minutes - Hydrate and stretch**

*Next: Frontend with Templates + Kairo CSS + Alpine*

---

<!-- slide-id: 2ad64af1-953e-4fad-b40d-4c3a82a2a54f -->

<!-- _class: title-slide -->

# Block 5: Frontend

Django Templates + Kairo CSS + Alpine.js

**Duration: ~30 minutes**

---

<!-- slide-id: 9acfd6dd-5025-4468-a359-0fdec27b91e3 -->

# The Frontend Stack

| Tool | Purpose |
|------|---------|
| **Django Templates** | Server-rendered HTML |
| **Kairo CSS** | Classless semantic styling |
| **Alpine.js** | Lightweight reactivity |

**No build step. No npm. No webpack. No classes to memorize.**

---

<!-- slide-id: 6a9ec2d8-b04c-4118-967c-623c7ada04be -->

# Django Templates

**Django's built-in templating engine:**
- Similar to Jinja2
- Template inheritance (base → child)
- Filters and tags
- Context variables from views

**Perfect for:** Server-rendered pages with sprinkles of interactivity.

---

<!-- slide-id: ce99556f-fef2-4a62-ab59-a8499d7bd092 -->

# Template Inheritance

```
base.html (master layout)
    │
    ├── Header, Navigation, Footer
    ├── Scripts (Kairo CSS, Alpine)
    │
    └── {% block content %} (child fills this)
            │
            ├── prompts/list.html
            ├── prompts/detail.html
            └── accounts/login.html
```

**DRY principle in action.**

---

<!-- slide-id: f40fe908-62af-4d64-af35-8ea17ce4b8fa -->

# Kairo CSS

**Classless CSS framework for semantic HTML:**
- Write semantic HTML, get beautiful defaults
- No classes to memorize or look up
- Single file, under 15KB
- Just set `--primary` and `--secondary` colors
- Dark mode built-in

**Philosophy:** *"Good design is as little design as possible."*

---

<!-- slide-id: c4b9c7ab-abd8-4522-95c4-a02a83b497e9 -->

# Why Kairo CSS for Django?

- **Zero classes** - Write HTML, get styling
- **Semantic HTML** - Django templates stay clean
- **Single import** - One CSS file via CDN
- **Customizable** - Just change CSS variables
- **Perfect for prototypes** - Focus on data, not design

[kairocss.nnisarg.in](https://kairocss.nnisarg.in/)

---

<!-- slide-id: 6bceaf45-8f39-4da7-8c57-87aa50f09755 -->

# Alpine.js

**Reactivity without React:**
- 15kb, no build step
- Declare behavior in HTML attributes
- Works with server-rendered pages
- Perfect for "islands of interactivity"

**The jQuery of the modern era, but better.**

---

<!-- slide-id: 1564f3b1-4878-42fe-a0f3-67d99e0a6274 -->

# Alpine.js Concepts

| Directive | Purpose |
|-----------|---------|
| `x-data` | Component state |
| `x-show` | Toggle visibility |
| `x-for` | Loop over items |
| `x-model` | Two-way binding |
| `@click` | Event handling |
| `x-text` | Set text content |

---

<!-- slide-id: 61de38a0-1c8d-4ecb-812d-9c3fa9564368 -->

# The Pattern

1. **Django serves the page** (template)
2. **Alpine handles interactivity** (client-side)
3. **Fetch calls your DRF API** (data)
4. **Alpine updates the DOM** (reactivity)

**Server-rendered shell + API-driven content.**

---

<!-- slide-id: fef8df46-56e8-4161-8c50-32d7db65c654 -->

# Why This Stack?

| Concern | Solution |
|---------|----------|
| SEO | Server-rendered HTML |
| Interactivity | Alpine.js |
| Styling | Kairo CSS (classless) |
| Data | DRF API |
| Auth | Knox tokens in localStorage |

**Full-stack Django without the SPA complexity.**

---

<!-- slide-id: cab3957a-427e-46fe-a629-24adf49d98f4 -->

# The Full Stack Loop

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

<!-- slide-id: 75a0096f-5ff9-47e6-ac31-4cd508b17181 -->

<!-- _class: title-slide -->

# Break Time

**5 minutes - Hydrate and stretch**

*Next: Assignment + Closing*

---

<!-- slide-id: aa0d92c6-b673-4c00-a057-9de5049e9ea9 -->

<!-- _class: title-slide -->

# Assignment

Your turn to build.

---

<!-- slide-id: 7b49a626-c057-4ca7-ad79-286fed3ae0e1 -->

# The Timeline

| Phase | Duration |
|-------|----------|
| **Build** | 1 week from today |
| **Evaluation** | Week 2 |
| **Certificates** | Mailed after evaluation |

**Personalized certificates** with a message from me, mailed to your registered email.

---

<!-- slide-id: b2b79d7d-46ec-40ca-bf88-e60a461fc635 -->

# The Challenge

**Build something that solves a real problem.**

- Could be useful
- Could be stupid
- Could be something I can't even relate to

**The only rule:** It must solve *your* problem.

Your problem. Your solution. Your project.

---

<!-- slide-id: d2f7a50d-eb24-4002-bf4e-d821335c1a0f -->

# Project Ideas (If You Need Inspiration)

| Category | Ideas |
|----------|-------|
| **Everyday** | Grocery tracker, Bill splitter, Medicine reminder, Wardrobe logger |
| **Student/Dev** | Assignment tracker, Bug journal, Side project graveyard, Resource hoarder |
| **Niche/Fun** | Plant watering log, Dream journal, Shower thought archive, Excuse tracker |

*Or build something completely different. It's your call.*

---

<!-- slide-id: 25145b66-b997-4b6b-8297-6333990590c8 -->

<!-- slide-id: new-django-ecosystem -->

# Django's Ecosystem

**The packages that make Django unstoppable:**

| Package | Purpose |
|---------|---------|
| **Django REST Framework** | Build APIs in minutes |
| **Celery** | Background tasks, scheduled jobs |
| **Channels** | WebSockets, real-time |
| **Wagtail** | CMS built on Django |
| **django-debug-toolbar** | Query profiling, debugging |
| **django-extensions** | Shell plus, better commands |
| **whitenoise** | Static file serving |
| **django-storages** | S3, Azure, GCS backends |
| **django-allauth** | Auth flows, social login |
| **django-filter** | Queryset filtering from URL params |

*The ecosystem is mature. Whatever you need, someone built it.*

---

<!-- slide-id: ab427709-5a7e-4c90-a6a5-5a9af1d70f8e -->

# Requirements

| Requirement | Details |
|-------------|---------|
| **Models** | Minimum 3 related models with proper relationships |
| **API** | DRF endpoints for your data |
| **Auth** | Knox or django-allauth |
| **Frontend** | Templates + Kairo CSS + Alpine.js |
| **Git** | Must be in a Git repository (any provider) |
| **README** | Explain what problem it solves |

---

<!-- slide-id: 854300e2-27f4-4fb9-a887-f771e2e77234 -->

# What Makes an Excellent Submission

| Level | Description |
|-------|-------------|
| **Good** | It works. Meets requirements. Has a README. |
| **Great** | Clean code. Clear problem statement. Thoughtful model design. |
| **Excellent** | Creative problem. Goes beyond minimum. Shows the "collect data now, insights later" mindset. |

---

<!-- slide-id: ccd18d51-74ae-4d3d-9a1e-1ccb9aec2ac1 -->

# How to Submit

1. Push your code to **any Git provider**
   - GitHub, GitLab, Codeberg, or even private repos
   - If private, add access for evaluation (details in WhatsApp)

2. Submit repo link via **Google Form**
   - Link will be shared in WhatsApp group

3. **Deadline:** 1 week from today

**NO ZIP FILES.** Git or nothing.

---

<!-- slide-id: 624db5a8-a0d7-4591-8f81-b6f3002d38bc -->

# Certificate

Upon valid submission, you'll receive:

- **Personalized certificate** confirming bootcamp completion
- **Personal message** from me
- Mailed to your **registered email** after evaluation week

*Build something. Ship it. Get recognized.*

---

<!-- slide-id: 18e2f358-716f-4854-b5f8-a7465b0731fb -->

# Resources

**Documentation:**
- Django: [docs.djangoproject.com](https://docs.djangoproject.com)
- DRF: [django-rest-framework.org](https://www.django-rest-framework.org)
- Knox: [github.com/jazzband/django-rest-knox](https://github.com/jazzband/django-rest-knox)
- uv: [docs.astral.sh/uv](https://docs.astral.sh/uv)
- Kairo CSS: [kairocss.nnisarg.in](https://kairocss.nnisarg.in/)
- Alpine.js: [alpinejs.dev](https://alpinejs.dev)

---

<!-- slide-id: b637e900-3ed9-434f-9890-57b6cc1dbae6 -->

# BroCode Resources

- **GitHub:** [github.com/BroCode501](https://github.com/BroCode501)
- **Blog:** [bromine.vercel.app](https://bromine.vercel.app)
- **Events:** [Event Horizon](https://events.neopanda.tech)
- **WhatsApp:** Link in registration email

---

<!-- slide-id: 234d6708-c465-4db0-9ee9-26bd94ebaea5 -->

<!-- _class: title-slide -->
<!-- _paginate: false -->

# Thank You!

**You now have the foundation to build data-centric applications.**

Collect data now. Build analytics later.
*Just like Instagram. Just like Spotify.*

---

<!-- slide-id: fcaeb4f6-63b4-43eb-a8dc-e0b3a673900b -->

**Arnav Ghosh**
Founder, BroCode Tech Community

GitHub: [@NotoriousArnav](https://github.com/NotoriousArnav)
Event: [events.neopanda.tech](https://events.neopanda.tech/events/django-101)

![w:150](logo.jpg)