# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

class Bird:
    def speak(self):
        return "Birds chirp."

class Dog:
    def speak(self):
        return "Dogs bark."

class Cat:
    def speak(self):
        return "Cats meow."

# Function that demonstrates polymorphism
def make_sound(animal):
    print(animal.speak())

# Create objects of different classes
bird = Bird()
dog = Dog()
cat = Cat()

# Call the same method using different objects
make_sound(bird)  # Output: Birds chirp.
make_sound(dog)   # Output: Dogs bark.
make_sound(cat)   # Output: Cats meow.
