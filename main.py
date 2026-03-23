from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from schemas import Student
from database import students

app = FastAPI()

@app.get('/')
def welcome():
    return "Welcome to student API"

@app.get("/students")
def get_students(course: Optional[str] = Query(None)):
    if course:
        return [s for s in students if s["course"].lower() == course.lower()]
    return students


@app.post("/students", status_code=201)
def add_student(student: Student):
    global id_counter
    new_student = {
        "id": id_counter,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }
    students.append(new_student)
    id_counter += 1
    return new_student


@app.get("/students/{id}")
def get_student(id: int):
    for s in students:
        if s["id"] == id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")


@app.put("/students/{id}")
def update_student(id: int, student: Student):
    for s in students:
        if s["id"] == id:
            s["name"] = student.name
            s["age"] = student.age
            s["course"] = student.course
            return s
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{id}")
def delete_student(id: int):
    for i, s in enumerate(students):
        if s["id"] == id:
            students.pop(i)
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")