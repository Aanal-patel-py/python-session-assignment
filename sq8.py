from dataclasses import dataclass,field
from datetime import date
import re

@dataclass(frozen=True, order=True)
class Employee:
    id: int=field(compare=False)
    name:str=field(compare=False)
    email:str=field(compare=False)
    salary: int
    dept: str =field(compare=False)
    hire_date: date=field(compare=False)

    def __post_init__(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern,self.email):
            raise TypeError("email format not proper")
        
        if self.salary<0:
            raise ValueError("salary must be greater than 0")
        
    def __str__(self):
        return f"id: {self.id}, name: {self.name},email:{self.email},salary: {self.salary}, dept: {self.dept},hire_date:{self.hire_date}"
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            id= data["id"],
            name= data["name"],
            email= data["email"],
            salary= data["salary"],
            dept= data["dept"],
            hire_date=data["hire_date"]
        )


emps=[
    Employee(1,'abc','abc@gmail.com',2000,'python',"2025-11-11"),
    Employee(2,'xyz','xyz@gmail.com',5000,'aiml',"2025-11-11"),
    Employee(3,'pqr','pqr@gmail.com',3000,'devops',"2025-11-11"),
    ]
emps.sort()
print(emps)

employee_dict = {
    "id": 1,
    "name": "abc",
    "email": "abc@gmail.com",
    "salary": 2000,
    "dept": "python",
    "hire_date": "2025-11-11"
}
emp=Employee.from_dict(employee_dict)
print(emp)

