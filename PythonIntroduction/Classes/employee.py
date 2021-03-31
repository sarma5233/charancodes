class employee:
    pass
emp_1 = employee()
emp_2 = employee()

emp_1.name ='Delta'
emp_1.id   =369789
emp_1.department = 'Aerospace'

emp_2.name ='Charlie'
emp_2.id  =369800
emp_2.department = 'IT'

print(emp_1.name)
print(emp_1.department)
print(emp_2.id)
print(emp_2.department)

class employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id   = id
        self.department = department

        emp_1 = employee('alfa', 369789, 'Aerospace')
        emp_2 = employee('Charlie', 369800, 'IT')

    print(emp_1.id)
    print(emp_2.name)