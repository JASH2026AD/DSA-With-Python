class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):      # Dog inherits Animal
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()    # Inherited method
d.bark()