from pydantic import BaseModel , Field
from typing  import Annotated, Optional

class Student(BaseModel):
    name: str
    age:Optional[int] = None
    # email:EmailStr
    cgpa:Annotated[Optional[float], Field(ge=0.0, le=10.0 , default=5 ,description='its a report student')] = None  # CGPA should be between 0.0 and 4.0

#new_student = {'name': 32}  # This will raise a validation error because 'name' should be a string
new_student = {'name': 'Zaid' , 'age':32,'cgpa':8.5}  # This will work correctly


student = Student(**new_student)
print(student)