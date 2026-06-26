from typing import TypedDict  # used to define the key and value in a dictionary

class Person(TypedDict):  
    name: str
    age: int

new_person: Person = {'name': 'mansa', 'age': 22}

print(new_person)