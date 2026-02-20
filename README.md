# 🎓 Training Center Management API

**A high-performance, secure backend for modern vocational institutions.**

This API manages the full lifecycle of a training center, from course creation and student enrollment to academic grading and automated progress tracking.

## 🛠 Tech Stack

- **Framework:** Django 6.0 + Django REST Framework (DRF)
- **Auth:** Djoser + SimpleJWT (Bearer Tokens)
- **Database:** SQLite(Dev)  / PostgreSQL (Prod ready)
- **Documentation:** Swagger UI & ReDoc (via drf-spectacular)

## 🌟 Core Features

- **Role-Based Access Controll (RBAC):** Three distinct roles (Admin, Instructor, Student) with granular permisions.
- **Self-Service Enrollment:** Students can browse and join cohorts independently.
- **Smart Business Logic:**
  - **The Bouncer:** Prevents enrollment once a cohort's capacity is reached.
  - **Auto-Graduation:** Automatically moves enrollment status to `COMPLETED` when a grade is posted.
- **API Excellence:**
  - **Filtering & Search:** Find courses by price or title and cohorts by start date.
  - **Pagination:** Standardized 10-item pages for speed.
  - **Throttling:** Protect against brute-force attacks (10 req/min anon, 100 req/min user).

## 📡 Quick Access

- **Interactive Docs:** `/api/docs/` (Swagger) or `/api/redoc/`
- **Authentication:** `auth/jwt/create/` (POST username/password to get token)
