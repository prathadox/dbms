# Student Management System

A full-featured Flask web application for managing student records, attendance, and departments with MySQL database backend. Built as a DBMS mini-project demonstrating CRUD operations, authentication, and database triggers.

## ✨ Key Features

### 🎓 Student Management
- **Add Students**: Create new student records with roll number, name, semester, gender, branch, email, phone, and address
- **View All Students**: Display complete list of all enrolled students
- **Edit Records**: Update existing student information (login required)
- **Delete Students**: Remove student records with automatic trigger logging (login required)
- **Search Students**: Find students by roll number with instant results
- **View Details**: See student information along with attendance records

### 🏢 Department Management  
- **Add Departments**: Create new academic departments/branches
- **Duplicate Prevention**: Automatic validation to prevent duplicate departments
- **Department Listing**: View all available departments
- **Branch Assignment**: Assign students to specific departments

### 📊 Attendance System
- **Record Attendance**: Track attendance percentage for each student
- **Roll Number Based**: Link attendance to student roll numbers
- **View History**: Check attendance records when searching students
- **Bulk Management**: Handle attendance for multiple students

### 🔐 User Authentication
- **User Registration**: Signup with username, email, and password
- **Secure Login**: Session-based authentication with Flask-Login
- **Email Validation**: Prevent duplicate email registrations
- **Protected Routes**: Login required for add/edit/delete operations
- **Logout**: Secure session termination

### 📝 Database Triggers & Audit Logging
- **Auto-Logging**: Automatic tracking of all student record changes
- **Trigger Events**:
  - INSERT: Logs when new students are added
  - UPDATE: Tracks modifications to student records  
  - DELETE: Records when students are removed
- **Timestamp Tracking**: Each action recorded with date/time
- **Audit Trail**: View complete history at `/triggers` route

### 🎨 User Interface
- **Modern Bootstrap Design**: Clean, professional interface
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Flash Messages**: User feedback for all actions (success, warnings, errors)
- **Font Awesome Icons**: Visual indicators throughout
- **AOS Animations**: Smooth scroll animations
- **Owl Carousel**: Image carousels and sliders

---

## 🚀 Quick Start (If Already Set Up)

**Server Already Running?** Check with:
```bash
ps aux | grep "python main.py" | grep -v grep
curl http://localhost:5000/test
```

If running, just open http://localhost:5000 in your browser!

To stop the server:
```bash
pkill -f "python main.py"
```

---

## 📋 Prerequisites

- Python 3.8+ (tested with Python 3.14)
- MySQL or MariaDB
- pip and virtualenv

## 📦 Requirements Files Explained

- **`requirements.txt`**: Minimal essential dependencies (USE THIS ONE)
- **`requirements_working.txt`**: Full pip freeze output (for reference only, not needed)

## Quick Setup

### 1. Install MySQL/MariaDB

**Arch Linux:**
```bash
sudo pacman -S mysql
sudo systemctl start mysql
sudo mysql_secure_installation
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation
```

### 2. Create Database

Login to MySQL:
```bash
mysql -u root -p
```

Create the database and import schema:
```sql
CREATE DATABASE students;
USE students;
SOURCE /path/to/students.sql;
EXIT;
```

Or from command line:
```bash
mysql -u root -p students < students.sql
```

### 3. Setup Python Environment

```bash
cd "student management"
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure Database Connection

Edit `main.py` line 26 and update with your MySQL credentials:

```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:YOUR_PASSWORD@localhost/students'
```

If your MySQL root user has no password:
```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/students'
```

Or without the colon:
```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/students'
```

### 6. Run the Application

**⚠️ IMPORTANT: Always activate virtual environment first!**

```bash
cd "student management"
source venv/bin/activate  # REQUIRED - activates virtual environment
python main.py
```

**Or use the run script:**
```bash
cd "student management"
./run.sh
```

The application will start on **http://localhost:5000**

**Common Error:** `ModuleNotFoundError: No module named 'flask'`
- **Solution**: You forgot to activate the virtual environment. Run `source venv/bin/activate` first!

**Running in Background (optional):**
```bash
# Run in background
nohup python main.py > flask.log 2>&1 &

# Check if running
ps aux | grep "python main.py" | grep -v grep

# Stop the server
pkill -f "python main.py"

# View logs
tail -f flask.log
```

### 7. Access the Application

Open your browser and navigate to:
- Homepage: http://localhost:5000
- Test DB Connection: http://localhost:5000/test
- Login: http://localhost:5000/login
- Signup: http://localhost:5000/signup

---

## 📖 What This Project Does

This is a **Student Management System (SMS)** web application that demonstrates complete **CRUD (Create, Read, Update, Delete) operations** with a MySQL database. It's built as a DBMS mini-project showcasing:

- **Full CRUD functionality** for student records
- **Database triggers** that automatically log all changes
- **User authentication** with protected routes
- **Attendance tracking** system
- **Department/branch management**
- **Search functionality** by roll number

### Project Purpose

This project serves as a practical demonstration of:
1. **Database Operations**: Creating, reading, updating, and deleting records in MySQL
2. **Database Triggers**: Automatic audit logging of all data changes
3. **Web Application Development**: Building a functional web app with Flask
4. **User Authentication**: Implementing login/logout with session management
5. **Frontend-Backend Integration**: Connecting HTML forms to database operations

---

## 🔧 How to Perform CRUD Operations

### **CREATE** - Add New Students

1. **Login First** (required for add/edit/delete):
   - Go to http://localhost:5000/signup to create an account
   - Or login at http://localhost:5000/login

2. **Add Departments** (if needed):
   - Navigate to http://localhost:5000/department
   - Enter department name (e.g., "Computer Science", "Electronics")
   - Click "Add Department"
   - You'll see: "Department Addes" (success message)

3. **Add a Student**:
   - Click **"Students"** in the navigation bar → http://localhost:5000/addstudent
   - Fill in the form:
     - **Roll Number**: e.g., "1ve17cs012"
     - **Student Name**: Full name
     - **Semester**: 1-8
     - **Gender**: Select from dropdown (Male/Female)
     - **Branch**: Select from departments you created
     - **Email**: Student email address
     - **Phone Number**: Contact number
     - **Address**: Full address
   - Click **"Add Record"**
   - Success message: **"Booking Confirmed"**
   - **Database trigger automatically logs**: "STUDENT INSERTED" with timestamp

### **READ** - View Students

#### View All Students:
- Click **"Student Details"** in navbar → http://localhost:5000/studentdetails
- Displays a complete table showing:
  - Student ID, Roll Number, Name, Semester, Gender
  - Branch, Email, Phone Number, Address
  - Edit/Delete buttons (if logged in)

#### Search Specific Student:
- Click **"Search"** in navbar → http://localhost:5000/search
- Enter a roll number (case-sensitive)
- Shows:
  - Complete student details (roll no, name, sem, gender, branch, email, phone, address)
  - **Attendance percentage** for that student

### **UPDATE** - Edit Student Records

**Prerequisites**: Must be logged in

1. Go to http://localhost:5000/studentdetails
2. Find the student you want to edit
3. Click the **"Edit"** button next to the student
4. URL becomes: `http://localhost:5000/edit/<student_id>`
5. Modify any fields in the form:
   - Roll Number, Name, Semester, Gender
   - Branch (select from dropdown)
   - Email, Phone, Address
6. Click submit
7. Success message: **"Slot is Updates"**
8. **Database trigger automatically logs**: "STUDENT UPDATED" with timestamp

### **DELETE** - Remove Students

**Prerequisites**: Must be logged in

1. Go to http://localhost:5000/studentdetails
2. Find the student you want to delete
3. Click the **"Delete"** button next to the student
4. Confirm deletion in the popup dialog
5. Student record is permanently removed
6. Success message: **"Slot Deleted Successful"**
7. **Database trigger automatically logs**: "STUDENT DELETED" with timestamp

---

## 📝 Complete CRUD Demo Workflow

Here's a step-by-step workflow to demonstrate all CRUD operations:

### Step 1: Setup Departments
```
1. Visit: http://localhost:5000/department
2. Add departments:
   - "Computer Science"
   - "Electronics"
   - "Mechanical"
```

### Step 2: Create User Account
```
1. Visit: http://localhost:5000/signup
2. Enter:
   - Username: admin
   - Email: admin@example.com
   - Password: admin123
3. Click Signup
4. Login at: http://localhost:5000/login
```

### Step 3: CREATE - Add Students
```
1. Click "Students" in navbar
2. Fill form:
   Roll No: TEST001
   Name: John Doe
   Sem: 3
   Gender: Male
   Branch: Computer Science
   Email: john@example.com
   Phone: 1234567890
   Address: 123 Main St
3. Click "Add Record"
4. Verify: Check triggers page - should show "STUDENT INSERTED"
```

### Step 4: READ - View All Students
```
1. Click "Student Details" in navbar
2. See table with all students
3. Verify your newly added student appears
```

### Step 5: READ - Search Specific Student
```
1. Click "Search" in navbar
2. Enter roll number: TEST001
3. View complete details + attendance
```

### Step 6: Add Attendance (Bonus Feature)
```
1. Click "Attendance" in navbar
2. Select roll number from dropdown
3. Enter attendance percentage: 85
4. Click "Add Attendance"
5. Search the student again to see attendance
```

### Step 7: UPDATE - Edit Student
```
1. Go to "Student Details"
2. Click "Edit" next to TEST001
3. Change semester from 3 to 4
4. Change email to newemail@example.com
5. Submit
6. Verify: Check triggers page - should show "STUDENT UPDATED"
```

### Step 8: DELETE - Remove Student
```
1. Go to "Student Details"
2. Click "Delete" next to TEST001
3. Confirm deletion
4. Verify student removed from table
5. Check triggers page - should show "STUDENT DELETED"
```

### Step 9: View Audit Log (Database Triggers)
```
1. Click "Records" in navbar → http://localhost:5000/triggers
2. See complete audit trail:
   - TID (Trigger ID)
   - Roll Number
   - Action (STUDENT INSERTED/UPDATED/DELETED)
   - Timestamp (exact date/time of change)
```

---

## 🔍 Understanding the CRUD Operations

### What Happens Behind the Scenes:

**CREATE** (`/addstudent`):
```python
# User fills form → POST request
Student(rollno, sname, sem, gender, branch, email, number, address)
db.session.add(query)
db.session.commit()
# Database trigger fires → Logs "STUDENT INSERTED"
```

**READ** (`/studentdetails` or `/search`):
```python
# GET request → Query database
Student.query.all()  # All students
Student.query.filter_by(rollno=rollno).first()  # Specific student
# Returns data → Rendered in HTML template
```

**UPDATE** (`/edit/<id>`):
```python
# User modifies form → POST request
post = Student.query.filter_by(id=id).first()
post.rollno = new_rollno
post.sname = new_name
# ... update all fields
db.session.commit()
# Database trigger fires → Logs "STUDENT UPDATED"
```

**DELETE** (`/delete/<id>`):
```python
# User clicks delete → POST request
post = Student.query.filter_by(id=id).first()
db.session.delete(post)
db.session.commit()
# Database trigger fires BEFORE delete → Logs "STUDENT DELETED"
```

---

## 🎯 Quick Reference: All Routes

| Route | Method | Description | Auth Required |
|-------|--------|-------------|---------------|
| `/` | GET | Homepage | No |
| `/login` | GET/POST | User login | No |
| `/signup` | GET/POST | User registration | No |
| `/logout` | GET | User logout | Yes |
| `/addstudent` | GET/POST | **CREATE** - Add new student | Yes |
| `/studentdetails` | GET | **READ** - View all students | No |
| `/edit/<id>` | GET/POST | **UPDATE** - Edit student | Yes |
| `/delete/<id>` | POST | **DELETE** - Remove student | Yes |
| `/search` | GET/POST | **READ** - Search by roll number | No |
| `/department` | GET/POST | Add/manage departments | No |
| `/addattendance` | GET/POST | Record attendance | No |
| `/triggers` | GET | View audit log (trigger records) | No |
| `/test` | GET | Test database connection | No |

## Project Structure

```
student management/
├── main.py              # Flask application with routes and models
├── students.sql         # Database schema with tables and triggers
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── templates/          # HTML templates (Jinja2)
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── student.html
│   ├── studentdetails.html
│   ├── attendance.html
│   ├── department.html
│   ├── search.html
│   ├── triggers.html
│   └── ...
└── static/            # Static assets
    ├── assets/
    │   ├── css/
    │   ├── js/
    │   └── vendor/   # Bootstrap, jQuery, etc.
    ├── css/
    └── images/
```

## Database Schema

The application uses the following tables:

- **student**: Student records (id, rollno, sname, sem, gender, branch, email, number, address)
- **user**: User authentication (id, username, email, password)
- **department**: Academic departments (cid, branch)
- **attendence**: Attendance records (aid, rollno, attendance)
- **trig**: Audit log for student changes (tid, rollno, action, timestamp)
- **test**: Database connection test table

## Usage

### First Time Setup

1. **Create an Account**: Navigate to http://localhost:5000/signup and create a user account
2. **Login**: Use your credentials to login at http://localhost:5000/login
3. **Add Departments**: Go to the Department page and add academic departments
4. **Add Students**: Use the Student form to add student records
5. **Manage Attendance**: Record attendance for students
6. **Search Students**: Search for student records by roll number

### Routes

- `/` - Homepage
- `/login` - User login
- `/signup` - User registration
- `/logout` - Logout current user
- `/addstudent` - Add new student (requires login)
- `/studentdetails` - View all students
- `/edit/<id>` - Edit student record (requires login)
- `/delete/<id>` - Delete student (requires login)
- `/department` - Manage departments
- `/addattendance` - Record attendance
- `/search` - Search students by roll number
- `/triggers` - View audit log
- `/test` - Test database connection

## Troubleshooting

### Issue: `mysqlclient` Installation Fails

**Solution**: The app now uses `pymysql` which is pure Python and doesn't require compilation.

If you still want to use `mysqlclient`:
```bash
# Arch Linux
sudo pacman -S mariadb-libs base-devel

# Ubuntu/Debian
sudo apt install default-libmysqlclient-dev build-essential

pip install mysqlclient
```

Then update the connection URI to use `mysql://` instead of `mysql+pymysql://`

### Issue: Cannot Connect to Database

**Check if MySQL is running:**
```bash
sudo systemctl status mysql
```

**Verify database exists:**
```bash
mysql -u root -p -e "SHOW DATABASES;"
```

**Check credentials in main.py** (line 26)

### Issue: Port 5000 Already in Use

Change the port in `main.py` (last line):
```python
app.run(debug=True, port=5001)
```

### Issue: Flask Import Errors

Make sure you're using the virtual environment:
```bash
source venv/bin/activate
pip list  # Verify packages are installed
```

### Issue: Permission Denied on MySQL

Grant privileges to your user:
```sql
GRANT ALL PRIVILEGES ON students.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

## 🔒 Security Notes

⚠️ **IMPORTANT: Update These Before Use**

### Critical Security Issues to Fix:

1. **Database Password Exposed**: Line 26 in `main.py` contains hardcoded password. Change it:
   ```python
   # CHANGE THIS LINE IN main.py:
   app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:YOUR_PASSWORD@localhost/students'
   ```
   **Better approach**: Use environment variables:
   ```python
   import os
   DB_PASSWORD = os.getenv('DB_PASSWORD', '')
   app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://root:{DB_PASSWORD}@localhost/students'
   ```

2. **Secret Key**: Change the secret key in `main.py` line 12 to a random string:
   ```python
   import secrets
   app.secret_key = secrets.token_hex(32)  # Or use environment variable
   ```

3. **Password Hashing**: Current implementation stores user passwords in **plain text**. For production, enable password hashing (lines 181, 204 in main.py):
   ```python
   # In signup route (line 181):
   encpassword = generate_password_hash(password)
   newuser=User(username=username, email=email, password=encpassword)
   
   # In login route (line 204):
   if user and check_password_hash(user.password, password):
   ```

4. **Debug Mode**: Set `debug=False` in production (line 255):
   ```python
   if __name__ == '__main__':
       app.run(debug=False, host='0.0.0.0')
   ```

5. **Database Credentials**: Never commit credentials to version control. Use `.gitignore`:
   ```
   .env
   *.log
   __pycache__/
   venv/
   ```

6. **SQL Injection**: Current code uses SQLAlchemy ORM which provides protection, but be careful with raw queries

### Production Deployment Checklist:
- [ ] Change database password in main.py
- [ ] Use environment variables for secrets
- [ ] Enable password hashing
- [ ] Set debug=False
- [ ] Use a production WSGI server (Gunicorn/uWSGI)
- [ ] Set up HTTPS
- [ ] Configure firewall rules
- [ ] Regular database backups

## 🛠️ Technology Stack

### Backend
- **Python 3.14** - Programming language
- **Flask 3.1.2** - Web framework
- **Flask-SQLAlchemy 3.1.1** - Database ORM wrapper
- **Flask-Login 0.6.3** - User session management
- **SQLAlchemy 2.0.44** - Object-Relational Mapping (ORM)
- **Werkzeug 3.1.3** - WSGI utility library (Flask dependency)
- **PyMySQL 1.1.2** - Pure Python MySQL client library
- **Jinja2 3.1.6** - Template engine for rendering HTML
- **itsdangerous 2.2.0** - Secure data signing/serialization

### Database
- **MySQL/MariaDB** - Relational database management system
- **Database Triggers** - Automatic audit logging (INSERT/UPDATE/DELETE)

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling
- **Bootstrap 5** - CSS framework for responsive UI
- **JavaScript (ES5/ES6)** - Client-side scripting

### JavaScript Libraries & Plugins
- **jQuery** - DOM manipulation and AJAX
- **jQuery Easing** - Animation easing functions
- **Bootstrap Bundle** - Bootstrap JS components (modals, dropdowns, etc.)
- **AOS (Animate On Scroll)** - Scroll animation library
- **Owl Carousel** - Image/content carousel slider
- **Venobox** - Lightbox/modal gallery
- **Font Awesome** - Icon library
- **Superfish** - Multi-level dropdown menu
- **HoverIntent** - Hover intent detection
- **PHP Email Form (validate.js)** - Form validation (JS port)

### Development Tools
- **Python Virtual Environment** - Isolated dependency management
- **pip** - Python package manager

### Architecture Pattern
- **MVC (Model-View-Controller)** pattern:
  - **Model**: SQLAlchemy ORM classes (Student, User, Department, etc.)
  - **View**: Jinja2 HTML templates
  - **Controller**: Flask route handlers

### Frontend Architecture
- **Monolithic Structure**: Frontend and backend in the same repository (no separate frontend repo)
- **Template-Based UI**: Using pre-built Bootstrap template **"TheEvent"** from BootstrapMade
- **Plugin-Based**: Using off-the-shelf libraries/plugins, not custom-built components
- **Template Engine**: Jinja2 for server-side rendering (not a separate frontend framework like React/Vue)
- **Custom Code**: Minimal custom CSS/JS (mainly template customization and initialization)

**Frontend Structure:**
```
static/
├── assets/
│   ├── css/
│   │   └── style.css          # Custom styling (template-based)
│   ├── js/
│   │   └── main.js            # Template initialization code
│   └── vendor/                 # Pre-built plugins (Bootstrap, jQuery, etc.)
└── templates/                  # Jinja2 HTML templates (not separate frontend app)
```

### Key Features Implementation
- **Authentication**: Session-based with Flask-Login
- **Database Operations**: SQLAlchemy ORM for type-safe queries
- **Form Handling**: Flask request object with validation
- **Flash Messages**: User feedback system
- **Route Protection**: `@login_required` decorator
- **Database Triggers**: MySQL triggers for audit logging

## Database Triggers

The application includes three triggers on the `student` table:

1. **Insert Trigger**: Logs when a new student is added
2. **Update Trigger**: Logs when a student record is updated
3. **Delete Trigger**: Logs when a student is deleted

View trigger logs at: http://localhost:5000/triggers

## Development

To run in development mode with auto-reload:
```bash
python main.py
```

The Flask debug mode is enabled by default (line 255 in main.py).

## Testing Database Connection

Visit http://localhost:5000/test to verify that the application can connect to the MySQL database.

Expected output:
- Success: "My database is Connected"
- Failure: "My db is not Connected"

## License

This is a DBMS mini-project for educational purposes.

## Contributors

Project created as part of Database Management Systems coursework.

## Support

For issues and questions, refer to the project documentation or database setup guides.

