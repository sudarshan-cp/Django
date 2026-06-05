# Jobnest

A job board web application built with Django.

## Features

- Job listings management
- User accounts and authentication
- Admin dashboard

## Tech Stack

- Python / Django 6.0
- SQLite (development)
- Bootstrap 5 (via django-crispy-forms)
- Pillow for image handling

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sudarshan-cp/Django.git
   cd Django
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser.

## Project Structure

```
Django/
├── accounts/       # User authentication app
├── jobs/           # Job listings app
├── jobnest/        # Project settings and root URLs
├── manage.py
└── requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

MIT
