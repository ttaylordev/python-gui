# Don't Make These Common Python Mistakes

## Try / Accept

```py
try:
    do_something()
except:
    pass
```

This code just lets your errors go scot free. 
There will be no warnings, no crashes yet...
It will be very hard to debug, and hard to locate within the code.

```py
myAge = 30

def runThisThing(x,y):
    print("My name is ", x, "I'm ", y, " years old, and these are my goods: ")
    myGoods = ['apple', 'blueberries', 'cake']
    i = 0
    while i < len(myGoods):
        print(myGoods[i])        
        i += 1

if __name__ == "__main__":
    try:
        print("Welcome to my program")
        myName = 'Bob'
        myName[0] = 'R'
    except:
        pass
    runThisThing(myName, myAge)
```
This is much better, there was an error in mutating the string instead of creating a new variable and assigning the new value to that new variable. The error in the previous example would go unchecked by the debugger.

```py
myAge = 30

def runThisThing(x,y):
    print("My name is ", x, "I'm ", y, " years old, and these are my goods: ")
    myGoods = ['apple', 'blueberries', 'cake']
    i = 0
    while i < len(myGoods):
        print(myGoods[i])        
        i += 1

if __name__ == "__main__":
    print("Welcome to my program")
    myName = 'Bob'
    myName = myName.replace('B','R')
    
    runThisThing(myName, myAge)
```

## Camel Case

Follow the pep 8 standards, unless you want to look like a fool. https://www.python.org/dev/peps/pep-0008/
Function names, and variable names should be in snake_case
Global variable should be written in capital letters.
Magic functions have __preceding and trailing.

```py
my_age = 30

def run_this_thing(x,y):
    print("My name is ", x, "I'm ", y, " years old, and these are my goods: ")
    my_goods = ['apple', 'blueberries', 'cake']
    i = 0
    while i < len(my_goods):
        print(my_goods[i])        
        i += 1

if __name__ == "__main__":
    print("Welcome to my program")
    MY_NAME = 'Bob'
    MY_NAME = MY_NAME.replace('B','R')
    
    run_this_thing(MY_NAME, MY_AGE)

```

## Global Variables

Globals can be accessed and modified by any function or method in the code, or even outside it via remote code injection/execution.
They are represent large flaws in security, debugging, refactoring, and documentation.
They confuse and obfuscate while reading and reasoning about the code.
They cause difficulties when running unit tests.

```py
def run_this_thing(x,y):
    print("My name is ", x, "I'm ", y, " years old, and these are my goods: ")
    my_goods = ['apple', 'blueberries', 'cake']
    i = 0
    while i < len(my_goods):
        print(my_goods[i])        
        i += 1

def main():
    my_age = 30
    my_name = 'Bob'
    print("Welcome to my program")
    my_name = my_name.replace('B','R')
    
    run_this_thing(my_name, my_age)
 
if __name__ == "__main__":
    main()
    
```

## Incrimenting Indices in Loops

A classic method for looping through arrays, or elements of strings etc, is to define and index, set to zero, then loop through an item, incrementing the index each iteration until some end condition is met.
In python, the prefered way is to use the for/in syntax. It is simple and concise.

```py
def run_this_thing(x,y):
    print("My name is ", x, "I'm ", y, " years old, and these are my goods: ")
    my_goods = ['apple', 'blueberries', 'cake']
    for item in my_goods:
        print(item)

def main():
    my_age = 30
    my_name = 'Bob'
    print("Welcome to my program")
    my_name = my_name.replace('B','R')
    
    run_this_thing(my_name, my_age)

if __name__ == "__main__":
    main()
```

## Unspecified Data Types

Specify the data types in function parameters and return types.
It is not required. It assists in preventing many errors, and it improves error checking and readability.
Specify and provide hints for parameters and arguments. 
Comments are great as well and actually help you to come up with the solutions before you code them.

```py
def run_this_thing(name: str, age: int) -> None:
    """
    | Prints the goods for a given name and age
    """
    print("My name is ", name, "I'm ", age, " years old, and these are my goods: ")
    my_goods = ['apple', 'blueberries', 'cake']
    for item in my_goods:
        print(item)
    return

def main(args=None) -> None:
    my_age = 30
    my_name = 'Bob'
    print("Welcome to my program")
    my_name = my_name.replace('B','R')
    
    run_this_thing(my_name, my_age)

if __name__ == "__main__":
    main()
```

## Importing Everything

Avoid import *