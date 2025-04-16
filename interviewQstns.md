Diff between list and tuple
List is mutable but tuple is not
What are Python’s built-in datatype?
Numeric (int, float, complex), Text (str), Sequence (list, tuple, range), Mapping (dict), Set (set, frozenset), Boolean (bool), Binary (bytes, bytearray, memoryview), and None (NoneType)
How do you implement Inheritance and super keyword in Py?
Inheritance by class Child(Parent):
Super by super()
What is init() in Py?
The initi() method is the constructor in OOP terms. It is used to initialize an object’s state when it is created. This method is automatically called when a new instance of a class is initiated
What are Fixtures in Pytest? When are they used?
In Pytest, a fixture is a way to provide setup and teardown logic for your tests — like preparing test data, opening database connections, initializing web drivers, etc.
Think of them as reusable building blocks that are automatically injected into your tests.
The code before yield runs before the test (setup).
The code after yield runs after the test (teardown).
What is Method Resolution order?
Method Resolution in Python refers to the order in which methods are searched and called when you deal with inheritance, especially multiple inheritance.
Python uses something called the MRO (Method Resolution Order) to figure out which method to call when multiple base classes define the same method.

How to create list of dicts?
How to sort list? > sorted([2,1,4,3])
Python’s default behavor is synchronous
Why self convention used in Python?
Self is not a keyword but a convention in Py. It refers to the current instance of a class
It should always be the first argument
How to reverse list? > num[::-1]
What is @classmethod ?
@classmethod is a decorator used to define a class method — a method that is bound to the class and not the instance.
Key Points About @classmethod:
Takes cls as the first argument, not self.


cls refers to the class itself, not a specific object.


Can be called using either the class or an instance.


Often used for:


Factory methods (creating objects in custom ways)


Modifying class-level state


Accessing or modifying class variables
class MyClass:
    class_var = 0

    @classmethod
    def increment_class_var(cls):
        cls.class_var += 1
        return cls.class_var

print(MyClass.increment_class_var())  # 1
print(MyClass.increment_class_var())  # 2

obj = MyClass()
print(obj.increment_class_var())  # 3

#Example 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        return cls(name, current_year - birth_year)

p = Person.from_birth_year("Alice", 1995)
print(p.name, p.age)  # Alice 30

@staticmethod is a decorator in Python used to define a static method — a method that belongs to a class but does NOT access or modify class or instance data.

Key Characteristics of @staticmethod
No self or cls parameter.


Behaves like a regular function, but is logically grouped with the class.


Can be called via the class or an instance.
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(3, 5))  # Output: 8

utils = MathUtils()
print(utils.add(10, 20))    # Output: 30
When to Use @staticmethod
You want a utility/helper function that makes sense to be grouped with the class.


The method doesn’t need access to class (cls) or instance (self) data.
13. Use of `conftest.py`?
	The conftest.py file in Pytest is used to define fixtures and hooks that are shared across multiple test files
14. How to execute only failed test cases in pytest?
	Pytest –last-failed
15. Use of `with`?
	The with statement in Python is used for resource management and exception handling. It simplifies the process of working with resources like files, network connections, locks, or database sessions by automatically handling setup and teardown.
with open('data.txt', 'r') as f:
    data = f.read()
16. What are the naming conventions for PyTest to discover tests?

Files: test_*.py or *_test.py

Functions: start with test_

Classes: start with Test and no __init__ method

17. How do you run tests using PyTest?

pytest (runs all tests in the current directory and subdirectories)

18. What is the scope of fixtures in PyTest?

function, class, module, package, session
19. How to parameterize tests in Python?
```
@pytest.mark.parametrize("x, y, result", [(1, 2, 3), (2, 3, 5)])
def test_add(x, y, result):
    assert x + y == result
```
20. How do you run only specific tests?

    By test name: pytest -k "test_login"

    By marker: pytest -m "smoke"
21. Commonly Used Hooks

| Hook Name |	Description |

`pytest_sessionstart(session)`	Called after the Session object has been created and before performing collection and entering the run test loop.  

`pytest_sessionfinish(session, exitstatus)`	Called after the whole test run completes.
`pytest_runtest_setup(item)`	Called before setup of each test.
`pytest_runtest_call(item)`	Called when the test is about to be run.
`pytest_runtest_teardown(item)`	Called after the test function has run.
`pytest_configure(config)`	Modify configuration, register markers, etc.
`pytest_unconfigure(config)`	Clean up at the end of the test run.




