# 🎓 MyLMS — Learning Management System (Beginner Django Project)

A simple, beginner-friendly **Learning Management System (LMS)** built with Django that demonstrates how online courses, users, enrollments, and notifications can work together.  
This project mimics the structure of real-world LMS websites like **Udemy** or **Coursera**, while staying simple enough for students and beginners.

---

## 📋 Table of Contents

- [Features Overview](#-features-overview)
- [Feature Summary Table](#-feature-summary-table)
- [User Roles & Permissions](#-user-roles--permissions)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup Instructions](#️-setup-instructions)
- [How It Works](#-how-it-works)
- [Frontend Overview](#-frontend-overview)
- [Demo Data (Optional)](#-demo-data-optional)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🚀 Features Overview

### 🧑‍💻 Core Features
- User **registration**, **login**, and **logout** with Django authentication.  
- **Role-based access control** (Student, Instructor, Sponsor, Admin).  
- Full **CRUD functionality** for courses, sectors, and subjects.  
- Students can **enroll** in courses and view progress.  
- Sponsors can **fund courses** for students.  
- Simple **notification system** for important updates.

### 🖥️ Frontend
- Responsive design using **Bootstrap 5**.  
- A beautiful **home page** showing demo courses and sectors.  
- Dynamic navigation bar that updates based on login state.  
- User dashboard with personalized info and counts.  

### ⚙️ Backend
- Structured, modular Django apps for maintainability.  
- Uses Django ORM and SQLite database for easy setup.  
- Built-in **admin panel** for managing data.  

---

## ✅ Feature Summary Table

| Feature | Description | Status |
|----------|--------------|--------|
| **User Authentication** | Login, Register, Logout | ✅ |
| **Role-Based Access** | Admin, Instructor, Student, Sponsor | ✅ |
| **Course Management** | Add, Edit, Delete Courses (CRUD) | ✅ |
| **Sector & Subject Management** | Group courses by sectors/subjects | ✅ |
| **Enrollment System** | Students enroll in available courses | ✅ |
| **Sponsor Management** | Sponsors fund student enrollments | ✅ |
| **Notification System** | Display alerts for new enrollments | ✅ |
| **Dashboard View** | Role-specific dashboard pages | ✅ |
| **Admin Panel** | Manage users, courses, enrollments | ✅ |
| **Responsive Frontend** | Bootstrap-based, mobile friendly | ✅ |
| **Demo Courses on Homepage** | Shown dynamically or as placeholders | ✅ |
| **Error-Free Migrations** | Tested on Django 5.2.7 | ✅ |

---

## 👥 User Roles & Permissions

| Role | Description | Permissions |
|------|--------------|--------------|
| **Admin** | Superuser who manages all modules. | Full access (Users, Courses, Enrollments, Notifications). |
| **Instructor** | Creates and manages their own courses. | Add/Edit/Delete courses, view students. |
| **Student** | Enrolls in courses and tracks progress. | View courses, enroll, and access dashboard. |
| **Sponsor** | Provides funding for student enrollments. | Manage sponsorship records. |

---

## 🛠 Tech Stack

- **Language:** Python 3.13  
- **Framework:** Django 5.2.7  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Environment:** Virtualenv  
- **Version Control:** Git + GitHub  

---

## 📂 Project Structure

```
lms/
├── accounts/           # User management, authentication, dashboards
├── courses/            # Course, subject, sector models & CRUD
├── enrollments/        # Enrollments and student tracking
├── notifications/      # Notification handling
├── sponsors/           # Sponsor records and funding
├── templates/          # HTML templates
├── static/             # CSS, JS, and assets
├── lms/                # Main Django project configuration
├── manage.py           # Django management tool
└── README.md           # This file
```

---

## ⚙️ Setup Instructions

### Step 1 — Clone the Repository
```bash
git clone https://github.com/Manav-1200/lms.git
cd lms
```

### Step 2 — Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
```

### Step 3 — Install Requirements
```bash
pip install -r requirements.txt
```

### Step 4 — Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5 — Create Superuser
```bash
python manage.py createsuperuser
```

### Step 6 — Run Development Server
```bash
python manage.py runserver
```

### Step 7 — Visit App
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the homepage.  
Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧭 How It Works

1. **Home Page:**  
   Shows a clean introduction, login/register buttons, and demo sectors and courses.  
2. **User Registration:**  
   Users register and are automatically assigned roles (default: Student).  
3. **Dashboard:**  
   Displays a summary of user’s activities and counts of enrollments, notifications, etc.  
4. **Admin Panel:**  
   Admins can manage users, courses, sectors, subjects, and sponsors.  
5. **Course Page:**  
   Shows available courses with CRUD options for authorized users.  
6. **Enrollments:**  
   Students enroll and appear under the Enrollments app.  
7. **Notifications:**  
   Simple alert system triggered for key events like new enrollments.  

---

## 💅 Frontend Overview

| Template | Description |
|-----------|--------------|
| `base.html` | Shared layout with navigation and footer. |
| `accounts/welcome.html` | Landing page with demo sectors & featured courses. |
| `accounts/login.html` | Login page for all users. |
| `accounts/register.html` | Registration form. |
| `accounts/dashboard.html` | Displays user-specific data. |
| `accounts/profile.html` | Shows profile info. |

---

## 🧰 Demo Data (Optional)

To show sample sectors and courses:

1. Visit **Django Admin Panel** → `http://127.0.0.1:8000/admin/`
2. Add sectors like:
   - Information Technology  
   - Business Management  
   - Arts & Design  
3. Add demo courses:
   - “Python for Beginners” under IT  
   - “Intro to Marketing” under Business  
   - “Creative Design Basics” under Arts  

These will appear automatically on the home page.

---

## 🌱 Future Enhancements

- Quiz/Assignments integration  
- Progress tracking for enrolled students  
- Course reviews & ratings  
- Instructor analytics dashboard  
- Payment and sponsorship tracking system  
- REST API support (Django REST Framework)

---

## 🧑‍🎓 Author

**Manav Neupane**  
> A beginner Django developer building this LMS to understand web development fundamentals, authentication, and CRUD systems.

📧 *Email (Optional)*: `manav.neupane1@gmail.com`  
🌐 *GitHub*:https://github.com/Manav-1200
