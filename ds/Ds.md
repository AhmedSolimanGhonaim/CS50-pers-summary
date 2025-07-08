
[text](https://g.co/gemini/share/ac38d575c880
)

# Arrays

- **Definition:**  
  An array is a contiguous block of memory where each element has the same type and fixed size, allowing O(1) indexing via a formula like `base + i * size`.

## Array vs List

| Feature         | Array (C/Java)         | Python List                |
|-----------------|-----------------------|----------------------------|
| Size            | Fixed                  | Dynamic                    |
| Data Type       | Homogeneous            | Heterogeneous              |
| Memory          | Compact, efficient     | More memory (references)   |
| Speed           | Fast for numerics      | Flexible, slower for numerics |
| Mutability      | Mutable (elements)     | Mutable (elements & size)  |

- **Python lists** are dynamic arrays (can grow/shrink).
- **Arrays** are more memory-efficient for large homogeneous data.

## List Characteristics

- Ordered
- Mutable (changeable)
- Can contain duplicates
- Dynamic size
- Can be nested
- Can contain any object type

### Disadvantages

1. Slower for searching/inserting in the middle (O(n))
2. Mutable—can lead to bugs in concurrent environments
3. Uses more memory (stores references)

## Mutable vs Immutable

- **Immutable:** int, float, bool, str, tuple
- **Mutable:** list, set, dict

When you change a list element, Python creates a new object for the new value and updates the reference in the list.

## How Python Lists Store Elements

- Each list element is a reference to an object stored elsewhere in memory.
- The list itself stores these references (addresses).
- When you change an element, the list updates the reference to the new object.

## List Resizing

- When appending and no space is left, Python allocates a new, larger block (usually double the size), copies elements, and appends the new item.
- This is why Python lists are dynamic.


🧩 Are Python lists stored contiguously?
Yes and no—in two layers:

The list container itself
In CPython, a list is implemented as a dynamic array of pointers (PyObject*), meaning the pointers are stored contiguously in memory 



> . You get O(1) indexing because the pointer array is tightly packed.
> 
> The objects these pointers refer to
> Each Python object (e.g., an integer, string) is separately heap-allocated, and their actual storage can be anywhere in memory—not contiguous 
> 


[text](https://medium.com/analytics-vidhya/amortized-runtime-analysis-for-python-lists-35e935e290db)

**its Amortized O(1). It runs in constant time as long as an re-allocation isn't required. In the worst case, it's O(n), but that worst case isn't frequent.

Technically, it is possible for a dynamic array to always have O(1) appends, but it requires using significantly more memory, which they evidently decided not to do.
**
[text](https://www.reddit.com/r/learnpython/comments/yeahqq/what_is_pythons_listappend_method_worst_time/?utm_source=chatgpt.com)


---

# Stacks and Queues

## Python List as Stack

```python
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")    # Push
stack.append("Iqbal")
print(stack)
print(stack.pop())     # Pop
print(stack)
```

- **Stack Principle:** Last-In, First-Out (LIFO)
- `append()` and `pop()` are O(1) at the end.

## Python List as Queue

```python
queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)
print(queue.pop(0))    # Dequeue (slow, O(n))
print(queue)
```

- **Queue Principle:** First-In, First-Out (FIFO)
- `pop(0)` is O(n) (slow), as all elements must shift.

## Using `collections.deque`

- **Deque** is optimized for fast appends and pops from both ends.

### Stack with Deque

```python
from collections import deque
stack = deque(["Ram", "Tarun", "Asif", "John"])
stack.append("Akbar")
stack.append("Birbal")
print(stack.pop())     # Pop from end
```

### Queue with Deque

```python
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
queue.append("Akbar")
queue.append("Birbal")
print(queue.popleft()) # Pop from front
```

---

# Custom Stack and Queue Classes

```python
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
```

---

# References

- [StackOverflow: Best way to implement stack and queues in Python](https://stackoverflow.com/questions/64602216/what-is-the-best-way-of-implementing-stack-and-queues-in-python-without-using-a?utm_source=chatgpt.com)