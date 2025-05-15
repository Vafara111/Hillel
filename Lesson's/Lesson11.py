class Animal:
    _count_of_paws = 4
    __age = 10
    def speak(self):
        print("Hey")

class Dog(Animal):
    def speak(self):
        print("Gav")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Turtle(Animal):
    def __init__(self, name):
        self.name = name
cat = Cat()
dog = Dog()
turtle = Turtle("Jeky")

# cat.speak()
# dog.speak()

def call_animal(animal: Cat | Dog):
    animal.speak()

call_animal(cat)
call_animal(dog)
call_animal(turtle)
print(turtle.name)
turtle.name = "A"
print(turtle.name)
print(Turtle._count_of_paws)
