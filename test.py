class Person:
    species = "homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def days_lived(self):
        return self.age * 365

jake = Person(name="Jake", age=21)

print(jake.days_lived())
print(jake.species)
    
