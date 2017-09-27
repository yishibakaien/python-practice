
class Animal(object):
    """docstring for Animal"""
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is running')
    def eat(self):
        print('dog is eating')
        
class Cat(Animal):
    pass

dog = Dog()
cat = Cat()
dog.run()
cat.run()