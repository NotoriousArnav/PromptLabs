# Assignment

Your turn to build.

---

## The Timeline

| Phase | Duration |
|-------|----------|
| **Build** | 1 week from today |
| **Evaluation** | Week 2 |
| **Certificates** | Mailed after evaluation |

**Personalized certificates** with a message from Arnav, mailed to your registered email.

---

## The Challenge

**Build something that solves a real problem.**

- Could be useful
- Could be stupid
- Could be something no one else can relate to

**The only rule:** It must solve *your* problem.

Your problem. Your solution. Your project.

---

## Requirements

| Requirement | Details |
|-------------|---------|
| **Models** | Minimum 3 related models with proper relationships |
| **API** | DRF endpoints for your data |
| **Auth** | Knox or django-allauth |
| **Frontend** | Templates + Kairo CSS + Alpine.js |
| **Git** | Must be in a Git repository (any provider) |
| **README** | Explain what problem it solves |

---

## Project Ideas (If You Need Inspiration)

| Category | Ideas |
|----------|-------|
| **Everyday** | Grocery tracker, Bill splitter, Medicine reminder, Wardrobe logger |
| **Student/Dev** | Assignment tracker, Bug journal, Side project graveyard, Resource hoarder |
| **Niche/Fun** | Plant watering log, Dream journal, Shower thought archive, Excuse tracker |

*Or build something completely different. It's your call.*

---

## What Makes an Excellent Submission

| Level | Description |
|-------|-------------|
| **Good** | It works. Meets requirements. Has a README. |
| **Great** | Clean code. Clear problem statement. Thoughtful model design. |
| **Excellent** | Creative problem. Goes beyond minimum. Shows the "collect data now, insights later" mindset. |

---

## Model Design Tips

### Think About Relationships

```
User
  ├── owns many → [Your Main Entity]
  │     ├── has many → [Related Entity 1]
  │     └── has many → [Related Entity 2]
  └── owns many → [Related Entity 2]
```

### Example: Grocery Tracker

```
User
  ├── GroceryList (one user → many lists)
  │     └── GroceryItem (one list → many items)
  └── Store (one user → many stores)
        └── GroceryItem.store (many items → one store)
```

### Example: Bug Journal

```
User
  ├── Bug (one user → many bugs)
  │     ├── Tag (many-to-many)
  │     └── Solution (one bug → many solutions)
  └── Tag (one user → many tags)
```

---

## README Template

```markdown
# [Project Name]

## Problem Statement

[What problem does this solve? Why did you build it?]

## Features

- Feature 1
- Feature 2
- Feature 3

## Tech Stack

- Django + DRF
- Knox Authentication
- Kairo CSS
- Alpine.js

## Models

[Brief description of your data models and relationships]

## Setup

```bash
# Clone the repo
git clone [your-repo-url]
cd [project-name]

# Install dependencies
uv sync

# Run migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Run server
uv run python manage.py runserver
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/...` | GET | ... |

## Screenshots

[Optional: Add screenshots]

## Author

[Your Name]
```

---

## How to Submit

### Step 1: Push to Git

Push your code to **any Git provider**:
- GitHub
- GitLab
- Codeberg
- Bitbucket
- Or any other Git hosting

**If your repo is private**, you'll need to add access for evaluation (details will be shared in WhatsApp).

### Step 2: Submit via Google Form

- Link will be shared in WhatsApp group
- Include your repo URL
- Include your registered email

### Step 3: Wait for Evaluation

- Evaluation happens in Week 2
- You'll receive feedback via email
- Certificate mailed after successful evaluation

---

## Submission Checklist

Before submitting, make sure you have:

- [ ] **3+ related models** with proper relationships
- [ ] **DRF API endpoints** for CRUD operations
- [ ] **Authentication** (Knox or allauth)
- [ ] **Frontend** with Django Templates + Kairo CSS + Alpine.js
- [ ] **README.md** explaining the problem and setup
- [ ] **Git repository** (not a ZIP file!)
- [ ] **Working application** (can run with provided instructions)

---

## Common Mistakes to Avoid

1. **ZIP files** - Must be a Git repository
2. **No README** - We need to know what it does
3. **Broken setup** - Test your setup instructions
4. **Missing migrations** - Commit your migration files
5. **Hardcoded secrets** - Use environment variables
6. **No relationships** - Models should be connected
7. **Copied code without understanding** - Build something original

---

## Tips for Success

### Start Simple

Don't try to build Instagram on day one. Start with:
1. Define your models
2. Create migrations
3. Set up admin
4. Build basic API
5. Add frontend
6. Polish and document

### Test Your Setup

After pushing to Git, try to clone and set up from scratch:

```bash
# Clone fresh
git clone [your-repo]
cd [project]

# Follow your own README
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

If it works for you from scratch, it'll work for evaluation.

### Ask for Help

- Use the WhatsApp group
- Ask specific questions
- Share error messages
- Help others too!

---

## Certificate

Upon valid submission, you'll receive:

- **Personalized certificate** confirming bootcamp completion
- **Personal message** from Arnav
- Mailed to your **registered email** after evaluation week

*Build something. Ship it. Get recognized.*

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

## Deadline

**1 week from bootcamp date**

**NO EXTENSIONS.** Ship what you have.

---

## Final Words

This bootcamp gave you the foundation. The assignment is where you prove you can build.

**The best way to learn is to build.**

Don't overthink it. Don't over-engineer it. Just build something that works and solves a real problem.

Good luck!

— Arnav
