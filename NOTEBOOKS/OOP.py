# Tells us that Python is an OOP language.
class Person:
    def __init__(self, name, age, email, address, phone):
        self.name = name 
        self.age = age
        self.email = email
        self.address = address
        self.phone = phone
    
    def display_name(self):
        print(f'Name of person: {self.name}')
        
    def display_age(self):
        print(f'Age of person: {self.age}')
        
    def display_email(self):
        print(f'Email of person: {self.email}')
        
    def display_address(self):
        print(f'Address of person: {self.address}')
        
    def display_phone(self):
        print(f'Phone of person: {self.phone}')
        
class Employee:
    def emp_dept(self, dept):
        print(f'Employee Department: {dept}')

# Create an instance of Person
person1 = Person(name='John Doe', age='20', email='laariachris@gmail.com', address='Nairobi', phone='740882331')

# Testing the methods
person1.display_name()
person1.display_age()
person1.display_email()
person1.display_address()
person1.display_phone()

#person2.name('Jane Malory')
#person2.age(25)
#person2.email('laariachris@gmail.com')
#person2.address('Nairobi')
#person2.phone(740882331)

person3 = Employee ()
#person3.emp_dept('Engineering')


