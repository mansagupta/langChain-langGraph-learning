from pydantic import BaseModel, EmailStr, Field
from typing import Optional
# Pydantic is a data validation and data parsing library in python

class Student(BaseModel):
    name: str = 'mansa'
    age: Optional[int] = None
    email: EmailStr # validates email
    cgpa: float = Field(gt=0, lt=10, default= 5, description= "something") # sets constraints, add description , regex and can provide default value

new_student = {'name': 'mansa', 'email': 'abc@gmail.com', 'cgpa': 6}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()

print(student_json)