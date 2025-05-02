# Flutter App Backend (Flask)

This is a Flask-based backend API developed for a mobile application built with Flutter. It provides endpoints for user authentication, product listing, basket management, and user profile data. The backend communicates via JSON and is designed to be consumed by the frontend mobile client.

## Features

- User registration and login (without JWT tokens)
- Fetching user profile data
- Product listing API
- Basket and basket items management
- SQLite database for lightweight storage
- API built using Flask's `MethodView` for clean route structure

## Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite
- Flask MethodViews for API routes

## Folder Structure
```
project/
│
├── app/
│   ├── __init__.py
│   ├── model/
│   │   └── models.py              # SQLAlchemy models
│   ├── api/
│   │   └── views.py               # API endpoints using MethodViews
│
├── static/uploads/                # Uploaded product images
├── run.py                         # Entry point for the Flask app

```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. Create a virtual environment and activate it
  ```bash
  python -m venv venv
  source venv/bin/activate   # or venv\Scripts\activate on Windows
  ```
3. Install dependencies
```bash
  pip install -r requirements.txt
```
4. Run the application
```bash
  python run.py
```
