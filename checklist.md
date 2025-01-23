# Сheck Your Code Against the Following Points

## Code Efficiency

1. Use the class name to get access to the class attributes:

Good example:

```python
class Person:
    city = "Kyiv"

    def __init__(self, name: str):
        self.name = name
        
    @staticmethod    
    def print_city() -> None:
        print(Person.city)

liz = Person("Liz")
liz.print_city()  # Kyiv
```

Bad example:

```python
class Person:
    city = "Kyiv"

    def __init__(self, name: str):
        self.name = name
        
    def print_city(self) -> None:
        print(self.city)

liz = Person("Liz")
liz.print_city()  # Kyiv
```

2. You can change the `bool` value in one line:

Good example:

```python
is_married = True

is_married = not is_married
```

Bad example:

```python
is_married = True

if is_married:
    is_married = False
else:
    is_married = True
```

3. Use the static method when needed.

## Code Style

1. Use annotation, it is a good practice:

Good example:

```python
def multiply_by_2(number: int) -> int:
    return number * 2
```

Bad example:
```python
def multiply_by_2(number):
    return number * 2
```

2. Make sure you use the double quotes everywhere.

Good example:

```python
greetings = "Hi, mate!"
```

Bad example:

```python
greetings = 'Hi, mate!'
```

3. Use interpolation instead of concatenation:

Good example:

```python
def print_full_name(name: str, surname: str) -> str:
    return f"{{Name: {name}, surname: {surname}}}"
```

Bad example:

```python
def print_full_name(name: str, surname: str) -> str:
    return "{" + "Name:" + name + ", surname:" + surname + "}"
```

4. Use descriptive and correct variable names:

Good example:

```python
def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
```

Bad example:
```python
def get_full_name(x: str, y: str) -> str:
    return f"{x} {y}"
```
5. Place each argument on a new line, including `self`, with proper indentation and formatting
 
Good example:

```python
def __init__(
        self, 
        name: str,
        age: int
) -> None:
```
Bad example:

```python
def __init__(self, 
             name: str,age: int) -> None:
```

6. It's important to use type annotations for clarity, such as `list[Animal]` instead of just `list` to specify a list of Animal instances

## Clean Code

1. There’s no need to add comments if the code is clear and self-explanatory.
