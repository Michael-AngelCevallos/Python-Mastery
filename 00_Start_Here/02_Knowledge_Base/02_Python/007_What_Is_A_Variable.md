# What Is A Variable?

## Definition

A variable in Python is a **name** that refers to an object in memory.

Variables do **not** store values directly. Instead, they provide a way to reference and interact with objects created by Python.

---

## Purpose

Variables allow programmers to assign meaningful names to data so it can be accessed, modified, and reused throughout a program.

Without variables, every value would need to be written manually each time it was used, making programs difficult to write, read, and maintain.

---

## Mental Model

Think of a variable as a **label** attached to an object.

The object exists independently in memory, while the variable provides a convenient name that allows Python to find that object.

```
first_name
     │
     ▼
┌──────────────┐
│  "Michael"   │
└──────────────┘
```

Multiple variables can reference the same object.

```
first_name ───┐
              │
              ▼
        ┌──────────────┐
        │  "Michael"   │
        └──────────────┘
              ▲
              │
last_name ────┘
```

---

## Assignment

The assignment operator (`=`) binds a variable name to an object.

Example:

```python
age = 35
```

This does **not** mean:

> age equals 35

It means:

> Bind the name `age` to the integer object `35`.

---

## Syntax

```python
first_name = "Michael"

age = 35

height = 5.9

is_learning_python = True
```

---

## Naming Conventions

Python follows the **snake_case** naming convention.

Good examples:

```python
first_name

player_health

account_balance

inventory_count
```

Avoid:

```python
firstname

my variable

thing

x
```

Variable names should clearly describe the data they represent.

---

## Constants

Python does not provide true constants.

Instead, constants are represented by using uppercase variable names.

```python
MAX_PLAYERS = 4

PI = 3.14159
```

This is a convention that signals the value should not be changed.

---

## Examples

Creating variables:

```python
first_name = "Michael"
last_name = "Cevallos"

age = 35

height = 5.9

is_learning_python = True
```

Printing variables:

```python
print(first_name)
print(age)
```

Assigning one variable to another:

```python
first_name = "Michael"

last_name = first_name
```

Both variables now reference the same string object.

---

## Common Mistakes

* Thinking variables store values instead of referencing objects.
* Confusing the assignment operator (`=`) with mathematical equality.
* Using spaces in variable names.
* Using reserved Python keywords as variable names.
* Choosing vague variable names such as `x`, `thing`, or `data` when a more descriptive name is appropriate.

---

## Engineering Notes

* Variables are names, not containers.
* Objects exist independently in memory.
* Multiple variables may reference the same object.
* Python automatically manages object memory.
* Clear variable names make code easier to understand and maintain.

---

## Related Topics

* Data Types
* Objects
* Memory
* Assignment Operator
* `print()`
* Functions
* Variable Scope
