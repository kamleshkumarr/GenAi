
# Pydantic is a data validation and data parsing library for python.
# from pydantic import BaseModel  #importing basemodel from pydantic library
# class Student(BaseModel): #Inherit Basemodel

#     name: str  # parameter
# new_student = {'name':'Kamlesh'}
# student = Student(**new_student)
# print(type(student))   # If we put any integera at place of name {'name': 32} it will give error. we can't put any integer at place of string.




# Iporting Optinal from typing
# from typing import Optional
# class Student(BaseModel):

#     name: str = 'Kamlesh' # default name 
#     age: Optional[int] = None # It is optinal, if you set your age value it will show , if you don't give any number in field of integer it will not throw error cause it is optinal field

# new_student = {'age':32}

# student = Student(**new_student)

# print(student)


# if we send data in this format 
# new_student = {'age':'32'}  # Then pydantic is very smart it automatically convert this string number into integer



# Email validation

# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class Student(BaseModel):
#     name: str = 'Kamlesh'
#     age: Optional[int] = None
#     email: EmailStr

# new_student = {'age':'32', 'email':'abc@gmail.com'}
# student = Student(**new_student)
# print(student)    


# Field constraints

from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str ='Kamlesh'
    cgpa: float = Field(gt=0, lt=10, default=5)

new_student = {'cgpa':9}

student = Student(**new_student)
print(student)

# we can also convert it into dictonary

student_dict = dict(student)
print(student_dict['name'])

# Can also be converted into json Format

student_json = student.model_dump_json(student)
print(student_json)