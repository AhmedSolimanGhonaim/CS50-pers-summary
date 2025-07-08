## Linked Lists

Linked lists are an ordered collection of objects.  
[Learn more about linked lists](https://realpython.com/linked-lists-python/?utm_source=chatgpt.com)

[text](https://g.co/gemini/share/de9b8e4a3c37)


[GeeksforGeeks مهمممممممممممممم: Singly Linked List Tutorial](https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/)

- Linked lists are stored in memory differently from lists. Lists use contiguous memory blocks to store references, while linked lists store references as part of their own elements.
- Linked lists can be used to implement queues, stacks, and graphs.

### Performance Considerations

- The difference in memory usage between lists and linked lists is usually insignificant. Focus on their performance differences, especially regarding time complexity.
- Linked lists are almost always slower for storing data. An append generally requires an allocation, which tends to be slow. Arrays (lists) can consolidate allocations, making them faster for storage and retrieval, especially due to better cache usage.
- Arrays are significantly faster for both storage (by constant factors) and retrieval, as long as you're appending at the end each time.
- Linked lists are faster for appending or removing elements at the front or at random locations.
- Linked lists are a functional data structure: you can create a new list by prepending to an old one without affecting the original list. This property makes them popular in functional programming languages like Lisp, Scheme, or Haskell.


### implementation in py
-Introducing collections.deque
    In Python, there’s a specific object in the collections module that you can use for linked lists called deque (pronounced “deck”), which stands for double-ended queue.

  - collections.deque uses an    implementation of a linked list in which you can access, insert, or remove elements from the beginning or end of a list with constant O(1) performance.

