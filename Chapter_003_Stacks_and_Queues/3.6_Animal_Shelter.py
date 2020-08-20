__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import time
import unittest
from myqueue import Queue


class AnimalShelter():

    class Cat():
        def __init__(self):
            self.time = time.time()

    class Dog():
        def __init__(self):
            self.time = time.time()

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        """Adds specified animal to shelter"""

        if type(animal) is not str:
            raise TypeError('input must be in string format')

        animal = animal.rstrip().lower()

        if animal not in {'cat', 'dog'}:
            raise KeyError('animal must be dog or cat')

        if animal == 'cat':
            self.cat_queue.enqueue(self.Cat())
        else:
            self.dog_queue.enqueue(self.Dog())

    def dequeueAny(self):
        """Returns the animal that has been at the shelter the longest"""

        if self.dog_queue.isEmpty() and self.cat_queue.isEmpty():
            raise IndexError('All animals have been adopted! :)')
        else:
            if self.dog_queue.peek().time < self.cat_queue.peek().time:
                return self.dog_queue.dequeue()
            else:
                return self.cat_queue.dequeue()

    def dequeueDog(self):
        """Returns the dog that has been at the shelter the longest"""

        if self.dog_queue.isEmpty():
            raise IndexError('All dogs have been adopted!')
        else:
            return self.dog_queue.dequeue()

    def dequeueCat(self):
        """Returns the cat that has been at the shelter the longest"""

        if self.dog_queue.isEmpty():
            raise IndexError('All cats have been adopted!')
        else:
            return self.cat_queue.dequeue()


class TestAnimalShelter(unittest.TestCase):
    def test_enqueue(self):
        shelter = AnimalShelter()
        with self.assertRaises(TypeError):
            shelter.enqueue(0)
            shelter.enqueue([])
            shelter.enqueue(shelter)
            shelter.enqueue({})

        with self.assertRaises(KeyError):
            shelter.enqueue('sammy')
            shelter.enqueue('hamster')

        shelter.enqueue('dog')
        shelter.enqueue('dog')

        self.assertEqual(len(shelter.dog_queue), 2)
        self.assertEqual(len(shelter.cat_queue), 0)

        shelter.enqueue('cat')
        self.assertEqual(len(shelter.dog_queue), 2)
        self.assertEqual(len(shelter.cat_queue), 1)

    def test_dequeueAny(self):
        shelter = AnimalShelter()
        with self.assertRaises(IndexError):
            shelter.dequeueAny()

        shelter.enqueue('dog')
        time.sleep(.5)
        shelter.enqueue('cat')
        time.sleep(.5)
        shelter.enqueue('dog')

        self.assertIs(type(shelter.dequeueAny()), AnimalShelter.Dog)
        self.assertEqual(len(shelter.dog_queue), 1)
        self.assertEqual(len(shelter.cat_queue), 1)

        self.assertIs(type(shelter.dequeueAny()), AnimalShelter.Cat)
        self.assertEqual(len(shelter.dog_queue), 1)
        self.assertEqual(len(shelter.cat_queue), 0)

    def test_dequeueDog(self):
        shelter = AnimalShelter()
        with self.assertRaises(IndexError):
            shelter.dequeueDog()

        shelter.enqueue('dog')
        time.sleep(.5)
        shelter.enqueue('cat')
        time.sleep(.5)
        shelter.enqueue('dog')

        self.assertIs(type(shelter.dequeueDog()), AnimalShelter.Dog)
        self.assertEqual(len(shelter.dog_queue), 1)
        self.assertEqual(len(shelter.cat_queue), 1)

        self.assertIs(type(shelter.dequeueDog()), AnimalShelter.Dog)
        self.assertEqual(len(shelter.dog_queue), 0)
        self.assertEqual(len(shelter.cat_queue), 1)

    def test_dequeueCat(self):
        shelter = AnimalShelter()
        with self.assertRaises(IndexError):
            shelter.dequeueCat()

        shelter.enqueue('dog')
        time.sleep(.5)
        shelter.enqueue('cat')
        time.sleep(.5)
        shelter.enqueue('dog')

        self.assertIs(type(shelter.dequeueCat()), AnimalShelter.Cat)
        self.assertEqual(len(shelter.dog_queue), 2)
        self.assertEqual(len(shelter.cat_queue), 0)


if __name__ == '__main__':
    unittest.main()
