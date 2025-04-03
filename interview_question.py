#Q)1. What does mean about scope of pythpon------------------------------------------------------------------------------------->
'''the scope of a variable refer to the context in which that variable is visible/accessible to the python interpreter '''

#Q)2.Expain need of loop and function and in python------------------------------------------------------------------------>
#A string data type is traditionally
#a sequence of characters, either as a literal constant or as some kind of variable
'''
Key Terms
ASCII
    American Standard Code for Information Interchange

character
    A data type representing single text characters like the alphabet, numeral digits, punctuation, etc.

double quote marks
    Used to create string type data within most programming languages.

single quote marks
    Used to create character type data within languages that differentiate between string and character data types.

string
    A series or array of characters as a single piece of data
'''

#Q)3. explain need of loop and function in python ------------------------------------>
''' Loops:-------
 loop are important in python or in any other programmng language as they help you to execute a block of code repeatedly

Function:-----
function in python. you use function in programming to bundle a set of instruction that you want to use repeatedly or
that because of their complex, are better self-cont6ained in a sub-program and called when needed
'''

#Q)8. Explane many types of argument we passed in python function,explane.------------------------->
'''
In Python, you can pass arguments to a function in several ways:
1. Positional Arguments:--

    These are the most common type of arguments.
    They are passed in the same order as the parameters are defined in the function. 

Python
Execution output

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)  # "Hello, Alice! You are 25 years old."

Hello, Alice! You are 25 years old.
2. Keyword Arguments:---

    These arguments are passed with their corresponding parameter names.
    Order doesn't matter when using keyword arguments. 

Python

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="Bob")  # "Hello, Bob! You are 30 years old."

3. Default Arguments:---

    These arguments have a default value set in the function definition.
    If no value is passed for these arguments, the default value is used. 

Python

def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet("Charlie")  # "Hello, Charlie! You are 18 years old."
greet("David", 22)  # "Hello, David! You are 22 years old."

4. Arbitrary Positional Arguments (*args):---

    Used when you don't know how many arguments will be passed to the function.
    These arguments are collected into a tuple within the function. 

Python

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4)) 

5. Arbitrary Keyword Arguments (**kwargs):----

    Used when you don't know how many keyword arguments will be passed.
    These arguments are collected into a dictionary within the function. 

Python

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=20, city="New York") 
'''
#Q)9.what is slice() and explain with example-------------------------------------------------------------------------->

'''
In Python, the slice() function creates a slice object that can be used to extract a portion of a sequence (e.g., a string, list, or tuple).
Syntax:
Python

slice(start, stop, step)

Parameters:

    start: The index where the slice starts (inclusive). If omitted, it defaults to 0.
    stop: The index where the slice ends (exclusive). If omitted, it defaults to the end of the sequence.
    step: The increment between indices. If omitted, it defaults to 1. 

Attributes:
    start: The value of the start parameter.
    stop: The value of the stop parameter.
    step: The value of the step parameter. 

Example:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_slice = slice(2, 7, 2)

result = my_list[my_slice]

print(result)'''

#Q)10. what is data-type in python Explain thought classification.

'''
In Python, a data type is a classification that determines the kind of value a variable can hold and the operations that can be performed on it.
 Think of it as a label that tells Python how to interpret and work with the data. 
Here's a breakdown of Python data types through classification:
1. Numeric Types:

    int: Represents whole numbers, e.g., 1, 2, -10, 1000.
    float: Represents decimal numbers, e.g., 3.14, 2.718, -0.5.
    complex: Represents complex numbers with real and imaginary parts, e.g., 2 + 3j. 

2. Sequence Types:

    str: Represents a sequence of characters, e.g., "Hello", "Python".
    list: Represents an ordered, mutable collection of items, e.g.,, ["apple", "banana"].
    tuple: Represents an ordered, immutable collection of items, e.g., (1, 2, 3), ("apple", "banana"). 

3. Mapping Type:

    dict: Represents a collection of key-value pairs, e.g., {"name": "Alice", "age": 30}. 

4. Set Types:

    set:
    Represents an unordered, mutable collection of unique elements, e.g., {1, 2, 3}.
    frozenset:
    Represents an unordered, immutable collection of unique elements, e.g., frozenset({1, 2, 3}). 

5. Boolean Type:

    bool: Represents a logical value, either True or False. 

6. None Type:

    NoneType: Represents the absence of a value, often used to indicate null or uninitialized variables. 

Mutability:

    Mutable:
    Data types like lists, dictionaries, and sets can be modified after creation.
    Immutable:
    Data types like strings, numbers, and tuples cannot be modified after creation. 

Checking Data Types:

    You can use the type() function to check the data type of a variable
'''

#Q)15.write difference between global and globals with examples.--------------------->
'''
In Python, global and globals() have distinct functionalities when dealing with global variables:
global Keyword:

    Purpose:
    Used to declare that a variable within a function refers to the global variable with the same name.
    Usage:
        Inside a function, use global followed by the variable name to indicate that you are working with the global variable,
          not creating a new local variable.
        This allows you to modify the value of the global variable from within the function. 

Example:
Python
Execution output

x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)

20
globals() Function:

    Purpose: Returns a dictionary representing the current global symbol table.
    Usage:
        Provides a way to access and manipulate global variables dynamically.
        Useful when you don't know the exact name of the global variable in advance or when 
        you want to work with a large number of global variables. 

Example:
Python
Execution output

x = 10

def access_global():
    print(globals()['x'])

access_global()

globals()['x'] = 30
print(x)

10
30
Key Difference:

    global is a keyword used to declare a variable within a function as a global variable.
    globals() is a function that returns a dictionary containing all global variables. 

When to use:

    Use global when you need to modify the value of a specific global variable within a function.
    Use globals() when you need to access or manipulate global variables dynamically or
      when you want to work with a collection of global variables
'''
#Q)16. Explain what is range() and attributes---------------------------------------->

'''

In Python, range() is a built-in function that generates a sequence of numbers. 
It's commonly used in loops to iterate a specific number of times.
How range() works:

    Syntax:
    range(start, stop, step)
        start (optional): The starting value of the sequence (default is 0).
        stop: The ending value of the sequence (not included in the sequence).
        step (optional): The increment between each number in the sequence (default is 1). 
    Examples:
        range(5) generates the sequence 0, 1, 2, 3, 4.
        range(2, 6) generates the sequence 2, 3, 4, 5.
        range(1, 10, 2) generates the sequence 1, 3, 5, 7, 9. 

Attributes of range():

    start: Returns the starting value of the range object.
    stop: Returns the ending value of the range object (not included).
    step: Returns the increment used in the range object. 

Example:
Python
my_range = range(1, 6)
print(my_range.start)  # Output: 1
print(my_range.stop)   # Output: 6
print(my_range.step)   # Output: 1
'''
#Q)17.write a programm to check given hear is leep year or not.------------------------->
'''n=int(input("enter your year"))
if (n%100!=0 and n%4==0):
         print(n,"this is leap yeaar!!")
elif (n%100==0 and n%400==0):
         print(n,"this is leap year!!") 
else:
        print(n,"this is not leap year!!")  '''              


#Q)21. explane *args and **kwargs with example------------------------------>
'''
In Python, *args and **kwargs are special syntaxes used in function definitions to allow for a variable number of arguments.
*args:

    *args allows you to pass a variable number of non-keyworded arguments to a function.
    The arguments are passed as a tuple.
    You can use any name after the *, but args is the convention. 

Example:
Python
Execution output

def print_numbers(*args):
  for num in args:
    print(num)

print_numbers(1, 2, 3)
print_numbers(10, 20, 30, 40)

1
2
3
10
20
30
40
**kwargs:

    **kwargs allows you to pass a variable number of keyword arguments to a function.
    The arguments are passed as a dictionary.
    You can use any name after the **, but kwargs is the convention. 

Example:
Python
Execution output

def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_info(name="John", age=30)
print_info(city="New York", country="USA")

name: John
age: 30
city: New York
country: USA
Using both *args and **kwargs:
You can even use both *args and **kwargs in the same function definition:
Python
Execution output

def print_all(*args, **kwargs):
  print("Non-keyword arguments:", args)
  print("Keyword arguments:", kwargs)

print_all(1, 2, 3, name="John", age=30) 
 '''
#Q)22. Explane what is index() and there attributes----------------------------->

'''In Python, the index() method is used to find the first occurrence of a specified element within a sequence, such as a string or a list.
Syntax:
Python

sequence.index(element, start, end)

Parameters:

    element: The value you're searching for.
    start (optional): The index at which to start searching.
    end (optional): The index at which to stop searching (exclusive). 

Return Value:

    The index of the first occurrence of the element.
    If the element is not found, a ValueError is raised. 

Examples:
Python

my_list = [10, 20, 30, 20, 40]

# Find the index of 20
index = my_list.index(20)
print(index)  # Output: 1

# Find the index of 20 starting at index 2
index = my_list.index(20, 2)
print(index)  # Output: 3

# Find the index of 50 (raises ValueError)
index = my_list.index(50)  # Raises ValueError: 50 is not in list

Important Points:

    The index() method only returns the index of the first occurrence of the element.
    To find all occurrences of an element, you can use a loop and the index() method with the start parameter.
    Use try-except blocks to handle the ValueError that is raised if the element is not found '''
#Q)23. write a find  prime number-------------------------->
'''n= int(input("Enter a number: "))

if n>1:
    for i in range(2 ,n):
        if (n% i) == 0:
            print( n,"is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number") '''

                        
#W.A.P to palindrome number---------------------------------------------------------->
''''n=int(input("enter the number"))
temp=n
sum=0

while n>0:
       r=n%10
       sum=sum*10+r
       n=n//10

if (temp==sum):
    print("it is your palindrome number")

else:
    print("it is not palindrome number")'''

                          
# python program to display all number withen a range exept the prime number---------------------->

'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Numbers within the range except prime numbers:")
for num in range(start_range, end_range + 1):
    if not is_prime(num):
        print(num, end=" ")
    else: 
        ("print number")   ''' 


''' while True:
     print["1 Additon\n 2 sub \n 3 mult \n 4 off"]
     n=int(input("enter waht you want to your number"))
     x=[1,2,3,4]
     if n in x:
          x=int(input("enter first number:"))
          y=int(input("enter second number:"))
          if n==1:
               print("Addtion=",x+y)
          elif n==2:
               print("multi=",x-y)
          elif n==3:
               print("div=",x/y)
          elif n==4:
               print("sub=",x-y) 
     elif n==5:
          break
     else:
          print("enter right number:") '''






                       





































































