from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict



class Employee(BaseModel):
    name: str
    age: int
    process: str
    salary: int
    perfomance:List[str] = []  #default value for list and optional class show = none 
    email: EmailStr  #default value for email and optional class show = none
    website: AnyUrl = None  #default value for URL and optional class show = none


def show_employee_data(employee: Employee):
    print(employee.name)
    print(employee.age)
    print(employee.process)
    print(employee.salary)
    print(employee.perfomance)
    print(employee.email)
    print(employee.website)


employee_data = {
    "name": "rishika",
    "age": 20,
    "process": "data science",
    "salary": 50000,
    "perfomance": ["good", "excellent"],
    "email": "rishika12@gmail.com",
    "website": "https://www.rishika.com"

}

employee1 = Employee(**employee_data)  #star define dictionary unpacking

(show_employee_data(employee=employee1))

