# 🎯 KidLink - Youth Activity Management System

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

KidLink is a comprehensive youth activity management platform that connects young people with engaging educational, creative, and social opportunities. Built with Django, it provides a complete solution for managing youth programs, institutes, activities, and registrations.

## 📋 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Security](#-security)
- [License](#-license)

---

## 🌟 Overview

KidLink streamlines the management of youth programs by providing:
- **Centralized Management**: Single platform for youth records, institutes, and activities
- **Intelligent Matching**: Link youth with appropriate institutes and activities
- **AI-Powered Assistance**: OpenAI-powered chatbot for instant help
- **Comprehensive Reporting**: Export data in Excel and PDF formats
- **Role-Based Access**: Secure authentication with staff-only administrative access

### Who Is It For?
- **Community Centers**: Manage youth programs and track engagement
- **Schools**: Coordinate extracurricular activities and youth services
- **Youth Organizations**: Organize events and maintain participant records
- **Social Services**: Track youth placements and program outcomes

---

## ✨ Key Features

### 👥 Youth Management
- **Complete Profiles**: Store detailed youth information (name, age, contact details)
- **Institute Assignments**: Link youth to registered institutes
- **Activity Enrollment**: Track youth participation in activities
- **Search & Filter**: Quick lookup by name, institute, or activity
- **Bulk Operations**: Export youth records to Excel/PDF

### 🏫 Institute Management
- **Multi-Institute Support**: Manage multiple partner organizations
- **Contact Information**: Store addresses, phone numbers, and emails
- **Youth Tracking**: View all youth enrolled per institute
- **CRUD Operations**: Create, update, view, and delete institute records

### 🎨 Activity Management
- **Event Planning**: Create activities with descriptions and dates
- **Registration Tracking**: Monitor youth signups per activity
- **Capacity Management**: Set participant limits
- **Activity Calendar**: Chronological view of upcoming events
- **Reporting**: Generate activity participation reports

### 🔗 Youth-Institute-Activity Linking
- **Many-to-Many Relationships**: Youth can join multiple activities and institutes
- **Registration System**: Track enrollment dates and status
- **Cross-Reference Reports**: See which youth attend which activities at which institutes

### 🤖 AI Chatbot Assistant
- **OpenAI GPT-4 Integration**: Intelligent conversational assistant
- **Context-Aware**: Understands youth management domain
- **Rate Limited**: 10 requests per minute to prevent abuse
- **Secure**: CSRF-protected, authentication-required
- **Real-Time Responses**: Instant answers to common questions

### 📊 Reporting & Export
- **Excel Export**: Download youth/activity data as `.xlsx`
- **PDF Generation**: Create printable reports with ReportLab
- **Custom Queries**: Filter before export
- **Bulk Operations**: Process multiple records efficiently

### 🔐 Authentication & Security
- **Staff-Only Access**: Login required for all administrative functions
- **CSRF Protection**: Secure forms against cross-site attacks
- **Rate Limiting**: Prevent API abuse
- **Input Validation**: Sanitize all user inputs
- **XSS Protection**: HTML escaping in templates

---

## 🏗️ System Architecture

### Database Schema

```
┌─────────────┐         ┌──────────────────┐         ┌─────────────┐
│   Youth     │         │  YouthInstitute  │         │  Institute  │
├─────────────┤         ├──────────────────┤         ├─────────────┤
│ id (PK)     │────┐    │ id (PK)          │    ┌────│ id (PK)     │
│ name        │    │    │ youth_id (FK)    │    │    │ name        │
│ age         │    └───→│ institute_id (FK)│←───┘    │ address     │
│ email       │         │ register_date    │         │ phone       │
│ phone       │         └──────────────────┘         │ email       │
└─────────────┘                                      └─────────────┘
      │                                                      │
      │                                                      │
      │         ┌──────────────────┐                        │
      │         │ YouthActivity    │                        │
      │         ├──────────────────┤                        │
      └────────→│ id (PK)          │                        │
                │ youth_id (FK)    │                        │
                │ activity_id (FK) │←───────────────────────┘
                │ register_date    │         ┌─────────────┐
                └──────────────────┘         │  Activity   │
                                             ├─────────────┤
                                             │ id (PK)     │
                                             │ name        │
                                             │ description │
                                             │ date        │
                                             │ institute_id│
                                             └─────────────┘
```

### Application Structure

```
kidlink/
├── kidlink/                    # Project configuration
│   ├── settings.py            # Django settings (with security configs)
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI entry point
├── administration/            # Core app - Youth management
│   ├── models.py              # Youth, Institute, Activity models
│   ├── views.py               # CRUD views, auth, exports
│   ├── forms.py               # Django ModelForms
│   ├── urls.py                # App-specific URLs
│   ├── admin.py               # Django admin configuration
│   └── management/
│       └── commands/
│           └── seed_data.py   # Test data generator
├── chatbot/                   # AI Assistant
│   ├── views.py               # OpenAI integration with rate limiting
│   └── urls.py                # Chatbot API endpoints
├── templates/                 # HTML templates
│   ├── sidebar.html           # Base template with navigation
│   ├── administration/        # Youth management templates
│   ├── institutes/            # Institute management templates
│   ├── activities/            # Activity management templates
│   └── chatbot/               # Chatbot interface
├── static/                    # Static assets
│   ├── CSS/                   # Stylesheets
│   ├── images/                # Images and icons
│   └── js/                    # JavaScript files
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database (dev only)
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (not in Git)
```

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2+
- **Language**: Python 3.12
- **Database**: SQLite3 (dev) / PostgreSQL (production)
- **ORM**: Django ORM
- **Authentication**: Django Auth with staff permissions

### Frontend
- **HTML5** with Django Templates
- **CSS3** with custom stylesheets
- **JavaScript (ES6+)** for interactivity
- **Bootstrap 5** for responsive design
- **Font Awesome** for icons

### APIs & Integrations
- **OpenAI GPT-4**: AI chatbot assistant
- **ReportLab**: PDF generation
- **openpyxl**: Excel file generation

### Security & Performance
- **WhiteNoise**: Static file serving
- **django-environ**: Environment variable management
- **Custom Rate Limiter**: API request throttling
- **CSRF Protection**: Built-in Django security

### DevOps & Deployment
- **Gunicorn**: WSGI HTTP server
- **Railway/Render/Heroku**: Deployment platforms
- **Git**: Version control
- **GitHub**: Repository hosting

---

## 🔐 Security

### Implemented Security Measures
- ✅ **Authentication**: `@login_required` on all views
- ✅ **Authorization**: `is_staff` checks
- ✅ **CSRF Protection**: Django tokens on all forms
- ✅ **XSS Prevention**: Template escaping
- ✅ **SQL Injection**: Django ORM parameterization
- ✅ **Rate Limiting**: Custom decorator on chatbot API
- ✅ **Input Validation**: Form validation with max lengths
- ✅ **HTTPS**: Enforced in production
- ✅ **Secure Cookies**: HTTP-only, secure flags in production
- ✅ **Environment Variables**: Secrets in `.env` (not in code)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Project Maintainer**: Frank Junior Jimenez Encarnacion  
**Email**: jimenezfrankjunior@gmail.com 
**GitHub**: [@yourusername](https://github.com/jimenez10frank)

---

## 📸 Screenshots

### Dashboard
<img width="1920" height="1080" alt="Dashboard" src="https://github.com/user-attachments/assets/33bb1290-cc54-4883-b455-02641de55b3d" />

### Youth Management
<img width="1920" height="1080" alt="YouthActivity" src="https://github.com/user-attachments/assets/b010939d-a430-41e9-920d-ab63ca79d3e0" />

### AI Chatbot
<img width="1920" height="1080" alt="AiAssistant" src="https://github.com/user-attachments/assets/cb62e79f-15ed-459f-990b-9cc1f63a0da5" />

### Youth Institutes
<img width="1920" height="1080" alt="YouthInstitute" src="https://github.com/user-attachments/assets/962e7ee0-6ce9-4417-aec3-4b18cf0d502f" />

---
