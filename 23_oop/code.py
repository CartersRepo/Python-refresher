student = {"name":"Rolf", "grades":(89,90,93,78,90)}

def average(sequence):
    return sum(sequence)/ len(sequence)

print(average(student["grades"]))




class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (89,90,93,78,90)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades)

#Both work the same:
print(student.average())
print(Student.average(student))