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

class Cow(Animal):
  def sound(show):
    return "Mowww"


animals=[Cat(), Dog(), Cow(), Animal()]

for Animal in animals:
  print(Animal.sound())


# Just like in Java Programming, it is being included about the Shapes of different matters.

class Pencil:
  def use(show):
    return "Writing"
    
class Eraser:
  def use(show):
    return "Erasing"

def tool(touse):
  print(touse.use())

tool(Pencil())

tool(Eraser())

