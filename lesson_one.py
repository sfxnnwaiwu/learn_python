from array import array
from collections import deque, namedtuple
from sys import getsizeof, path
from pprint import pprint
from timeit import timeit
from typing import List
from abc import ABC, abstractmethod

from share import exception


import logging

logging

pprint(path)



# print("Jecinta Nwaiwu " * 10)

age = 20
name = "John Smith"
is_new_patient = True

# user_input = input("Please what is your name?: ")

# print(f"Hello {user_input}, you are {age} years old and you are a new patient: {is_new_patient}")

# person_name = input("what is your name?: ")
# person_favourite_colour = input("what is your favourite colour?: ")
# print(f"{person_name} likes {person_favourite_colour}")


# person_weight = input("what is your weight in pounds?: ")

# person_weight_in_lbs = int(person_weight)

# person_weight_in_kg = person_weight_in_lbs * 0.453592
# print(f"{person_weight_in_kg}kg")

# new_array = [10, 50, 90, 40]

# value_index = new_array.index(50)
# print(value_index)

my_turple = (8, 9)

# def tryCatch():
#     try:
#         total_value = my_turple.count(0) or None
#         print(total_value)
#     except ValueError:
#         print(ValueError)

#     except Exception as e:
#         print(f"Unexpected Error: {e}")

# tryCatch()

test_list = [("Orange", 40), ("Lemon", 30), ("Grape", 20)]

price_obj = map(lambda item: item[1], test_list)
price_list = list(price_obj)
print(price_list) 

filter_obj = filter(lambda item: item[1] > 20, test_list)
filter_list = list(filter_obj)
print(filter_list)

print("=============================================================")
print(test_list)
print("=============================================================")


# List Comprehension
filtered_list = [item for item in test_list if item[1] > 20]
print(filtered_list)

priced_list = [item[1] for item in test_list]
print(priced_list)

number_item = array("i", [1, 2, 3, 4, 5])
number_item.append(6)
number_item.insert(0, 0)
print(number_item)

# SETS

numbers = [2, 4, 5, 6, 7, 8, 9, 10]
first_set = set(numbers)
print(first_set)

second_set = {13, 4, 15, 6, 17, 8, 20, 10}
print(second_set)

combined_set = first_set.union(second_set) # or first_set | second_set.  What is can be found in the first and second set
print(combined_set)

intersection_set = first_set.intersection(second_set) # or first_set & second_set. What is common in the first and second set
print(intersection_set)

difference_set = first_set.difference(second_set) # or first_set - second_set. What is in the first set but not in the second set
print(difference_set)

semitry_difference_set = first_set.symmetric_difference(second_set) # or first_set ^ second_set. What is in the first set and not in the second set and vice versa
print(semitry_difference_set)


sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

char_frequency = {char : sentence.count(char) for char in sentence if char != " "}
pprint(char_frequency)

most_common_char = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)[0]
print(most_common_char)


# Class

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def zero(cls):
        return cls(0, 0)
    
    def draw(self):
        print(f"Point {self.x}, {self.y}")

point = Point(6, 9)
print(type(point))
print(isinstance(point, Point))

class Comodity:
    def __init__(self, name, price):
        self.__name = name
        self.price = price

    def __str__(self):
        return f"{self.__name}: {self.__price}"
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price

comodity = Comodity("Rice", 2000)
comodity.price = 3000
print(comodity.price)
print(comodity.name)

print(issubclass(Comodity, object))

class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory")

read_stream = MemoryStream()


PointStream = namedtuple("PointStream", ["x", "y"])
p1 = PointStream(x=3, y=5)
p2 = PointStream(x=3, y=5)

print(p1)

print(p1 == p2)

pprint(dir(exception))
