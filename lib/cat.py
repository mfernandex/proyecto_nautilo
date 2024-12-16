class Cat:
    species = "Felinus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return self.name