Parent Class (Animal)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")


Child Class (Dog)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("The dog barks.")


#In this example:

'''Animal is the parent class.
- Dog is the child class that inherits from Animal.
- Dog has its own __init__ method, which calls the parent's __init__ method using super().__init__(name).
- Dog overrides the sound method to provide its own implementation.'''
