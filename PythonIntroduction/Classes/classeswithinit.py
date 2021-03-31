class student:
    pass
#object

student_1 = student()
student_2 = student()

student_1.name = 'Alfa'
student_1.age  = 30

student_2.name = 'Beta'
student_2.age  =  '33'

print(student_1.age)
print(student_2.name)

class student:
    def __init__(self, name,age):
        self.name=name
        self.age = age
        student_1 =student('alfa', 30)
        student_2 =student('beta', 33)

    print(student_1.name)
    print(student_2.age)


