# Student Management System using Django

## Overview

This project is a comprehensive Student Management System developed using Django, a high-level Python web framework. The system allows users to log in as Head of Department (HOD), teacher, or student, each with specific roles and functionalities.

## Features

### 1. User Authentication

- **Login:** Users can log in as HOD, teacher, or student with their respective credentials.
- **Role-Based Access Control (RBAC):** Each role has unique permissions and functionalities.

### 2. HOD Dashboard

- **Add Staff:** HOD can add new staff members to the system, providing essential details.
- **Add Courses:** HOD can add new courses to the system for students to enroll in.
- **Manage Students:** HOD can view and manage student details and assignments.

### 3. Teacher Dashboard

- **Take Attendance:** Teachers can mark attendance for their assigned courses and classes.
- **Feedback System:** Teachers can provide feedback to students and receive feedback from them.
- **Grade Assignments:** Teachers can grade assignments submitted by students.

### 4. Student Dashboard

- **View Courses:** Students can view the list of courses available in the system.
- **Submit Assignments:** Students can submit assignments to their respective teachers.
- **View Attendance:** Students can check their attendance records.

### 5. Attendance Management

- **Automated Attendance:** The system automatically tracks and updates attendance based on teacher input.

### 6. Feedback System

- **Teacher-Student Communication:** Facilitates communication between teachers and students through a feedback system.

### 7. Assignment Management

- **Submit Assignments:** Students can submit assignments online.
- **Grading System:** Teachers can grade assignments and provide feedback.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Debshibraj123/complete_student_mngmnt_system_using_django.git
   cd mysite
# Install dependencies

pip install -r requirements.txt

# Apply database migrations

python manage.py makemigrations 
python manage.py migrate

# Create a superuser account

python manage.py createsuperuser

# Run the development server

python manage.py runserver
