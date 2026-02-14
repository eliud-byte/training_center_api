# Tranining Center Management API 🎓

A robust backend API for managing a vocational training center. This system handles User Authentication (Role-Based), Course Management, Cohort Scheduling, and Student Enrollment.

## Key Features
* **Role-Based Access Control (RBAC):** Distinct permissions for Admins, Instructors, and Students.
* **Secure Authentication:** JWT (JSON Web Tokens) implementation via Djoser.
* **Cohort Management** Logic to manage course instances, capacity, and instructor assignment
* **PostgresSQL Integration:** Production-ready database schema for data integrity.

## Tech Stack
* **Language:** Python 3.12+
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Authentication:** Djoser / SimpleJWT

## ⚙️ Local Setup Guide
Follow these steps to get the project running on your local machine.

### 1. Prerequisites
* Python installed
* PostgreSQL installed and running

### 2. Installation
1.  **Clone the repository** (if using git)
    ```bash
    git clone <repo-url>
    cd training_center_api
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Environment Variables**
    Create a `.env` file in the root directory and add your databse credentials:
    ```text
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://YOUR_DB_USER:YOUR_DB_PASSWORD@127.0.0.1:5432/training_center_db
    ```

*Note: Ensure you have a PostgreSQL database named `training_center_db` created locally.*

5. **Initialize the Database**
```bash
python manage.py migrate
```

6. **Create Admin User
```bash
python mnage.py createsuperuser
```

7. Run the Server
```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/`.

## 📡 API Endpoints (Quick Reference)
### Authentication
* `POST /auth/users/` - Register a new user
* `POST /auth/jwt/create/` - Login (Get Access / Refresh Tokens)

