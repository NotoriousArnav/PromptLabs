# BroCode Protocols: Django & API Bootcamp

## Course Overview

Welcome to the Django & API Bootcamp! This course teaches you how to build **data-centric applications** using Django - the same framework that powers Instagram, Pinterest, and Disqus.

### What You'll Walk Away With

- A working understanding of **Django's data-centric approach**
- **PromptLab** - a complete reference project you can learn from
- An **assignment** to build your own project (1 week)
- **Personalized certificate** upon successful submission

---

## Why Django?

### The Data-Centric Philosophy

Django excels at applications that **collect, organize, and serve data**. Think:
- Instagram (photos)
- Spotify (music catalogs)
- Pinterest (pins and boards)

**The mindset:** Collect data now, build analytics later.

### What Django Gives You

| Feature | Description |
|---------|-------------|
| **ORM** | Think in Python, not SQL |
| **Admin Panel** | Free CRUD interface for your data |
| **Auth System** | Battle-tested, extensible |
| **Migrations** | Version control for your database |
| **Batteries Included** | Everything you need, nothing you don't |

### Django's Design Philosophy

| Principle | Meaning |
|-----------|---------|
| **Explicit > Implicit** | No magic. You know what's happening. |
| **DRY** | Don't Repeat Yourself. One source of truth. |
| **Loose Coupling** | Components work together, not dependent. |
| **Consistency** | Same patterns everywhere. |
| **Less Code** | Framework handles boilerplate. |

---

## Django at Scale - Proof It Works

| Company | Scale | What They Do |
|---------|-------|--------------|
| **Instagram** | 2B+ users | Photo sharing, stories, reels |
| **Pinterest** | 450M+ users | Visual discovery engine |
| **Disqus** | 50M+ comments/month | Comment system |
| **Eventbrite** | 4M+ events/year | Event management |
| **Mozilla** | 100M+ users | Firefox add-ons, support |

---

## When to Use Django

**Django excels when:**
- Data-heavy CRUD operations
- Admin panel needed for non-technical users
- Python ecosystem integration (ML, data science)
- Rapid prototyping to MVP
- Content sites (blogs, CMS, wikis)
- Multi-tenant SaaS platforms

**When NOT Django:**

| Need | Better Choice | Why |
|------|---------------|-----|
| Real-time heavy | Node.js, Elixir | Event loop, channels |
| Edge computing | Next.js, Remix | Edge runtime support |
| Pure microservice | FastAPI, Go | Lighter footprint |
| Extreme throughput | Go, Rust | Raw performance |
| Mobile backend | Firebase, Supabase | Built-in SDKs |
| Static site | Hugo, Astro | No server needed |

---

## Framework Comparison

| Framework | Language | Strength | Weakness |
|-----------|----------|----------|----------|
| **Django** | Python | Admin, ORM, batteries | Can feel heavy |
| **Laravel** | PHP | Elegant DX, ecosystem | PHP's reputation |
| **Rails** | Ruby | Convention over config | Ruby less popular |
| **Express** | JS | Minimal, flexible | DIY everything |
| **Next.js** | JS | React SSR, edge | Full-stack is new |
| **FastAPI** | Python | Speed, async, types | No admin, minimal |

**There's no "best." Only "best for this job."**

---

## The Project: PromptLab

A data-centric application for storing and organizing AI prompts.

**Core Features:**
- Store prompts with attachments and expected outputs
- Upvotes, downvotes, and comments
- User authentication with Knox tokens
- S3-compatible storage (MinIO locally, AWS/Supabase in prod)

---

## Course Structure

| Block | Topic | Duration |
|-------|-------|----------|
| 1 | Project Configuration | ~22 min |
| 2 | Models | ~30 min |
| 3 | Django REST Framework | ~30 min |
| 4 | Knox Authentication | ~30 min |
| 5 | Frontend (Templates + Kairo CSS + Alpine.js) | ~30 min |

---

## Resources

### Documentation
- Django: [docs.djangoproject.com](https://docs.djangoproject.com)
- DRF: [django-rest-framework.org](https://www.django-rest-framework.org)
- Knox: [github.com/jazzband/django-rest-knox](https://github.com/jazzband/django-rest-knox)
- uv: [docs.astral.sh/uv](https://docs.astral.sh/uv)
- Kairo CSS: [kairocss.nnisarg.in](https://kairocss.nnisarg.in/)
- Alpine.js: [alpinejs.dev](https://alpinejs.dev)

### BroCode
- GitHub: [github.com/BroCode501](https://github.com/BroCode501)
- Blog: [bromine.vercel.app](https://bromine.vercel.app)
- Events: [events.neopanda.tech](https://events.neopanda.tech)

---

## Next Steps

Continue to [01-project-setup.md](./01-project-setup.md) to set up your Django project with `uv`.
