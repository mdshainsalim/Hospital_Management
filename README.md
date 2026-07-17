# Hospital Management System API

A Hospital Management System built with Django REST Framework.

## Features

- User Registration
- JWT Authentication
- Doctor Management
- Appointment Management
- Billing System
- Dashboard Statistics
- Search
- Filter
- Ordering
- Pagination
- Custom Middleware
- Admin Panel

---

## Technologies

- Python 3
- Django 6
- Django REST Framework
- SQLite
- Simple JWT
- Django Filter

---

## Installation

Clone the repository

```bash
git clone <repository_url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run migration

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

---

## Authentication

Login

```
POST /api/login/
```

Returns

- Access Token
- Refresh Token

Use

```
Authorization: Bearer <ACCESS_TOKEN>
```

---

## API Endpoints

### Accounts

```
POST /api/register/
POST /api/login/
GET  /api/profile/
```

### Doctors

```
GET
POST
PUT
DELETE

/api/doctors/
```

### Appointments

```
GET
POST
PUT
DELETE

/api/appointments/
```

### Bills

```
GET
POST
PUT
DELETE

/api/bills/
```

### Dashboard

```
GET /api/dashboard/dashboard/
```

---

## Admin

```
http://127.0.0.1:8000/admin/
```

---

## Author

Md Shain Salim