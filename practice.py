class Person:
    'This is the base class for all Persons registered'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Hello my name is {self.name} and I\'m {self.age} years old.')


person_object = Person('Jane', '22')
print(Person.__doc__)