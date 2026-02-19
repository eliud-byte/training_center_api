# 🎓 Tranining Center Management API

A robust, RESTful backend API designed to manage vocational training centers. This system handels role-based access control, course scheduling, automated student enrollments, and academic grading.

## 🚀 Key Features

- **Role-Based Access Control (RBAC):** Distinct permissions for **Admins**, **Instructors**, and **Students**.
- **Secure Authentication:** JWT (JSON Web Tokens) implementation via Djoser.
- **course Catalog:** Admins can manage course templates (titles, descriptions, pricing).
- **Cohort Management** Schedule specific class instances with assigned instructors and capacity limits.
- **Smart Validation:** Logic to prevent scheduling errors (e.g., end dates before start dates).
- **Self_Service Enrollments:** Students can browse and enroll in cohorts directly via the API.
- **Capacity Enforcement:** Automated "Bouncer" logic prevents over-enrollment beyond  cohort's set capacity.
- **Academic Grading:** Instructors can assign scores and feedback to specific enrollments.
- **Automated Workflow:** Enrollment status automatically transitions to `COMPLETED` once a grade is posted.
- **Human-Readable API:** Nested serializers show student names, cohort titles, and even grades directly inside enrollment objects.

## 🛠 Tech Stack

- **Language:** Python 3.12+
- **Framework:** Django 6 & Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** Djoser / SimpleJWT
- **Tools:** Git, Pip

## Database Schema (Updated)

The project uses a relational database structure designed for scalability. The relationship between users and classes is managed through a central "Join Table".

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
    Enrollment {
        int id PK
        string status "PENDING, ACTIVE, COMPLETED, DROPPED"
    }
    Grade {
        int id PK
        decimal score
        text feedback
    }
    
    User ||--o{ Cohort : "instructs"
    Course ||--|{ Cohort : "has instances"
    User ||--o{ Enrollment : "signs up"
    Cohort ||--o{ Enrollment : "contains"
    Enrollment ||--o| Grade : "has"
```

## 📡 API Endpoints

### 1. Authentication

- `POST /auth/users/` - Register a new user
- `POST /auth/jwt/create/` - Login (Get Access / Refresh Tokens)

### 2. Courses (The Catalog)

_Requires Admin role for Create/Update/Delete._

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/courses/` | List all available training courses. |
| POST | `/api/courses/` | Create a new course syllabus. |
| GET | `/api/courses/{id}/` | View specific course details. |
| PATCH | `/api/courses/{id}/` | Update course pricing or description. |

### 3. Cohorts(Scheduled Classes)

_Links Courses to Instructors. Requires Admin role for changes._

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/cohorts/` | List all active/upcoming cohorts. |
| POST | `/api/cohorts/` | Schedule a new cohort instance. |
| GET | `/api/cohorts/{id}/` | View cohort details (including instructor name). |

### 4. Enrollments

- `GET /api/enrollments/` - List enrollments (Students see only theirs; Staff see all).
- `POST /api/enrollments/` - Join a cohort(Auto-assogn the logged-in student).
- `GET /api/enrollments/{id}/` - View details including nested Grade data.

### 5. Grading

- `GET /api/grades/` - View student performance records.
- `POST /api/grades/` - Assign a grade to an enrollment (**Instructor/Admin only**)

## Permissions

- **Public (Anon):** Can view (GET) Courses and Cohorts.
- **Authenticated Users:** Can view their own profiles.
- **Admins:** Full access to Create (POST), Update(PUT), and Delete (DELETE) resources.

## 🔒 Business Logic

1. **Validation:** `Enrollment.save()` checks the current cohort count against `capacity`. If full, the request is rejected with a `400 Bad Request`.
2. **Automation:** When a `Grade` is saved, the linked `Enrollment.status` is automatically updated to `COMPLETED`.
3. **Security:** Students are prevented from enrolling other users or modifying their own grades via strict `perform_create` overrides and custom permissions.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeture`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Local Setup Guide

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python installed
- PostgreSQL installed and running

### 2. Installation

1. **Clone the repository** (if using git)

    ```bash
    git clone <repo-url>
    cd training_center_api
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Variables**

    Create a `.env` file in the root directory and add your database credentials:

    ```text
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://YOUR_DB_USER:YOUR_DB_PASSWORD@127.0.0.1:5432/training_center_db
    ```

    _Note: Ensure you have a PostgreSQL database named `training_center_db` created locally._

5. **Initialize the Database**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create Admin User**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Server**

    ```bash
    python manage.py runserver
    ```

    Access the API at `http://127.0.0.1:8000/`.
