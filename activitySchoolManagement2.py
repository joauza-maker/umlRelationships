class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

person1 = Person("Lina", 20)

print(f"Name: {person1.name}")
print(f"Age : {person1._age}")

# Reflection: Using get_age() is better because it encapsulates the data, which allows you to change age without breaking external code.