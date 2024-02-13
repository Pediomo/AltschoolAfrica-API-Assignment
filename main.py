from fastapi import FastAPI, HTTPException

app = FastAPI()

# Additional ASGI server configuration and routes


#Create a FastAPI project with the following specifications:

# In-memory storage (Python Dictionary)for students
students = {}

# Model(format) for Student resource 

class Student:
    def __init__(self, name: str, age: int, sex: str, height: float):
        self.id = len(students) + 1
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


 # Home endpoint
@app.get("/")
def home():
    return "Welcome to my API Assignment"       


# Create a Student Resource
        
@app.post("/students/")
def create_student(name: str, age: int, sex: str, height: float):
    student = Student(name, age, sex, height)
    students[student.id] = student
    return {"message": "Student created successfully", "student_id": student.id}


# Retrieve a Student resource by id

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id].__dict__


# Retrieve all Students' Resource

@app.get("/students/")
def get_all_students():
    return [student.__dict__ for student in students.values()]


# Update a Student Resource by id

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id].name = name
    students[student_id].age = age
    students[student_id].sex = sex
    students[student_id].height = height
    return {"message": "Student updated successfully", "student_id": student_id}


# Delete a Student Resource by id

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted successfully", "student_id": student_id}


