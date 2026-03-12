from dataclasses import dataclass, field
@dataclass
class Car:
    name: str
    model: str
    year: int
    color: str = field(repr=False)

c=Car('abc','efg',2021,'black')
print(c)