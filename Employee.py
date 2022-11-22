# Create Class here
class Employee:

    # Class attributes
    os = 'Windows 2010'
    work_style = 'remote'
    hourly_salary = 15

# Constructor method/initializer
# Build the object 
    def __init__(self, role, is_manager, location = 'New York') -> None:
        self.role = role
        self.is_manager = is_manager
        self.location = location

    def bio(self):
        return f'HELLO! I am a {self.role} and i am located in {self.role}'

# Create object/instance
Marian = Employee('Developer', False)
Bob = Employee('QA', True)

print(Marian.role)
print(Bob.is_manager)
print(Bob.role)

print(Marian.bio())
print(Bob.bio())










# Employee.hourly_salary = 16.75
# Marian.hourly_salary = 30
# Employee.hourly_salary = 18
# Employee.os = 'Mac'

# print(Marian.os)
# print(Bob.os)
# print(Bob.hourly_salary)
# print(Marian.hourly_salary)

# print(id(Employee.hourly_salary))
# print(id(Bob.hourly_salary))
# print(id(Marian.hourly_salary))









# print(Marian)
# print(Bob)
# print(type(Marian))
# print(type(Bob))
# # Returns Boolean value, if name belongs to class.
# print(isinstance(Marian,Employee))
# print(isinstance(100,int))



