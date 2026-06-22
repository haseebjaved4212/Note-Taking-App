# 🎸 Django — Complete Reference

> A comprehensive, practical guide to Django — the high-level Python web framework. Covers project setup, models, views, templates, forms, admin, authentication, REST APIs, and deployment.

![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-18-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

---

## 📚 Table of Contents

1. [What is Django?](#1-what-is-django)
2. [Installation & Project Setup](#2-installation--project-setup)
3. [Project Structure](#3-project-structure)
4. [Settings](#4-settings)
5. [URLs & Routing](#5-urls--routing)
6. [Views — Function-Based](#6-views--function-based)
7. [Views — Class-Based](#7-views--class-based)
8. [Models & the ORM](#8-models--the-orm)
9. [Migrations](#9-migrations)
10. [QuerySets & ORM Queries](#10-querysets--orm-queries)
11. [Django Admin](#11-django-admin)
12. [Templates](#12-templates)
13. [Forms](#13-forms)
14. [Static Files & Media](#14-static-files--media)
15. [Authentication & Authorization](#15-authentication--authorization)
16. [Middleware](#16-middleware)
17. [Signals](#17-signals)
18. [Django REST Framework](#18-django-rest-framework)
19. [Testing](#19-testing)
20. [Deployment](#20-deployment)
21. [Best Practices](#21-best-practices)
22. [Quick Reference Cheat Sheet](#22-quick-reference-cheat-sheet)

---

## 1. What is Django?

Django is a **high-level Python web framework** that encourages rapid development and clean, pragmatic design. It follows the **batteries-included** philosophy — an ORM, admin panel, authentication system, form handling, and security features all ship with the framework out of the box.

### Core Philosophy

| Principle | Meaning |
|-----------|---------|
| **DRY** (Don't Repeat Yourself) | Define data models once, reuse everywhere |
| **Batteries included** | ORM, admin, auth, forms all built in |
| **Loose coupling** | Components (models, views, templates) are independent |
| **Convention over configuration** | Sensible defaults, less boilerplate |
| **Security by default** | CSRF protection, SQL injection prevention, XSS protection built in |

### Django's Architecture — MTV Pattern

Django follows **Model-Template-View (MTV)**, a variation of MVC.

```
┌─────────┐      ┌─────────┐      ┌──────────┐
│  Model  │ ───▶ │  View   │ ───▶ │ Template │
│ (data)  │      │ (logic) │      │  (HTML)  │
└─────────┘      └─────────┘      └──────────┘
     ▲                                   │
     │            Request/Response       │
     └───────────────────────────────────┘
```

| MTV Component | Equivalent in MVC | Responsibility |
|----------------|--------------------|--------------------|
| **Model** | Model | Data structure, database schema |
| **Template** | View | Presentation, HTML rendering |
| **View** | Controller | Business logic, connects model to template |

### Why Use Django?

```python
# Build a fully working blog backend in minutes
# - User authentication: built in
# - Admin panel to manage posts: built in
# - Database ORM: built in
# - Form validation: built in
# - Security (CSRF, XSS, SQLi protection): built in
```

---

## 2. Installation & Project Setup

### Installing Django

```bash
# Create a virtual environment first (always)
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install Django
pip install django

# Check version
python -m django --version
```

### Creating a Project

```bash
# Create a new Django project
django-admin startproject myproject
cd myproject

# Run the development server
python manage.py runserver

# Run on a specific port
python manage.py runserver 8080

# Run on all network interfaces (accessible from other devices)
python manage.py runserver 0.0.0.0:8000
```

### Creating an App

Django projects are made of **apps** — self-contained modules for a specific feature (blog, users, payments, etc).

```bash
python manage.py startapp blog
```

> [!NOTE]
> A **project** is the whole website. An **app** is a reusable module within it (e.g. `blog`, `accounts`, `payments`). A single project can contain many apps, and apps can be reused across projects.

### Registering the App

```python
# myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',   # 👈 your new app
]
```

---

## 3. Project Structure

```
myproject/
├── manage.py                  # CLI utility for admin tasks
├── myproject/                 # project configuration package
│   ├── __init__.py
│   ├── settings.py            # all project settings
│   ├── urls.py                # root URL configuration
│   ├── asgi.py                # ASGI entry point (async)
│   └── wsgi.py                # WSGI entry point (sync)
└── blog/                      # an app
    ├── migrations/            # database migration files
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py                # admin panel registration
    ├── apps.py                 # app configuration
    ├── models.py                # data models
    ├── tests.py                  # unit tests
    ├── views.py                   # request handlers
    └── urls.py                    # app-specific URLs (you create this)
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `manage.py` | Run commands: server, migrations, shell, tests |
| `settings.py` | Database config, installed apps, middleware, secret key |
| `urls.py` | Maps URL paths to views |
| `models.py` | Defines database tables as Python classes |
| `views.py` | Handles requests, returns responses |
| `admin.py` | Registers models to appear in the admin panel |
| `apps.py` | App-specific configuration |
| `wsgi.py` / `asgi.py` | Entry points for production servers |

---

## 4. Settings

`settings.py` is the control center of a Django project.

```python
# myproject/settings.py

# Security
SECRET_KEY = 'your-secret-key-here'   # NEVER commit this to version control
DEBUG = True                           # MUST be False in production
ALLOWED_HOSTS = []                     # required when DEBUG = False

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

# Middleware — order matters
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # global templates folder
        'APP_DIRS': True,                    # also look inside app/templates/
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

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
```

### Using Environment Variables for Secrets

```python
# settings.py — never hardcode secrets
import os
from pathlib import Path

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

> [!WARNING]
> Never commit `SECRET_KEY`, database passwords, or API keys to version control. Use environment variables or a `.env` file (with `python-decouple` or `django-environ`) and add `.env` to `.gitignore`.

### Database Engines

| Database | Engine String |
|----------|---------------|
| SQLite (default) | `django.db.backends.sqlite3` |
| PostgreSQL | `django.db.backends.postgresql` |
| MySQL | `django.db.backends.mysql` |
| Oracle | `django.db.backends.oracle` |

---

## 5. URLs & Routing

### Root URL Configuration

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),   # delegate to app's urls.py
    path('', include('core.urls')),
]
```

### App-Level URLs

```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'   # namespace for {% url %} tags

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/', views.post_by_slug, name='post_by_slug'),
    path('create/', views.post_create, name='post_create'),
]
```

### URL Path Converters

```python
path('articles/<int:year>/', views.year_archive),       # int
path('articles/<str:name>/', views.by_name),             # str (default)
path('articles/<slug:slug>/', views.by_slug),             # slug-formatted string
path('articles/<uuid:id>/', views.by_uuid),                # UUID
path('articles/<path:subpath>/', views.by_path),            # full URL path including /
```

| Converter | Matches | Example |
|-----------|---------|---------|
| `str` | Any non-empty string excluding `/` | `<str:name>` |
| `int` | Positive integers | `<int:pk>` |
| `slug` | Letters, numbers, hyphens, underscores | `<slug:slug>` |
| `uuid` | A formatted UUID | `<uuid:id>` |
| `path` | Any string, including `/` | `<path:subpath>` |

### Named URLs and Reverse Lookup

```python
# In templates
# <a href="{% url 'blog:post_detail' pk=post.id %}">Read more</a>

# In Python code
from django.urls import reverse
url = reverse('blog:post_detail', kwargs={'pk': 5})

# Redirect using a name
from django.shortcuts import redirect
def my_view(request):
    return redirect('blog:post_list')
```

### Using `re_path` for Regex Patterns

```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]
```

---

## 6. Views — Function-Based

A view is a Python function (or class) that takes a web request and returns a web response.

### Basic View

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def simple_response(request):
    return HttpResponse("Hello, Django!")

def json_response(request):
    return JsonResponse({'status': 'ok', 'message': 'Hello, API!'})
```

### Handling Different HTTP Methods

```python
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('blog:post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html')
```

### Request Object Essentials

```python
def view_example(request):
    request.method          # 'GET', 'POST', etc.
    request.GET              # query string parameters (?key=value)
    request.POST              # form data from POST request
    request.FILES               # uploaded files
    request.user                 # currently logged-in user
    request.session               # session data
    request.headers                # HTTP headers
    request.path                    # the URL path requested
    request.META                     # raw request metadata (headers, IP, etc.)
```

### Decorators for Function-Based Views

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import csrf_exempt

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@require_http_methods(["GET", "POST"])
def my_view(request):
    ...

@require_POST
def delete_post(request, pk):
    ...

@csrf_exempt   # use carefully — disables CSRF protection
def webhook_handler(request):
    ...
```

---

## 7. Views — Class-Based

Class-Based Views (CBVs) reduce boilerplate for common patterns like listing, detail pages, and forms.

### Generic Display Views

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
```

```python
# blog/urls.py
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
```

### Generic Editing Views

```python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
```

### Mixins — Adding Behavior to CBVs

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    login_url = '/login/'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user   # only the author can delete
```

### Customizing CBV Behavior

```python
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # Custom filtering logic
        return Post.objects.filter(published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured'] = Post.objects.filter(featured=True)[:3]
        return context
```

### Function-Based vs Class-Based Views

| Feature | Function-Based (FBV) | Class-Based (CBV) |
|---------|----------------------|---------------------|
| Readability | Explicit, linear | Compact, DRY |
| Reusability | Lower | Higher (inheritance, mixins) |
| Learning curve | Easier for beginners | Steeper initially |
| Best for | Custom one-off logic | CRUD, repeated patterns |
| Decorators | Easy to apply | Need mixins or `method_decorator` |

---

## 8. Models & the ORM

Models define your database schema as Python classes. Django's ORM converts them into SQL automatically.

### Basic Model

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)
    content     = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    published   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
```

### Common Field Types

| Field | Description | Example |
|-------|-------------|---------|
| `CharField` | Short text, requires `max_length` | `models.CharField(max_length=100)` |
| `TextField` | Long text, no length limit | `models.TextField()` |
| `IntegerField` | Whole numbers | `models.IntegerField()` |
| `FloatField` | Decimal numbers | `models.FloatField()` |
| `DecimalField` | Precise decimals (money) | `models.DecimalField(max_digits=10, decimal_places=2)` |
| `BooleanField` | True/False | `models.BooleanField(default=False)` |
| `DateField` | Date only | `models.DateField()` |
| `DateTimeField` | Date and time | `models.DateTimeField(auto_now_add=True)` |
| `EmailField` | Validated email string | `models.EmailField()` |
| `URLField` | Validated URL string | `models.URLField()` |
| `SlugField` | URL-friendly string | `models.SlugField(unique=True)` |
| `FileField` | File upload | `models.FileField(upload_to='files/')` |
| `ImageField` | Image upload (needs Pillow) | `models.ImageField(upload_to='images/')` |
| `ForeignKey` | Many-to-one relation | `models.ForeignKey(Author, on_delete=models.CASCADE)` |
| `ManyToManyField` | Many-to-many relation | `models.ManyToManyField(Tag)` |
| `OneToOneField` | One-to-one relation | `models.OneToOneField(User, on_delete=models.CASCADE)` |
| `UUIDField` | Universally unique ID | `models.UUIDField(default=uuid.uuid4)` |
| `JSONField` | Store JSON data | `models.JSONField(default=dict)` |

### Field Options

```python
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,        # required in forms
        null=False,          # required in database
        unique=True,           # no duplicates allowed
        db_index=True,           # creates a database index
        default='Untitled',        # default value
        help_text='Product name',    # shown in admin/forms
        verbose_name='Product Name',   # human-readable label
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)   # optional field
```

### Relationships

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=30)

class Article(models.Model):
    # Many-to-one — many articles, one author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')

    # Many-to-many — an article can have many tags, a tag many articles
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)

    # One-to-one — a profile belongs to exactly one user
    # profile = models.OneToOneField(User, on_delete=models.CASCADE)
```

### `on_delete` Options

| Option | Behavior |
|--------|----------|
| `CASCADE` | Delete related objects too |
| `PROTECT` | Prevent deletion if related objects exist |
| `SET_NULL` | Set the field to `NULL` (requires `null=True`) |
| `SET_DEFAULT` | Set the field to its default value |
| `SET()` | Set to a value returned by a callable |
| `DO_NOTHING` | Take no action (dangerous — can break referential integrity) |

### Model Methods & Properties

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def word_count(self):
        return len(self.content.split())

    @property
    def is_recent(self):
        return (timezone.now() - self.created_at).days < 7

    def summary(self, length=100):
        return self.content[:length] + '...' if len(self.content) > length else self.content
```

---

## 9. Migrations

Migrations are how Django propagates model changes into the database schema.

### Migration Workflow

```bash
# 1. Create migration files based on model changes
python manage.py makemigrations

# Create migrations for a specific app
python manage.py makemigrations blog

# 2. Apply migrations to the database
python manage.py migrate

# Apply migrations for a specific app
python manage.py migrate blog

# Show SQL that a migration will run (without applying it)
python manage.py sqlmigrate blog 0001

# List all migrations and their applied status
python manage.py showmigrations

# Undo a migration — roll back to a previous state
python manage.py migrate blog 0002

# Roll back ALL migrations for an app
python manage.py migrate blog zero
```

### Anatomy of a Migration File

```python
# blog/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
```

### Data Migrations

Sometimes you need to migrate data, not just schema.

```python
# Generate an empty migration to customize
# python manage.py makemigrations blog --empty --name populate_slugs

from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.slug = slugify(post.title)
        post.save()

class Migration(migrations.Migration):
    dependencies = [('blog', '0001_initial')]
    operations = [
        migrations.RunPython(populate_slugs),
    ]
```

> [!WARNING]
> Always commit migration files to version control. Never edit a migration that has already been applied in production — create a new migration instead.

---

## 10. QuerySets & ORM Queries

The Django ORM lets you query the database using Python instead of raw SQL.

### Creating Objects

```python
# Method 1 — create and save separately
post = Post(title="My First Post", content="Hello world")
post.save()

# Method 2 — create() does both in one step
post = Post.objects.create(title="My First Post", content="Hello world")

# get_or_create — create only if it doesn't already exist
post, created = Post.objects.get_or_create(
    title="My First Post",
    defaults={'content': 'Hello world'}
)
```

### Reading / Querying Objects

```python
# Get all
posts = Post.objects.all()

# Get a single object — raises exception if 0 or 2+ results
post = Post.objects.get(pk=1)

# Filter — returns a QuerySet (can be empty)
published = Post.objects.filter(published=True)

# Exclude
unpublished = Post.objects.exclude(published=True)

# Ordering
posts = Post.objects.order_by('-created_at')         # descending
posts = Post.objects.order_by('title', '-created_at') # multiple fields

# Limiting (like SQL LIMIT/OFFSET)
first_five = Post.objects.all()[:5]
page_two   = Post.objects.all()[5:10]

# Count
total = Post.objects.count()

# Check existence
has_posts = Post.objects.filter(author=user).exists()

# First / Last
latest = Post.objects.order_by('-created_at').first()
```

### Field Lookups

```python
Post.objects.filter(title__exact="Hello")          # exact match
Post.objects.filter(title__iexact="hello")          # case-insensitive exact
Post.objects.filter(title__contains="Django")         # substring match
Post.objects.filter(title__icontains="django")          # case-insensitive contains
Post.objects.filter(views__gt=100)                         # greater than
Post.objects.filter(views__gte=100)                          # greater than or equal
Post.objects.filter(views__lt=100)                             # less than
Post.objects.filter(views__lte=100)                              # less than or equal
Post.objects.filter(created_at__year=2024)                         # date year
Post.objects.filter(created_at__range=(start, end))                  # date range
Post.objects.filter(author__in=[user1, user2])                         # in a list
Post.objects.filter(content__startswith="Once")                         # starts with
Post.objects.filter(content__endswith="end.")                            # ends with
Post.objects.filter(tags__isnull=True)                                    # is null
```

### Chaining Filters

```python
# Filters can be chained — combined with AND logic
posts = Post.objects.filter(published=True).filter(author=user).order_by('-created_at')

# Equivalent single filter call
posts = Post.objects.filter(published=True, author=user).order_by('-created_at')
```

### `Q` Objects — OR / Complex Queries

```python
from django.db.models import Q

# OR condition
posts = Post.objects.filter(Q(title__icontains='django') | Q(content__icontains='django'))

# AND + OR combined
posts = Post.objects.filter(
    Q(published=True) & (Q(category='tech') | Q(category='news'))
)

# NOT condition
posts = Post.objects.filter(~Q(author=request.user))
```

### Updating Objects

```python
# Update a single object
post = Post.objects.get(pk=1)
post.title = "Updated Title"
post.save()

# Bulk update — much faster, single SQL query
Post.objects.filter(published=False).update(published=True)

# Increment a field atomically (avoids race conditions)
from django.db.models import F
Post.objects.filter(pk=1).update(views=F('views') + 1)
```

### Deleting Objects

```python
# Delete a single object
post = Post.objects.get(pk=1)
post.delete()

# Bulk delete
Post.objects.filter(published=False).delete()
```

### Related Object Queries

```python
# Forward relationship — access related object directly
post = Post.objects.get(pk=1)
print(post.author.username)

# Reverse relationship — uses related_name or model_set
author = User.objects.get(pk=1)
posts = author.posts.all()              # if related_name='posts'
posts = author.post_set.all()             # default reverse accessor

# Filter across relationships
posts = Post.objects.filter(author__username='haseeb')
comments = Comment.objects.filter(post__author__username='haseeb')
```

### Aggregation

```python
from django.db.models import Count, Avg, Sum, Max, Min

# Aggregate over the whole queryset
stats = Post.objects.aggregate(
    total=Count('id'),
    avg_views=Avg('views'),
    max_views=Max('views'),
)
print(stats)   # {'total': 50, 'avg_views': 234.5, 'max_views': 1200}

# Annotate — per-object aggregation
authors = User.objects.annotate(post_count=Count('posts'))
for author in authors:
    print(author.username, author.post_count)
```

### Performance — `select_related` and `prefetch_related`

```python
# N+1 query problem — BAD, hits database once per post
posts = Post.objects.all()
for post in posts:
    print(post.author.username)   # extra query each time!

# select_related — for ForeignKey/OneToOne, single JOIN query
posts = Post.objects.select_related('author').all()
for post in posts:
    print(post.author.username)   # no extra query

# prefetch_related — for ManyToMany/reverse FK, separate optimized query
posts = Post.objects.prefetch_related('tags').all()
for post in posts:
    print([tag.name for tag in post.tags.all()])   # no extra query per post
```

| Method | Use For | How It Works |
|--------|---------|---------------|
| `select_related()` | `ForeignKey`, `OneToOneField` | SQL JOIN — single query |
| `prefetch_related()` | `ManyToManyField`, reverse FK | Separate query, joined in Python |

---

## 11. Django Admin

Django's admin panel is a free, auto-generated interface for managing your data.

### Enabling Admin

```bash
# Create a superuser account
python manage.py createsuperuser
```

Visit `http://127.0.0.1:8000/admin/` and log in.

### Registering a Model

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Customizing the Admin Interface

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published', 'created_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 25
    inlines = [CommentInline]

    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(published=True)
    publish_posts.short_description = "Mark selected posts as published"
```

### Common `ModelAdmin` Options

| Option | Purpose |
|--------|---------|
| `list_display` | Columns shown in the list view |
| `list_filter` | Sidebar filters |
| `search_fields` | Enables a search box |
| `prepopulated_fields` | Auto-fill a field (e.g. slug from title) |
| `readonly_fields` | Fields shown but not editable |
| `ordering` | Default sort order |
| `list_per_page` | Pagination size |
| `inlines` | Edit related objects on the same page |
| `actions` | Custom bulk actions |

---

## 12. Templates

Django's template engine renders dynamic HTML using its own template language (DTL).

### Rendering a Template

```python
# views.py
from django.shortcuts import render

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

### Template Syntax

```html
<!-- blog/templates/blog/post_list.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Blog Posts</h1>

  {% if posts %}
    <ul>
    {% for post in posts %}
      <li>
        <a href="{% url 'blog:post_detail' pk=post.pk %}">{{ post.title }}</a>
        <span>{{ post.created_at|date:"F j, Y" }}</span>
        {% if post.published %}
          <span class="badge">Published</span>
        {% else %}
          <span class="badge">Draft</span>
        {% endif %}
      </li>
    {% endfor %}
    </ul>
  {% else %}
    <p>No posts yet.</p>
  {% endif %}
{% endblock %}
```

### Template Inheritance

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
  <nav>{% include 'partials/navbar.html' %}</nav>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>{% include 'partials/footer.html' %}</footer>
</body>
</html>
```

### Common Template Tags

| Tag | Purpose |
|-----|---------|
| `{% extends 'base.html' %}` | Inherit from a parent template |
| `{% block name %}...{% endblock %}` | Define an overridable section |
| `{% include 'partial.html' %}` | Include another template |
| `{% for x in list %}...{% endfor %}` | Loop |
| `{% if condition %}...{% endif %}` | Conditional |
| `{% url 'name' %}` | Reverse a URL by name |
| `{% static 'path' %}` | Link to a static file |
| `{% csrf_token %}` | Required inside every `<form method="post">` |
| `{{ variable }}` | Output a variable |
| `{{ variable\|filter }}` | Apply a filter to a variable |

### Common Template Filters

```html
{{ post.title|upper }}                  <!-- UPPERCASE -->
{{ post.title|lower }}                   <!-- lowercase -->
{{ post.title|truncatewords:10 }}         <!-- limit word count -->
{{ post.created_at|date:"M d, Y" }}        <!-- format a date -->
{{ post.content|linebreaks }}               <!-- convert \n to <p>/<br> -->
{{ post.content|striptags }}                 <!-- remove HTML tags -->
{{ value|default:"N/A" }}                     <!-- fallback if empty -->
{{ list|length }}                              <!-- length of a list -->
{{ value|safe }}                                <!-- mark as safe (skip auto-escaping) -->
{{ price|floatformat:2 }}                        <!-- format decimals -->
```

### `{% for %}` Loop Variables

```html
{% for post in posts %}
  {{ forloop.counter }}     <!-- 1-indexed loop counter -->
  {{ forloop.counter0 }}    <!-- 0-indexed loop counter -->
  {{ forloop.first }}       <!-- True on first iteration -->
  {{ forloop.last }}        <!-- True on last iteration -->
  {{ forloop.revcounter }}  <!-- counter counting down to 1 -->
{% endfor %}
```

> [!WARNING]
> Django auto-escapes HTML in `{{ variable }}` output to prevent XSS attacks. Only use the `|safe` filter or `{% autoescape off %}` on content you fully trust.

---

## 13. Forms

Django forms handle rendering, validation, and cleaning of user input.

### A Basic Form

```python
# blog/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('.com'):
            raise forms.ValidationError("Only .com emails are allowed")
        return email
```

### Using a Form in a View

```python
# views.py
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # process the data — send email, save, etc.
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

```html
<!-- contact.html -->
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Send</button>
</form>
```

### `ModelForm` — Auto-Generated from a Model

```python
# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters")
        return title
```

```python
# views.py
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)   # don't save yet
            post.author = request.user        # set extra field
            post.save()                         # now save
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
```

### File Upload Forms

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
```

```html
<!-- requires enctype for file uploads -->
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

```python
def profile_update(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
```

### Common Form Field Types

| Field | Renders As | Example |
|-------|-----------|---------|
| `CharField` | `<input type="text">` | `forms.CharField(max_length=100)` |
| `EmailField` | `<input type="email">` | `forms.EmailField()` |
| `IntegerField` | `<input type="number">` | `forms.IntegerField()` |
| `BooleanField` | `<input type="checkbox">` | `forms.BooleanField(required=False)` |
| `ChoiceField` | `<select>` | `forms.ChoiceField(choices=CHOICES)` |
| `DateField` | `<input type="date">` | `forms.DateField()` |
| `FileField` | `<input type="file">` | `forms.FileField()` |
| `ModelChoiceField` | `<select>` from a queryset | `forms.ModelChoiceField(queryset=Category.objects.all())` |

---

## 14. Static Files & Media

### Static Files (CSS, JS, images bundled with code)

```python
# settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']      # development source files
STATIC_ROOT = BASE_DIR / 'staticfiles'         # production collectstatic destination
```

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
<script src="{% static 'js/app.js' %}"></script>
```

```bash
# Collect all static files into STATIC_ROOT for production
python manage.py collectstatic
```

### Media Files (user-uploaded content)

```python
# settings.py
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

```python
# urls.py — serve media files in development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
# models.py
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True)
```

```html
{% if profile.avatar %}
  <img src="{{ profile.avatar.url }}" alt="Avatar">
{% endif %}
```

> [!NOTE]
> In production, static and media files should be served by a dedicated service (Nginx, AWS S3, Cloudflare R2) — not by Django itself.

---

## 15. Authentication & Authorization

Django ships with a complete user authentication system.

### Built-in Auth Views

```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
```

### Manual Login / Logout / Register

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
```

### Restricting Access

```python
# Function-based views
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@permission_required('blog.add_post')
def post_create(request):
    ...

# Class-based views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login/'

class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
```

```html
<!-- Templates -->
{% if user.is_authenticated %}
  <p>Welcome, {{ user.username }}!</p>
  <a href="{% url 'logout' %}">Logout</a>
{% else %}
  <a href="{% url 'login' %}">Login</a>
{% endif %}
```

### Custom User Model

It is strongly recommended to set up a custom user model **before your first migration**, even if you don't need it immediately.

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    is_verified = models.BooleanField(default=False)
```

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

> [!WARNING]
> Switching to a custom user model after running initial migrations is painful and risky. Set `AUTH_USER_MODEL` at the very start of a project.

### Permissions and Groups

```python
# Check permissions
request.user.has_perm('blog.add_post')
request.user.is_staff
request.user.is_superuser

# Assign permissions programmatically
from django.contrib.auth.models import Permission, Group

group = Group.objects.create(name='Editors')
permission = Permission.objects.get(codename='add_post')
group.permissions.add(permission)
user.groups.add(group)
```

---

## 16. Middleware

Middleware is a framework of hooks into Django's request/response processing.

### How Middleware Works

```
Request  ──▶ Middleware 1 ──▶ Middleware 2 ──▶ View
                                                  │
Response ◀── Middleware 1 ◀── Middleware 2 ◀──────┘
```

### Writing Custom Middleware

```python
# blog/middleware.py
import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)   # passes to next middleware/view

        duration = time.time() - start
        response['X-Response-Time'] = f"{duration:.3f}s"
        return response
```

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ... built-in middleware
    'blog.middleware.RequestTimingMiddleware',   # 👈 your custom middleware
]
```

### Common Built-in Middleware

| Middleware | Purpose |
|-----------|---------|
| `SecurityMiddleware` | HTTPS redirects, security headers |
| `SessionMiddleware` | Enables `request.session` |
| `CommonMiddleware` | URL rewriting, basic protections |
| `CsrfViewMiddleware` | CSRF protection for POST requests |
| `AuthenticationMiddleware` | Enables `request.user` |
| `MessageMiddleware` | Enables the messages framework |
| `XFrameOptionsMiddleware` | Clickjacking protection |

---

## 17. Signals

Signals let decoupled pieces of code get notified when actions happen elsewhere in the framework.

### Built-in Signals

```python
# blog/signals.py
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_delete, sender=Post)
def log_post_deletion(sender, instance, **kwargs):
    print(f"Post '{instance.title}' is about to be deleted")
```

### Connecting Signals

```python
# blog/apps.py
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals   # registers the signal handlers
```

### Common Signals

| Signal | Fires When |
|--------|-----------|
| `pre_save` | Before a model's `save()` is called |
| `post_save` | After a model's `save()` is called |
| `pre_delete` | Before a model's `delete()` is called |
| `post_delete` | After a model's `delete()` is called |
| `m2m_changed` | When a ManyToManyField changes |
| `request_started` | When Django starts processing a request |
| `request_finished` | When Django finishes a request |

> [!TIP]
> Signals are powerful but can make code harder to trace. Prefer overriding `save()` directly when the logic belongs to a single model, and reach for signals when truly decoupled apps need to react to each other.

---

## 18. Django REST Framework

DRF is the standard toolkit for building REST APIs on top of Django.

### Installation

```bash
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
]
```

### Serializers

```python
# blog/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_name', 'published', 'created_at']
        read_only_fields = ['id', 'created_at']
```

### API Views

```python
# blog/views.py
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer

# Using a ViewSet — full CRUD with minimal code
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Using generic views — more explicit
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### Routing with `ViewSet`

```python
# urls.py
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
# Automatically creates: /api/posts/, /api/posts/<pk>/
```

### Authentication for APIs

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

```bash
pip install djangorestframework-simplejwt   # for JWT-based auth
```

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

---

## 19. Testing

Django includes a testing framework built on Python's `unittest`.

### Writing Tests

```python
# blog/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='haseeb', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_count(self):
        self.assertEqual(Post.objects.count(), 1)


class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='haseeb', password='testpass123')
        self.post = Post.objects.create(title='Test', content='Content', author=self.user)

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

    def test_post_detail_view_404(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

    def test_login_required_for_create(self):
        response = self.client.get(reverse('blog:post_create'))
        self.assertRedirects(response, '/login/?next=/blog/create/')
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test blog

# Run a specific test class
python manage.py test blog.tests.PostModelTest

# Run with verbosity
python manage.py test --verbosity=2

# Check test coverage
pip install coverage
coverage run manage.py test
coverage report
coverage html
```

### Common Assertions

| Assertion | Checks |
|-----------|--------|
| `assertEqual(a, b)` | `a == b` |
| `assertTrue(x)` | `x` is truthy |
| `assertFalse(x)` | `x` is falsy |
| `assertContains(response, text)` | Response body contains text |
| `assertRedirects(response, url)` | Response redirects to URL |
| `assertRaises(Exception)` | Code raises an exception |
| `response.status_code` | HTTP status code check |

---

## 20. Deployment

### Pre-Deployment Checklist

```python
# settings.py — production settings
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security headers
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
```

```bash
# Run Django's built-in deployment checklist
python manage.py check --deploy
```

### Production Server Stack

```
Internet ──▶ Nginx (reverse proxy + static files)
                  │
                  ▼
            Gunicorn / uWSGI (WSGI server)
                  │
                  ▼
            Django Application
                  │
                  ▼
            PostgreSQL Database
```

### Running with Gunicorn

```bash
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

### Common Deployment Targets

| Platform | Notes |
|----------|-------|
| **Railway / Render** | Easiest, Git-based deploys, free tiers available |
| **Heroku** | Classic PaaS choice, Procfile-based |
| **AWS (EC2 / Elastic Beanstalk)** | Full control, more setup required |
| **DigitalOcean App Platform** | Simple, predictable pricing |
| **VPS (manual)** | Nginx + Gunicorn + systemd, full control |
| **Docker** | Containerized, portable across any host |

### Environment Variables for Production

```bash
# .env (never commit this file)
DJANGO_SECRET_KEY=your-production-secret-key
DJANGO_DEBUG=False
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432
```

### Static Files in Production

```bash
python manage.py collectstatic --noinput
```

```python
# Use whitenoise for simple static file serving without a separate service
pip install whitenoise

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # 👈 add right after security
    # ...
]
```

---

## 21. Best Practices

| Practice | Why It Matters |
|----------|----------------|
| Use environment variables for secrets | Never expose `SECRET_KEY` or DB passwords in code |
| Set `DEBUG = False` in production | `DEBUG = True` leaks stack traces and sensitive data |
| Use `select_related` / `prefetch_related` | Avoid the N+1 query problem |
| Keep business logic out of views | Push reusable logic into models or services |
| Use `ModelForm` over manual forms when possible | Less duplication, automatic validation |
| Write tests for models and views | Catch regressions before deployment |
| Use migrations consistently | Never modify the database schema manually |
| Set a custom user model early | Switching later is painful |
| Use `get_object_or_404` instead of manual try/except | Cleaner, idiomatic Django |
| Validate user input via forms/serializers | Never trust raw `request.POST` data directly |
| Use Django's built-in auth | Don't reinvent password hashing or sessions |
| Cache expensive queries | Use Django's cache framework for hot paths |
| Keep apps small and focused | One app per feature domain, not one giant app |

### Project Layout for Larger Apps

```
myproject/
├── apps/
│   ├── accounts/
│   ├── blog/
│   └── payments/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
├── static/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── manage.py
```

---

## 22. Quick Reference Cheat Sheet

```bash
# ── PROJECT / APP SETUP ───────────────────────────────
django-admin startproject myproject     # new project
python manage.py startapp blog          # new app
python manage.py runserver              # dev server

# ── MIGRATIONS ────────────────────────────────────────
python manage.py makemigrations         # create migration files
python manage.py migrate                # apply migrations
python manage.py showmigrations         # list migration status
python manage.py sqlmigrate blog 0001   # show SQL for a migration

# ── ADMIN / USERS ─────────────────────────────────────
python manage.py createsuperuser        # create admin user
python manage.py changepassword <user>  # reset password

# ── SHELL / DEBUGGING ─────────────────────────────────
python manage.py shell                  # interactive Python shell with models loaded
python manage.py dbshell                # database CLI shell
python manage.py check                  # check for project issues
python manage.py check --deploy         # deployment readiness check

# ── STATIC FILES ──────────────────────────────────────
python manage.py collectstatic          # gather static files for production

# ── TESTING ────────────────────────────────────────────
python manage.py test                   # run all tests
python manage.py test blog              # run tests for one app
```

```python
# ── MODELS ─────────────────────────────────────────────
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# ── VIEWS (FBV) ────────────────────────────────────────
def my_view(request):
    return render(request, 'template.html', {'key': 'value'})

# ── VIEWS (CBV) ────────────────────────────────────────
class MyView(ListView):
    model = Post

# ── URLS ───────────────────────────────────────────────
path('posts/<int:pk>/', views.post_detail, name='post_detail')

# ── ORM QUERIES ────────────────────────────────────────
Post.objects.all()
Post.objects.filter(published=True)
Post.objects.get(pk=1)
Post.objects.create(title="...", content="...")
Post.objects.filter(pk=1).update(title="New")
Post.objects.filter(pk=1).delete()

# ── TEMPLATE TAGS ──────────────────────────────────────
{% extends 'base.html' %}
{% block content %}{% endblock %}
{% for x in list %}{% endfor %}
{% if condition %}{% endif %}
{% url 'name' %}
{% static 'path' %}
{% csrf_token %}
```

---

<div align="center">

**Django Complete Reference** — Made with 💚 by Haseeb

*Django 5.x · Python 3.10+ · Feel free to fork and star ⭐*

</div>