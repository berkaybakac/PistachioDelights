# PistachioDelights

PistachioDelights is a full-stack web application that simulates a dessert store experience. Users can register, browse a list of pistachio-based Turkish desserts, manage their shopping cart, and complete a simulated checkout process. The application is built using Flask, SQLAlchemy, and session-based logic.

## Features

- User registration with hashed passwords  
- List of desserts with images and prices  
- Add/remove desserts to/from cart with quantity control  
- Session-based cart management  
- Simulated checkout functionality  
- Clean and modular Flask project structure  

## Technologies Used

- Python 3.8+  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- Jinja2  
- HTML & CSS (with Bootstrap CDN)  

## Project Structure

```
.
├── app.py             # Main Flask application
├── models.py          # User model and password hashing
├── config.py          # Application configuration and DB URI
├── init_db.py         # Script to initialize the database
├── static/            # Static assets (images, CSS)
├── templates/         # HTML templates
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Installation

Follow the steps below to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/berkaybakac/PistachioDelights.git
cd PistachioDelights
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the database

```python
# Run Python shell
python

# Then execute the following:
from app import db, app
with app.app_context():
    db.create_all()
```

### 4. Run the application

```bash
flask run
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

## Available Routes

| Route                     | Description                                |
|---------------------------|--------------------------------------------|
| `/`                       | Homepage                                   |
| `/about`                  | About page                                 |
| `/register`               | Register a new user                        |
| `/tatlilar`               | Browse dessert items                       |
| `/sepete_ekle/<tatli>`    | Add a dessert to the cart                  |
| `/sepete_azalt/<tatli>`   | Decrease quantity or remove from cart      |
| `/sepet`                  | View current cart                          |
| `/odeme_yapildi`          | Simulated checkout confirmation            |

## Screenshots

### Desserts Page

![Desserts Page](static/tatlilar_sayfasi.png)

### Cart Page

![Cart Page](static/sepet_sayfasi.png)

### Checkout Page

![Checkout Page](static/odeme_sayfasi.png)

> Make sure the above images exist inside the `static/` folder with matching filenames.

## Security Notes

Passwords are hashed using Werkzeug:

```python
from werkzeug.security import generate_password_hash, check_password_hash

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)
```

## Possible Improvements

- Add login/logout functionality  
- Store cart items in a database instead of session  
- Admin interface for dessert management  
- Payment gateway integration  

## License

This project is licensed under the MIT License.
