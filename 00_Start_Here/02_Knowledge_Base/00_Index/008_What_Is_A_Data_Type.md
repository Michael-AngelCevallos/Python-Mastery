# What Is A Data Type

---

## Definition

A data type tells Python how a value should be interpreted and what operations are valid for it.

Every object in Python has a data type.

Variables do not own data types.
Variables simply reference objects.

---

## Mental Model

Variable (Label)
        │
        ▼
     Object
   ┌──────────────┐
   │ Value        │
   │ Data Type    │
   └──────────────┘

The object owns both the value and the data type.

---

## Common Primitive Data Types

### Integer (int)

Represents whole numbers.

Example:

```python
age = 35
```

---

### Float (float)

Represents decimal numbers.

Example:

```python
temperature = 98.6
```

---

### String (str)

Represents text.

Example:

```python
name = "Michael"
```

---

### Boolean (bool)

Represents True or False.

Example:

```python
is_passing = True
```

---

## Determining A Data Type

Python provides the built-in function:

```python
type()
```

Example:

```python
age = 35

print(type(age))
```

Output:

```
<class 'int'>
```

---

## Dynamic Typing

Python determines an object's data type automatically.

Example:

```python
age = 35
```

Python recognizes the value as an integer object without requiring the programmer to declare the type.

Unlike Java:

```java
int age = 35;
```

Python simply uses:

```python
age = 35
```

---

## Choosing The Correct Data Type

Choose the data type based on what the information represents, not what it looks like.

Examples:

| Information | Correct Type | Reason |
|-------------|-------------|--------|
| Name | String | Text |
| GPA | Float | Decimal value |
| Age | Integer | Whole number |
| Has Insurance | Boolean | True / False |
| ZIP Code | String | Identifier |
| Phone Number | String | Identifier |
| VIN | String | Identifier |
| Serial Number | String | Identifier |

---

## Engineering Notes

Good software engineers first determine what information represents in the real world before selecting a data type.

Data modeling comes before programming.

---

## Related Topics

- Variables
- Objects
- Dynamic Typing
- Python vs Java
- type()