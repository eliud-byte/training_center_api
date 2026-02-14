# Tranining Center Management API

A robust backend API for managing a vocational training center. This system handles User Authentication (Role-Based), Course Management, Cohort Scheduling, and Student Enrollment.

## Key Features
- **Role-Based Access Control (RBAC):** Distinct permissions for Admins, Instructors, and Students.
- **Secure Authentication:** JWT (JSON Web Tokens) implementation via Djoser.
- **course Catalog:** Admins can manage course templates (titles, descriptions, pricing).
- **Cohort Management** Schedule specific class instances with assigned instructors and capacity limits.
- **Smart Validation:** Logic to prevent scheduling errors (e.g., end dates before start dates).
- **Human-Readable API: Nested serializers provide detailed text responses (e.g., "Python 101") instead of just raw Database IDs.

## Tech Stack
* **Language:** Python 3.12+
* **Framework:** Django 6 & Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Authentication:** Djoser / SimpleJWT
- **Tools:** Git, Pip

## Database Schema
The project uses a relational database structure designed for scalability.
```Code snippet
erDiagram
    User {
        int id PK
        string username
        string email
        string role "ADMIN, INSTRUCTOR, STUDENT"
    }
    Course {
        int id PK
        string title
        text description
        decimal price
    }
    Cohort {
        int id PK
        string name
        date start_date
        date end_date
        int capacity
    }
    
    User ||--o{ Cohort : "instructs"
    Course ||--|{ Cohort : "has instances"
```

## Local Setup Guide
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

## API Endpoints
### Authentication
* `POST /auth/users/` - Register a new user
* `POST /auth/jwt/create/` - Login (Get Access / Refresh Tokens)

### 2. Courses (The Catalog)
_Requires Admin role for Create/Update/Delete._
| Method | Endpoint | Description |
| :--- | : --- | :--- |
| GET | `/api/courses/` | List all available training courses. |
| POST | `/api/courses/` | Create a new course syllabus. |
| GET | `/api/courses/{id}/` | View specific course details. |
| PATCH | `/api/courses/{id}/` | Update course pricing or description. |

### 3. Cohorts(Scheduled Classes)
_Links Courses to Instructors. Requires Admin role for changes._
| Method | Endpoint | Description |
| :--- | : --- | :--- |
| GET | `/api/cohorts/` | List all active/upcoming cohorts. |
| POST | `/api/cohorts/` | Schedule a new cohort instance. |
| GET | `/api/cohorts/{id}/` | View cohort details (including instructor name). |

## Permissions
- **Public (Anon):** Can view (GET) Courses and Cohorts.
- **Authenticated Users:** Can view their own profiles.
- **Admins:** Full access to Create (POST), Update(PUT), and Delete (DELETE) resources.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeture`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.
