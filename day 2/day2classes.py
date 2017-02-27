import random

class Person():
    def __init__(self):
        # pass - this goes onto the next function when it has no code
        # so in this case it would go on to sleep
        # print "Person created!"
        self.name = ""
    def sleep(self):
        return "zzzz My name is " + self.name

#person1 = Person()
people = []
names = ['Chelsey', 'Fern', 'Ka', 'Kev', 'Scott']
for i in range(5):
    p = Person()
    index = random.randrange(0,len(names))
    p.name = names[index]
    people.append(p)
    names.pop(index)
    print p.name


class Dog():
    def __init__(self, n, a):
        # print "dog created!"
        self.name = n
        self.breed = "Beagle"
        self.age = a
    def bark(self):
        return "Woof Woof " + self.name
    def run(self):
        return "I am frolicking and I am " + str(self.age) + " years old"

d1 = Dog("Fido", 7)
print d1.run()

d2 = Dog("Rex", 12)
print d2.bark()

#to call a class in a different file

# from animals import Dog "animals" is the other file name
# can use * instead of the class name "Dog"

# d = Dog("Lassie",12)

# print d.name