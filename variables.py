"""
VARIABLES
To declare a variable we type the name of the variable followed by an equal sign and the value we want to assign to it
Python accepts numbers with a decimal point or whole numbers
Python also accepts strings which are sequences of characters enclosed in quotes
Variables cannot start with a number
Variables cannot contain spaces
Variables cannot contain special characters except underscore
Variables are case sensitive
"""

age = 20
print(age)

price = 19.95
print(price)

# If we want to use multple words we use (_) to separate them and make them readable
# We can also use a variable to store a string
first_name = 'Leslie'
print(first_name)


"""
EXPRESSIONS AND STATEMENTS
An expression is any sort of code that returns a value(1+1)
An expression is a combination of values, variables, and operators
An expression evaluates down to a single value
A statement is a unit of code that has an effect, like creating a variable
A statement is an operation on a value (name="Leslie")
A statement does not evaluate down to a single value
A program is formed by a series of statements and each statement is put on its own line
We can use a semi-colon to add more than one statement on a single line

"""

name = "Imani"
print(name)

name = "Joseph"; print(name)


"""
DATA TYPES
Python has several built-in data types
Python has five standard data types
1. Numbers -> integer numbers are represented using the "int" class
           -> floating numbers are the decimals/ fractions
2. String
3. List
4. Tuple
5. Dictionary
6. Set
7. Boolean
8. NoneType
"""

name = "Leslie"
print(type(name))  # Output: <class 'str'>
print(type(name) == str)
print(isinstance(name, str))
# This will output true because the name is a string

age = 20
print(type(age))  # Output: <class 'int'>
print(isinstance(age, int))
# This will output true because the age is an integer
# isinstance() is a function that checks if an object is an instance of a class
num = 3.5
print(type(num))  # Output: <class 'float'>
print(isinstance(num, float))
# This will output true because the num is a float (it has a decimal)

# We can convert an integer into a float by adding the name float infront of the integer
num = float(3)
print(type(num))  # Output: <class 'float'>
print(isinstance(num, int))
# This will output false because the num is an integer (it does not have a decimal)

num = "3"
print(type(num))  # Output: <class 'str'>
print(isinstance(num, str))
# This will output true because the name is a string

# We can convert a string into an integer by adding the name int infront of the string
num = int("3")
print(type(num))  # Output: <class 'int'>
print(isinstance(num, int))

# Casting -> THis is a way to extract an integer from the string
number = "29"
age = int(number)
print(isinstance(age, int))

"""
OPERATORS
Operators are special symbols that represent computations like +, -, /, *, etc
Operators are used to perform operations on variables and values
Operators are classified as unary, binary, and ternary
Unary operators operate on a single value
Binary operators operate on two values
Ternary operators operate on three values

Types of operators
1. Arithmetic Operators -> Used to do math 
                        eg; + -> Addition
                            - -> Subtraction
                            * -> Multiplication
                            / -> Division
                            % -> Modulus/ Remainder
                            ** -> Exponentiation (power eg; 4**2 = 16)
                            // -> Floor Division -> Does a division problem and rounds down to the nearest whole number
                            
                        
2. Assignment Operators(=)-> Used to assign a value into a variable
                          -Also used to assign a variable value to another variable
                          eg; a = 5 -> Assigns 5 to a
                          
3. Comparison Operators -> Used to compare values
                        eg: == -> Equals to
                            != -> Not equals to
                            > -> Greater than
                            < -> Less than
                            >= -> Greater than / equal to
                            <= -> Less than / equal to
                           
4. Logical Operators -> Used to combine conditions
                     eg: and -> Logical and
                          or -> Logical or
                         not -> Logical not
                          in -> Check if a value is in a sequence
                          is -> Check if two variables are the same object
                          is not -> Check if two variables are not the same object
    *Logical operators are also known as boolean operators
    

5. Membership Operators
6. Identity Operators
7. Bitwise Operators
8. Ternary Operators

"""

# ARITHMETIC OPERATORS
# The plus operator can also be used to concactenate string values
print("Hello " + "World")  # Output: Hello World

# We can also combine the arithmetic operators with assignment operators
x = 5
x += 3  # This is equivalent to x = x + 3
print(x)  # Output: 8
x -= 2  # This is equivalent to x = x - 2
print(x)  # Output: 6
x *= 3  # This is equivalent to x = x * 3
print(x)  # Output: 18
x /= 2  # This is equivalent to x = x / 2
print(x)  # Output: 9.0

age = 8
age +=8  #age = age + 8
print(age)  # Output: 16

# COMPARISON OPERATORS
# These operators are used to compare values
# They return a boolean value (True or False)
x = 5
y = 3
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x >= y)  # Output: True
print(x <= y)  # Output: False,


# BOOLEAN/ LOGICAL OPERATORS
# These operators are used to combine conditions
# They return a boolean value (True or False)
# They are the NOT, AND, OR
x = 5
 


