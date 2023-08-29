# Python Classes and Objects

## Table of Contents

* [Description](#description)
* [Objectives](#objectives)
* [Instructions](#instructions)
* [Files](#files)
* [Author](#author)

## Description

Contains various programs written in Python that demonstrate the use of classes and objects.

## Objectives

### General

* Why Python programming is awesome
* What is OOP
* "first-class everything"
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

## Instructions

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* Your code should use the `PEP 8` style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

## Files

[0-square.py](0-square.py)

```sh
Write an empty class Square that defines a square:

```

* You are not allowed to import any module

[1-square.py](1-square.py)

```sh
Write a class Square that defines a square by: (based on 0-square.py)
```

* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

[2-square.py](2-square.py)

```sh
Write a class Square that defines a square by: (based on 1-square.py)
```

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module

[3-square.py](3-square.py)

```sh
Write a class Square that defines a square by: (based on 2-square.py)
```

* Private instance attribute: `size`:
* Instantiation with optional `size`: `def __init__(self, size=0):`
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

[4-square.py](4-square.py)

```sh
Write a class Square that defines a square by: (based on 3-square.py)

# Private instance attribute: size:
# Public instance method: def area(self): that returns the current square area
# Property def size(self): to retrieve it
# Property setter def size(self, value): to set it:
# `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
# if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
# Instantiation with optional `size`: `def __init__(self, size=0):`
# You are not allowed to import any module
```

[5-square.py](5-square.py)

```sh
Write a class Square that defines a square by: (based on 4-square.py)

# Private instance attribute: size:
# property def size(self): to retrieve it
# property setter def size(self, value): to set it:
# `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
# if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
# Instantiation with optional `size`: `def __init__(self, size=0):`
# Public instance method: `def area(self):` that returns the current square area
# Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
# if `size` is equal to 0, print an empty line
# You are not allowed to import any module
```

[6-square.py](6-square.py)

```sh
Write a class Square that defines a square by: (based on 5-square.py)

# Private instance attribute: size:
# property def size(self): to retrieve it
# property setter def size(self, value): to set it:
# `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
# if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
# Private instance attribute: position:
# property def position(self): to retrieve it
# property setter def position(self, value): to set it:
# `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
# Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
# Public instance method: `def area(self):` that returns the current square area
# Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
# if `size` is equal to 0, print an empty line
# `position` should be use by using space - Don’t fill lines by spaces when `position[1] > 0`
# You are not allowed to import any module
```

## Author

* **Andrew Maina** - [Andrew]("https://github.com/KigMaina")
