from array import array
from collections import deque


queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

print(queue.popleft())         # The first to arrive, "Eric", leaves
# The remaining queue is ["John", "Michael", "Terry", "Graham"]
print(queue)

queue.clear()                   # Remove all elements from the queue
print(queue)                    # The queue is now empty.

if not queue:                   # Test if the queue is empty
    print("The queue is empty")


# Challenge 1 - Queue - FIFO (First In First Out)
# Implement a Queue class that has the following methods
# to add an item to the queue
# to remove an item from the queue
# to check the size of the queue
# to check if the queue is empty
# to view the top item in the queue
# to view all items in the queue
# Example
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# print(queue.size()) # Output: 5
# print(queue.dequeue()) # Output: 1
# print(queue.dequeue()) # Output: 2
# print(queue.isEmpty()) # Output: False
# print(queue.peek()) # Output: 3
# print(queue.display()) # Output: [3, 4, 5]
# print(queue.dequeue()) # Output: 3
# print(queue.dequeue()) # Output: 4
# print(queue.dequeue()) # Output: 5
# print(queue.isEmpty()) # Output: True
# print(queue.size()) # Output: 0
# print(queue.dequeue()) # Output: Queue is empty
# print(queue.peek()) # Output: Queue is empty
# print(queue.display()) # Output: Queue is empty
# Constraints
# The methods should be implemented in constant time
# The methods should return appropriate messages for empty queue
# The methods should return appropriate messages for full queue
# The methods should return appropriate messages for non-empty queue
# The methods should return appropriate messages for non-full queue
# The methods should return appropriate messages for non-integer input
# The methods should return appropriate messages for non-numeric input
# The methods should return appropriate messages for non-string input
# The methods should return appropriate messages for non-list input
# The methods should return appropriate messages for non-dictionary input
# The methods should return appropriate messages for non-tuple input
# The methods should return appropriate messages for non-set input
# The methods should return appropriate messages for non-float input
# The methods should return appropriate messages for non-boolean input
# The methods should return appropriate messages for non-array input
# The methods should return appropriate messages for non-deque input
# The methods should return appropriate messages for non-stack input
# The methods should return appropriate messages for non-queue input
# The methods should return appropriate messages for non-linked list input
# The methods should return appropriate messages for non-binary tree input
# The methods should return appropriate messages for non-binary search tree input

number = [0, 1, 2, 3, 4, 5, 6, 7]

first = set(number)
print(first)

second = {0, 1, 2, 3, 4, 5, 6, 7}
second.add(8)
second.remove(3)
len(second)

union = first | second
intersection = first & second
difference = first - second
sementric_difference = first ^ second

list()
tuple()
dict()
set()

dictionary = {'x': 1, 'y': 2}

dictionary['z'] = 3
print(dictionary)

dictionary['x'] = 4
dictionary.get('x')

if 'a' in dictionary:
    print(dictionary['a'])


del dictionary['x']
print(dictionary)

for key in dictionary:
    print(key)

for key, value in dictionary.items():
    print(key, value)


values = [x * 2 for x in range(5)]
values = {x * 2 for x in range(5)}
