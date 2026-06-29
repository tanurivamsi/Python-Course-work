'''1. What is Python and why is it popular?
2. What are the major features of Python?
3. Why is Python called a high-level language?
4. What is dynamically typed behavior in Python?
5. What does interpreted language mean in Python?
6. How does Python execute code internally?
7. What is bytecode in Python?
8. What is the role of the Python Virtual Machine (PVM)?
9. Difference between compiler and interpreter.
10. Why is Python slower than C/C++?
11. What happens when a Python script runs?
12. What is the purpose of .pyc files?
13. What is the difference between CPython, PyPy, Jython, and IronPython?
14. What is the GIL (Global Interpreter Lock)?
15. How does Python handle multithreading?
16. What are identifiers and keywords?

17. What are comments and docstrings?
18. What is indentation and why is it important?
19. What are Python naming conventions?
20. What is PEP 8?'''

#1)what is Python programming
'''
Python is an interpreted, object-oriented, and case-sensitive programming language.
It is one of the most popular programming languages because it is easy to learn, read, and understand. Python has a simple syntax that makes coding easier for beginners as well as experienced programmers. It executes
programs efficiently and provides a robust and reliable environment for software development.
'''

# 2. What are the major features of Python?

'''**Answer:**

Major features of Python are:

* Easy to Learn
* High-Level Language
* Interpreted Language
* Object-Oriented
* Dynamically Typed
* Cross-Platform
* Open Source
* Large Standard Library
* Portable
* Extensible
* Scalable
'''

# 3. Why is Python called a high-level language?

'''**Answer:**

Python is called a **high-level language** because its syntax is close
to human language and easy to read and write.
It hides hardware-level details like memory management,
allowing programmers to focus on solving problems.
'''

# 4. What is dynamically typed behavior in Python?

'''**Answer:**

Python is dynamically typed, meaning you **do not need to declare the data type** of a variable.

The type is assigned automatically during execution.
'''

a = 10      # int
a = "Hello" # string
print(a)

# 5. What does interpreted language mean in Python?
'''**Answer:**

Python is an interpreted language because the code is executed **line by line** through
the Python Interpreter instead of being converted directly into machine code before execution.
'''

# 6. How does Python execute code internally?

'''**Answer:**

Python executes code in three steps:

1. Python source code (.py)
2. Compiler converts it into Bytecode (.pyc)
3. Python Virtual Machine (PVM) executes the bytecode

Flow:


Python Code (.py)
        ↓
Python Compiler
        ↓
Bytecode (.pyc)
        ↓
Python Virtual Machine (PVM)
        ↓
Machine Code
        ↓
Output

'''

# 7. What is bytecode in Python?

'''**Answer:**

Bytecode is an intermediate code generated after compiling Python source code.

* Stored in `.pyc` files
* Platform-independent
* Executed by the Python Virtual Machine (PVM)

'''

# 8. What is the role of the Python Virtual Machine (PVM)?

'''**Answer:**

The PVM executes Python bytecode and converts it into machine instructions that
the operating system can understand.

Without the PVM, Python programs cannot run.

'''

# 9. Difference between compiler and interpreter.
'''
| Compiler                           | Interpreter                 |
| ---------------------------------- | --------------------------- |
| Converts the whole program at once | Executes line by line       |
| Faster execution                   | Slower execution            |
| Errors shown after compilation     | Errors shown immediately    |
| Generates executable file          | No executable file          |
| Example: C, C++                    | Example: Python, JavaScript |

'''

# 10. Why is Python slower than C/C++?

'''**Answer:**

Python is slower because:

* It is interpreted.
* It is dynamically typed.
* It performs automatic memory management.
* Extra runtime checking increases execution time.

C/C++ are compiled directly into machine code, making them faster.

'''
# 11. What happens when a Python script runs?

'''**Answer:**

Steps:

1. Python reads the `.py` file.
2. Converts it into bytecode.
3. Stores bytecode in `.pyc` (optional).
4. PVM executes the bytecode.
5. Output is displayed.
'''

# 12. What is the purpose of .pyc files?

'''**Answer:**

`.pyc` files store compiled bytecode.

Advantages:

* Faster execution
* Avoids recompiling unchanged code
* Stored inside the `__pycache__` folder

'''

# 13. What is the difference between CPython, PyPy, Jython, and IronPython?
'''
| Implementation | Runs On                     |
| -------------- | --------------------------- |
| CPython        | C language (Default Python) |
| PyPy           | Faster using JIT Compiler   |
| Jython         | Java Virtual Machine (JVM)  |
| IronPython     | .NET Framework              |
'''

# 14. What is the GIL (Global Interpreter Lock)?
'''
**Answer:**

The Global Interpreter Lock (GIL) allows **only one thread to execute Python bytecode at a time** in
CPython.

Advantages:

* Simpler memory management

Disadvantages:

* Limits CPU-bound multithreading performance

'''

# 15. How does Python handle multithreading?

'''**Answer:**

Python supports multithreading using the `threading` module.

Due to the GIL:

* Good for I/O-bound tasks
* Not ideal for CPU-bound tasks

For CPU-bound tasks, use the `multiprocessing` module.

'''

# 16. What are identifiers and keywords?

### Identifiers

'''Identifiers are names given to:

* Variables
* Functions
* Classes
* Objects

Example:

```python
student_name
total_marks
```
'''
### Keywords

'''Keywords are reserved words with predefined meanings.

Examples:

```python
if
else
while
for
def
class
return
True
False
None
```

You cannot use keywords as variable names.

'''

# 17. What are comments and docstrings?

### Comments

'''Comments explain code.

Single-line:

```python
# This is a comment
```


Multi-line:

```python
'''
'''This is
a multi-line comment'''
'''
```
'''
### Docstrings
'''
Docstrings describe functions, classes, or modules.

Example:

python'''
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
o = add(2,2)
print("Addition of a and b is : ",o)



# 18. What is indentation and why is it important?
'''
**Answer:**

Indentation means giving spaces before a block of code.

Python uses indentation instead of braces `{}` to define code blocks.

Example:

```python
if True:
    print("Hello")
```

Without proper indentation, Python raises an `IndentationError`.

'''

# 19. What are Python naming conventions?

'''**Answer:**

Common naming conventions:

* Variables → `snake_case`
* Functions → `snake_case`
* Classes → `PascalCase`
* Constants → `UPPER_CASE`
* Private variables → `_variable`
* Strongly private variables → `__variable`

Examples:

```python
student_name
calculate_salary()
StudentDetails
MAX_SIZE
```

'''

# 20. What is PEP 8?

'''**Answer:**

**PEP 8 (Python Enhancement Proposal 8)** is the official style guide for writing Python code.

It improves readability and consistency.

Some PEP 8 rules:

* Use 4 spaces for indentation.
* Maximum line length: 79 characters.
* Use meaningful variable names.
* Add spaces around operators.
* Separate functions and classes with blank lines.
* Follow `snake_case` for variables/functions and `PascalCase` for classes.

PEP 8 helps developers write clean, readable, and maintainable Python code.'''
