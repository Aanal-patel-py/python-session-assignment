from dataclasses import dataclass,field
from datetime import date
import re

@dataclass
class Employee:
    id: int
    name:str
    email:str
    salary: int
    dept: str =field()  
    hire_date: date

    def __post_init__(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern,self.email):
            raise TypeError("email format not proper")
        
        if self.salary<0:
            raise ValueError("salary must be greater than 0")
    def __str__(self):
        return f"id: {self.id}, name: {self.name},email:{self.email},salary: {self.salary}, dept: {self.dept},hire_date:{self.hire_date}"
        

x=Employee(1,'abc','abc@gmail.com',2000,'python',"2025-11-11")
print(x)