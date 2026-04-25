# North Gate Resort Isiolo

A Django-based booking system for North Gate Resort Isiolo.

## Getting started

1. Create and activate a Python virtual environment:

```bash
cd /Users/Leo/northgate
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python3 manage.py migrate
```

4. Create a superuser:

```bash
python3 manage.py createsuperuser
```
```

5. Run the development server:

```bash
python3 manage.py runserver
```

6. Open the site in your browser:

- Public site: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## Project structure

- `core/` - main hotel booking app
- `core/models.py` - Room, Booking, Order, Payment models
- `core/views.py` - home, room detail, booking, user auth
- `core/templates/core/` - frontend templates
- `northgate/settings.py` - project configuration

## Notes

- The app currently uses SQLite for local development.
- Room availability is checked before saving a booking.
- We can next add PostgreSQL support and M-Pesa STK Push integration.
