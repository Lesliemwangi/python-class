"""
control flow
1. Selection statement -> use to run code (if/switch)
2. Iteration statement -> use to repeat code (for/while)
3. Jump statement -> use to transfer control (break/continue/return)
4. Exception handling -> use to handle runtime errors (try/except/finally)
5. Repetition -> running a piece of code until a certain condition is met (while/ do... while)
"""

"""
1. Comparison Operators -> ==
2. Logical Operators -> not, and, or
3. Membership Operators -> in, not in
4. Identity Operators -> is, is not
5. Bitwise Operators -> &, |, ^, ~, <<, >>
6. Assignment Operators -> =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=
7. Ternary Operators -> condition? value1 : value2
8. Operator Precedence -> ()
9. Number Operator -> <, >
"""

age = 19

if age >= 18:
    print("This is an adult")
else:
    print("Not an adult")
    
user = 'student'

if user == 'student':
    print("Student has logged in")
elif user == 'tm':
    print("TM has logged in")
elif user == 'pod':
    print("Pod Lead has logged in")
else:
    
    print("User not found")
    
    
# try/except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# try/except/finally    
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This code will always run")
    
    
    
try:
    print("successful operation")
    raise Exception("error")
except:
    print("unsuccessful operation")
    
    
def add_number(num):
    try:
        if type(num) is not int:
            raise TypeError("num must be an integer")
        return num + 10
    
    except TypeError:
        print("num must be an integer")
        return "Value passed is not a number"
    except AssertionError:
        assert "none"
    
result = add_number("10")
print(result)
result = add_number(30)
print(result)

"""
# Types of errors

TypeError
ArithmeticError
AssertionError
ZeroDivisionError
SyntaxError
IndentationError
IndexError
KeyError
ValueError
NameError
EOFError

"""