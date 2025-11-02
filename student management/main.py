from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
import json

# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='kusumachandashwini'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:2206@localhost/students'# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
db=SQLAlchemy(app)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Department(db.Model):
    cid=db.Column(db.Integer,primary_key=True)
    branch=db.Column(db.String(100))

class Attendence(db.Model):
    aid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    attendance=db.Column(db.Integer())

class Trig(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))





class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(50))
    sname=db.Column(db.String(50))
    sem=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    branch=db.Column(db.String(50))
    email=db.Column(db.String(50))
    number=db.Column(db.String(12))
    address=db.Column(db.String(100))
    

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/studentdetails')
def studentdetails():
    # query=db.engine.execute(f"SELECT * FROM `student`") 
    query=Student.query.all() 
    return render_template('studentdetails.html',query=query)

@app.route('/triggers')
def triggers():
    # query=db.engine.execute(f"SELECT * FROM `trig`") 
    query=Trig.query.all()
    return render_template('triggers.html',query=query)

@app.route('/department',methods=['POST','GET'])
def department():
    if request.method=="POST":
        dept=request.form.get('dept')
        if not dept or dept.strip() == '':
            flash("Department name cannot be empty","danger")
            return redirect('/department')
        query=Department.query.filter_by(branch=dept).first()
        if query:
            flash("Department Already Exists","warning")
            return redirect('/department')
        try:
            dep=Department(branch=dept)
            db.session.add(dep)
            db.session.commit()
            flash("Department Added Successfully","success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding department: {str(e)}","danger")
    return render_template('department.html')

@app.route('/addattendance',methods=['POST','GET'])
def addattendance():
    # query=db.engine.execute(f"SELECT * FROM `student`") 
    query=Student.query.all()
    if request.method=="POST":
        rollno=request.form.get('rollno')
        attend=request.form.get('attend')
        
        # Validation
        if not rollno or rollno == 'Select RollNo':
            flash("Please select a roll number","danger")
            return render_template('attendance.html',query=query)
        if not attend or attend.strip() == '':
            flash("Attendance percentage cannot be empty","danger")
            return render_template('attendance.html',query=query)
        
        try:
            attendance_value = int(attend)
            if attendance_value < 0 or attendance_value > 100:
                flash("Attendance must be between 0 and 100","danger")
                return render_template('attendance.html',query=query)
                
            atte=Attendence(rollno=rollno,attendance=attendance_value)
            db.session.add(atte)
            db.session.commit()
            flash("Attendance Added Successfully","success")
        except ValueError:
            flash("Attendance must be a valid number","danger")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding attendance: {str(e)}","danger")

        
    return render_template('attendance.html',query=query)

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method=="POST":
        rollno=request.form.get('roll')
        bio=Student.query.filter_by(rollno=rollno).first()
        attend=Attendence.query.filter_by(rollno=rollno).first()
        return render_template('search.html',bio=bio,attend=attend)
        
    return render_template('search.html')

@app.route("/delete/<string:id>",methods=['POST','GET'])
@login_required
def delete(id):
    try:
        post=Student.query.filter_by(id=id).first()
        if not post:
            flash("Student not found","danger")
            return redirect('/studentdetails')
        db.session.delete(post)
        db.session.commit()
        flash("Student Deleted Successfully","success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting student: {str(e)}","danger")
    return redirect('/studentdetails')


@app.route("/edit/<string:id>",methods=['POST','GET'])
@login_required
def edit(id):
    # dept=db.engine.execute("SELECT * FROM `department`")    
    if request.method=="POST":
        rollno=request.form.get('rollno')
        sname=request.form.get('sname')
        sem=request.form.get('sem')
        gender=request.form.get('gender')
        branch=request.form.get('branch')
        email=request.form.get('email')
        num=request.form.get('num')
        address=request.form.get('address')
        
        # Validation
        if not rollno or not sname or not email:
            flash("Roll number, name, and email are required","danger")
            dept=Department.query.all()
            posts=Student.query.filter_by(id=id).first()
            return render_template('edit.html',posts=posts,dept=dept)
        
        try:
            post=Student.query.filter_by(id=id).first()
            if not post:
                flash("Student not found","danger")
                return redirect('/studentdetails')
            post.rollno=rollno
            post.sname=sname
            post.sem=sem
            post.gender=gender
            post.branch=branch
            post.email=email
            post.number=num
            post.address=address
            db.session.commit()
            flash("Student Updated Successfully","success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating student: {str(e)}","danger")
        return redirect('/studentdetails')
    dept=Department.query.all()
    posts=Student.query.filter_by(id=id).first()
    if not posts:
        flash("Student not found","danger")
        return redirect('/studentdetails')
    return render_template('edit.html',posts=posts,dept=dept)


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        
        # Validation
        if not username or not email or not password:
            flash("All fields are required","danger")
            return render_template('/signup.html')
        
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exists","warning")
            return render_template('/signup.html')
        
        try:
            # encpassword=generate_password_hash(password)
            # this is method 2 to save data in db
            newuser=User(username=username,email=email,password=password)
            db.session.add(newuser)
            db.session.commit()
            flash("Signup Successful! Please Login","success")
            return render_template('login.html')
        except Exception as e:
            db.session.rollback()
            flash(f"Error creating account: {str(e)}","danger")

          

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        
        # Validation
        if not email or not password:
            flash("Email and password are required","danger")
            return render_template('login.html')
        
        user=User.query.filter_by(email=email).first()

        # if user and check_password_hash(user.password,password):
        if user and user.password == password:
            login_user(user)
            flash("Login Successful","success")
            return redirect(url_for('index'))
        else:
            flash("Invalid Credentials","danger")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successful","success")
    return redirect(url_for('login'))



@app.route('/addstudent',methods=['POST','GET'])
@login_required
def addstudent():
    # dept=db.engine.execute("SELECT * FROM `department`")
    dept=Department.query.all()
    if request.method=="POST":
        rollno=request.form.get('rollno')
        sname=request.form.get('sname')
        sem=request.form.get('sem')
        gender=request.form.get('gender')
        branch=request.form.get('branch')
        email=request.form.get('email')
        num=request.form.get('num')
        address=request.form.get('address')
        
        # Validation
        if not rollno or not sname or not email:
            flash("Roll number, name, and email are required","danger")
            return render_template('student.html',dept=dept)
        if gender == 'Select Gender':
            flash("Please select a gender","danger")
            return render_template('student.html',dept=dept)
        if branch == 'Select Branch':
            flash("Please select a branch","danger")
            return render_template('student.html',dept=dept)
        
        # Check if student already exists
        existing_student = Student.query.filter_by(rollno=rollno).first()
        if existing_student:
            flash("Student with this roll number already exists","warning")
            return render_template('student.html',dept=dept)
        
        try:
            query=Student(rollno=rollno,sname=sname,sem=sem,gender=gender,branch=branch,email=email,number=num,address=address)
            db.session.add(query)
            db.session.commit()
            flash("Student Added Successfully","success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding student: {str(e)}","danger")


    return render_template('student.html',dept=dept)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'


app.run(debug=True)    