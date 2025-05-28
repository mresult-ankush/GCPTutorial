## Best Practices for Writing Clean Python Code

### **1. Unclear Variable Names and Magic Numbers**

**Poor Example:**

```python
a = 10
b = 3.14
c = a * b
print(c)
```

**Improved Example:**

```python
radius = 10
pi = 3.14
area = pi * radius
print(area)
```

**Best Practices:**

* Use clear, descriptive variable names.
* Avoid using unexplained numbers in code (magic numbers).

---

### **2. Repetitive Code Instead of Loops or Functions**

**Poor Example:**

```python
print("Hello John")
print("Hello Mary")
print("Hello Alex")
```

**Improved Example:**

```python
names = ["John", "Mary", "Alex"]
for name in names:
    print(f"Hello {name}")
```

**Best Practice:**

* Use loops and data structures to eliminate redundancy.

---

### **3. Absence of Functions**

**Poor Example:**

```python
x = 5
y = 10
z = x * y + y / x
print(z)
```

**Improved Example:**

```python
def calculate_expression(x, y):
    return x * y + y / x

result = calculate_expression(5, 10)
print(result)
```

**Best Practice:**

* Encapsulate logic within functions for readability and reuse.

---

### **4. Hardcoded Inputs and No Error Handling**

**Poor Example:**

```python
salary = int(input("Enter salary: "))
bonus = salary * 0.1
print("Bonus is", bonus)
```

**Improved Example:**

```python
def calculate_bonus(salary, rate=0.1):
    try:
        salary = float(salary)
        bonus = salary * rate
        print(f"Bonus is {bonus}")
    except ValueError:
        print("Invalid salary input. Please enter a number.")

salary_input = input("Enter salary: ")
calculate_bonus(salary_input)
```

**Best Practices:**

* Validate inputs.
* Avoid hardcoding values.
* Use functions for logic encapsulation.

---

### **5. Poor Formatting and Ignoring PEP8**

**Poor Example:**

```python
def add(a,b):return a+b
print( add(2,3))
```

**Improved Example:**

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

**Best Practices:**

* Follow PEP8 for proper formatting.
* Maintain consistent indentation and spacing.

---

### **6. Inefficient Code**

**Poor Example:**

```python
squares = []
for i in range(10):
    squares.append(i*i)
```

**Improved Example:**

```python
squares = [i * i for i in range(10)]
```

**Best Practice:**

* Use list comprehensions for concise and efficient code.

---

### **7. Ignoring Built-in Functions**

**Poor Example:**

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)
```

**Improved Example:**

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

**Best Practice:**

* Use built-in functions for simplicity and performance.

---

### **8. Relying on Global Variables**

**Poor Example:**

```python
x = 5

def multiply(y):
    return x * y

print(multiply(10))
```

**Improved Example:**

```python
def multiply(x, y):
    return x * y

print(multiply(5, 10))
```

**Best Practice:**

* Avoid global variables; pass data via function parameters.

---

### **9. Manual Tuple Indexing**

**Poor Example:**

```python
person = ("Alice", 25, "Engineer")
name = person[0]
age = person[1]
job = person[2]
```

**Improved Example:**

```python
name, age, job = ("Alice", 25, "Engineer")
```

**Best Practice:**

* Use tuple unpacking for readability.

---

### **10. Monolithic Code Without Modularity**

**Poor Example:**

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")
```

**Improved Example:**

```python
def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

name, age = get_user_input()
greet_user(name, age)
```

**Best Practice:**

* Break code into smaller, testable, reusable functions.

---

### **11. Not Using Context Managers**

**Poor Example:**

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

**Improved Example:**

```python
with open("data.txt", "r") as file:
    content = file.read()
```

**Best Practice:**

* Use `with` statements to manage resources safely.

---

### **12. No Docstrings or Meaningful Comments**

**Poor Example:**

```python
def calc(x, y):
    return x ** y
```

**Improved Example:**

```python
def calc_power(base, exponent):
    """Returns base raised to the power of exponent."""
    return base ** exponent
```

**Best Practice:**

* Use descriptive function names and add docstrings.

---

### **13. Deeply Nested Code**

**Poor Example:**

```python
def process(data):
    if data:
        if isinstance(data, list):
            if len(data) > 0:
                return data[0]
```

**Improved Example:**

```python
def process(data):
    if not data or not isinstance(data, list) or len(data) == 0:
        return None
    return data[0]
```

**Best Practice:**

* Use guard clauses to reduce nesting and improve readability.

---

### **14. Repetitive Logic (Violating DRY Principle)**

**Poor Example:**

```python
print("Welcome, Alice")
print("Welcome, Bob")
print("Welcome, Charlie")
```

**Improved Example:**

```python
def welcome(name):
    print(f"Welcome, {name}")

for name in ["Alice", "Bob", "Charlie"]:
    welcome(name)
```

**Best Practice:**

* Apply the DRY (Don't Repeat Yourself) principle.

---

### **15. Manual Index Tracking Instead of `enumerate()`**

**Poor Example:**

```python
names = ["Alice", "Bob", "Charlie"]
for i in range(len(names)):
    print(i, names[i])
```

**Improved Example:**

```python
names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names):
    print(i, name)
```

**Best Practice:**

* Use `enumerate()` for more readable indexed loops.

---

### **16. Catching All Exceptions Blindly**

**Poor Example:**

```python
try:
    result = 10 / 0
except:
    print("Something went wrong.")
```

**Improved Example:**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

**Best Practice:**

* Catch specific exceptions to avoid suppressing hidden errors.

---

### **17. Using Mutable Default Arguments**

**Poor Example:**

```python
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list
```

**Improved Example:**

```python
def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list
```

**Best Practice:**

* Avoid mutable types as default argument values.

---

### **18. Outdated String Formatting**

**Poor Example:**

```python
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
```

**Improved Example:**

```python
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")
```

**Best Practice:**

* Use f-strings for better readability and performance.

---

### **19. Obscure One-Liners**

**Poor Example:**

```python
print((lambda x: x ** 2)(int(input())))
```

**Improved Example:**

```python
def square_number():
    number = int(input("Enter a number: "))
    print(number ** 2)

square_number()
```

**Best Practice:**

* Prioritize code clarity over cleverness.

---

### **20. Missing Type Hints**

**Poor Example:**

```python
def add(a, b):
    return a + b
```

**Improved Example:**

```python
def add(a: int, b: int) -> int:
    return a + b
```

**Best Practice:**

* Use type hints to make function interfaces clearer.

---
