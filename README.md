# PistachioDelights

PistachioDelights is a full-stack web application that simulates a pistachio dessert store. Built using Flask and SQLAlchemy, the app allows users to register securely, browse traditional Turkish desserts, manage their cart, and complete a simulated checkout process.

## Features

- User registration with hashed passwords  
- Static list of desserts with images and prices  
- Add/remove desserts to/from cart with quantity control  
- Session-based cart management  
- Simulated checkout confirmation  
- Clean and modular project structure  

## Technologies Used

- Python 3.8+  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- HTML, CSS  
- Bootstrap (via CDN)  
- Jinja2 Templating  

## Project Structure

```
.
├── app.py             # Main application with all routes
├── models.py          # User model with password hashing
├── config.py          # App config and database setup
├── init_db.py         # Initializes the database
├── static/            # Dessert images, CSS
│   ├── Baklava.png
│   ├── Yeşil fıstıklar.jpg
│   ├── katmer.jpg
│   ├── kunefe.jpg
│   ├── lokum.jpg
│   ├── kadayif.webp
│   ├── sutlac.jpg
│   ├── style.css
├── templates/         # HTML templates
├── .gitignore
├── LICENSE
└── README.md
```

## How to Run

To run the application locally:

### 1. Clone the repository

```bash
git clone https://github.com/berkaybakac/PistachioDelights.git
cd PistachioDelights
```

### 2. Set up and run

Open Python shell and create the database:

```python
from app import db, app
with app.app_context():
    db.create_all()
```

Then run the Flask server:

```bash
flask run
```

Go to `http://127.0.0.1:5000` in your browser.

## Routes Overview

| Route                   | Function                                      |
|------------------------|-----------------------------------------------|
| `/`                    | Homepage                                       |
| `/about`               | About page                                     |
| `/register`            | Register a new user                            |
| `/tatlilar`            | Show dessert list with prices and images       |
| `/sepete_ekle/<name>`  | Add dessert to cart                            |
| `/sepete_azalt/<name>` | Decrease quantity or remove dessert            |
| `/sepet`               | View and manage shopping cart                  |
| `/odeme_yapildi`       | Simulated payment confirmation and cart reset  |

## Screenshots

### Desserts Page

![Desserts Page](static/Baklava.png)

### Cart Page

![Cart Page](static/katmer.jpg)

### Checkout Page

![Checkout Page](static/sutlac.jpg)

> Tip: You can rename or standardize screenshots (e.g., `tatlilar_sayfasi.png`) for consistency.

## Security

Passwords are never stored in plain text.  
They are hashed securely using Werkzeug methods:

```python
from werkzeug.security import generate_password_hash, check_password_hash

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)
```

## Notes

- The dessert data is currently hardcoded inside `app.py`
- Cart is stored in session — not linked to the user model or database
- There is no login/logout functionality (registration only)

## Possible Improvements

- Add login/logout system  
- Store cart in the database per user  
- Admin panel for dessert management  
- Replace hardcoded data with database queries  
- Add image thumbnails to the cart page  

## License

MIT License — see LICENSE file for details.
