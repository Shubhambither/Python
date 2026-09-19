# Master Study Notes: Internal Working of Python (Memory, References, Mutability, & Slicing)

## 1. High-Level Python Memory Model: Variables as Name Tags
In Python, variables do not store raw data values directly inside themselves. Instead, **variables act as name tags or references (pointers)** that point to objects residing in the computer's heap memory.

* **Assignment Behavior (`x = value`):** When you assign a value to a variable, Python creates an object in memory and attaches the variable name tag to that specific memory address.
* **Inspect Memory Address (`id()`):** You can inspect the exact memory address (heap location) where an object resides using Python's built-in `id()` function (which returns the CPython memory pointer address as an integer).
```python
x = 42
print(id(x))  # Prints the unique memory address in CPython
print(hex(id(x)))  # Prints the hexadecimal pointer format (e.g., 0x7fa...)