
# Memory Addresses and Object Identity in Python

This document explores how Python manages memory, object identity, and related best practices.

---

## Useful Links

- [Gemini Share Link](https://g.co/gemini/share/798e6bb6ac13)
- [Is Python Call by Reference or Call by Value? (GeeksforGeeks)](https://www.geeksforgeeks.org/python/is-python-call-by-reference-or-call-by-value/?utm_source=chatgpt.com)

---

## Memory Concepts

- **Addresses in memory** are often shown in hexadecimal.
- **Main frame, call stack, heap, and local scope** are key memory regions:
    - Function calls are managed in the call stack.
    - The scope where a breakpoint is set is the local scope.
    - Python prevents garbage collection issues.
    - Stack overflow can occur with excessive recursion.

---

## Recursion and Stack Limits

> From the documentation on `sys.setrecursionlimit()`:
>
> Set the maximum depth of the Python interpreter stack to limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.
>
> By increasing the recursion limit, the program can crash the Python interpreter.
>
> Since Python does not optimize tail recursion, unlimited recursion causes the stack to overflow (run out of memory).
>
> In many real-world applications, it is necessary to implement functions without recursion to avoid stack overflow memory errors.
>
> See also: Setting stacksize in a python script

---

## Example: Memory Address of an Integer

```python
n = 5
print(id(n))
print(hex(id(n)))
# Example output:
# 11760808
# 0xb374a8
```

---

## Integer Interning

Python automatically interns integers in the range **–5 to 256**.

- While the general rule for small integer caching (specifically -5 to 256) is commonly taught, CPython has optimizations that can lead to unexpected `True` results for larger integers in certain scenarios.

### Why might `a is b` be `True` for large integers?

- **Interning of Literals During Compilation:** When identical integer literals (like `10000000`) appear multiple times in the same code block, the Python compiler may "intern" these literals, creating only one object in memory.
- **Script vs. Interactive Interpreter:** In scripts, assignments like `a = 10000000` and `b = 10000000` may refer to the same object. In the interactive interpreter, they are usually distinct objects.

#### Example: Script Execution

```python
# your_script.py
a = 10000000
b = 10000000
print(a is b)  # Likely True
```

#### Example: Interactive Interpreter

```python
>>> a = 10000000
>>> b = 10000000
>>> print(a is b)  # Likely False
```

**Key Takeaway:**  
The `-5 to 256` range is a reliable cache for small integers. For larger integers, the behavior of `is` depends on whether the literals are interned by the Python compiler.  
**Always use `==` for value comparison and `is` only for object identity.**

---

## Examples

```python
a = 100
b = 100
print(a is b)  # True

a = 10000000
b = 10000000
print(id(a) is id(b))  # Should be False

a = 2
b = 2
print(a is b)
print(id(a), id(b))

a = int("10000001")
b = int("10000001")
print(a is b)  # Could be False, as they are distinct objects
```

---

## Best Practices

- Use `==` for comparing values of strings, numbers, or containers.
- Use `is` for identity checks (e.g., `if x is None:`).
- Don’t rely on implicit interning for correctness—it varies by Python version and context.
- Only use `sys.intern()` when you have many duplicate strings and performance or memory usage is critical.

---

## Passing by Object Reference

- In Python, there's no classic “pass by reference” or “pass by value” like in C++ or Java.
- Instead, Python uses **“pass by object reference”** or **“pass by assignment”** (also called call by sharing).

---

