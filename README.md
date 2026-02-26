# 🎓 Training Center Management API

**A high-performance, secure backend for modern vocational institutions.**

This robust RESTFUL API built with **Django** and **Django REST Framework (DRF)** designed to manage educational workflows, including student enrollments, course management, cohort tracking, and grading systems.

## 🚀 Live Demo

### API Documentation (Swagger UI)

<https://eliud.pythonanywhere.com/>

*Note: The root URL automatically redirects to the interactive API documentation.*

## 🛠 Features

- **Full CRUD Functionality:** Manage Courses, Cohorts, Students, and Grades via a standardized interface.
- **Interactive Documents:** Intergrated **Swagger/OpenAPI** and **Redoc** for real-time endpoint testing.
- **Advanced Filtering & Search:** Filter grades by specific `student` or `course` IDs.
  - Search through comments and student usernames using **django-filter**.
- **Secure Configuration:** Uses `python-dotenv` for environment variable management to keep sensitive keys out of version control.

## 🏗 Tech Stack

- **Backend:** Python 3.12+, Django 4.2+
- **API Engine:** Django REST Framework
- **Database:** SQLite (Database-agnostic configuration ready for PostgreSQL migration)
- **Documentation:** drf-spectacular
- **Hosting:** PythonAnywhere

## 🚦 Getting Started (Local Setup)

To run this project locally, follow these steps:

1. **Clone the repository**

    ```Bash
    git clone https://github.com/eliud-byte/training_center_api.git
    cd training_center_api
    ```

2. **Create and activate a virtual environment:**

    ```Bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```Bash
    pip install -r requirements.txt
    ```

4. **Configuration Environment Variables:**

    ```Plaintext
      SECRET_KEY=your-secret-key
      DEBUG=True
      ALLOWED_HOSTS=127.0.0.1,localhost
    ```

5. **Run Migrations & Start Server:**

    ```Bash
      python manage.py migrate
      python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/api/docs/`.

## 📖 API Endpoints Summary

| **Endpoint** | **Method** | **Description** |
| :--- | :--- | :--- |
| `/api/courses/` | GET/POST | List or create courses |
| `/api/cohorts/` | GET/POST | List or create cohorts |
| `/api/grades/` | GET/POST | List or create grades (Supports filtering) |
| `/api/docs/` | GET | Interactive Swagger UI |

## 🛡 Security & Best Practices

- **Environment Isolation:** All secrets are managed via `.env` files.
- **Static Assets Management:** Implements `CompressedManifestStaticFilesStorage` to ensure caching efficiency and prevent broken styles.
- **Scalability**: ViewSets and Routers are used to keep code DRY (Don't Repeat Yourself) and maintainable.
