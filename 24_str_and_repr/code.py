class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person is named: {self.name} and is {self.age} years old."
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

#Person.__init__()
bob = Person("Bob", 35)
print(bob)