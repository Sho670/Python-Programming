# This code shows runtime polymorphism in python programming using method called sound() method.

# This includes class Animal and various animals included with thier sounds.

class Animal:
  def sound(show):
    return "Sound"
class Cat(Animal):
  def sound(show):
    return "Meow"

class Dog(Animal):
  def sound(show):
    return "Bark"
