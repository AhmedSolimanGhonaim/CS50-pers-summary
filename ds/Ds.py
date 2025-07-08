
# ! queues

from collections import deque


class QueuesArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)
        return e

    def dequeue(self):
        if self.isempty():
            raise ValueError("Queue is empty")
        return self._data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is empty')
        return self._data[0]


class StacksArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)
        return e

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            raise IndexError
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            raise IndexError
        return self._data[-1]


#! linked list
# queue linkedlist

queue = deque(['ahmed', 'lil', 5, 6])
print(queue)

# queue is lit a  line so FiFo
queue.append(7)
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)


# STACK
from collections import deque
history = deque()
history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
history
deque(['https://realpython.com/python-csv/',
       'https://realpython.com/pandas-read-write-files/',
       'https://realpython.com/'])
