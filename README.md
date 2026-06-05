# Jobnest

A full-featured job board web application built with Django and Bootstrap 5.

---

## Features

- Browse and search job listings by keyword and job type
- Job detail pages with full description, requirements and salary info
- Filter jobs by type: Full Time, Part Time, Remote, Contract, Internship
- Admin panel to post and manage job listings
- Branded admin dashboard (Jobnest Administration)
- Responsive UI built with Bootstrap 5
- Environment-based configuration via `.env`

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, Django 6.0 |
| Frontend | Bootstrap 5.3, Bootstrap Icons |
| Database | SQLite (development) |
| Forms | django-crispy-forms + crispy-bootstrap5 |
| Config | django-environ |
| Images | Pillow |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudarshan-cp/Django.git
   cd Django
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your `SECRET_KEY`.

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the app**

   | URL | Page |
   |-----|------|
   | `http://127.0.0.1:8000/` | Home page |
   | `http://127.0.0.1:8000/jobs/` | Browse all jobs |
   | `http://127.0.0.1:8000/admin/` | Admin dashboard |

---

## Posting Jobs (Admin)

1. Go to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Click **Jobs → Add Job**
4. Fill in the title, company, location, type, description, and salary
5. Check **Is active** to publish it
6. Click **Save** — the job appears on the site instantly

---

## Project Structure

```
Django/
├── accounts/               # User authentication app
│   ├── Acc_urls.py
│   ├── models.py
│   └── views.py
├── jobs/                   # Job listings app
│   ├── templates/
│   │   └── jobs/
│   │       ├── home.html
│   │       ├── job_list.html
│   │       └── job_detail.html
│   ├── admin.py
│   ├── jobs_urls.py
│   ├── models.py
│   └── views.py
├── jobnest/                # Project settings and root URLs
│   ├── templates/
│   │   └── base.html
│   ├── settings.py
│   └── urls.py
├── .env.example
├── manage.py
└── requirements.txt
```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

MIT
