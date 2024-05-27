# single line comment

"""
multi line comment
"""

"""
The def keyword is used to define the function greet().

The function does not take any parameters, indicated by the empty parentheses ().

Inside the function, the print() statement is used to display the greeting message. 

The f-string f"Good {time}" embeds the value of the time variable within the string.

The time variable is referenced within the function, but it is defined outside the function. 

This is a variable scoping concept in Python.

The function is called at the end of the code using greet().

When the greet() function is called, it will print the greeting message "Good week" since the time variable is assigned the value "week" outside the function.
"""
# when you put the "time = morning" as the parameter it becomes the keyword
# it is printed when you put the print without any value "print()"

time = "week"


def greet():
    # print("Hello World")
    # print("How are you?")
    print(f"Good {time}")


# call the function
greet()
# greet("afternoon")
# greet("evening")

"""
The function definition starts with the def keyword followed by 
the function name greet() and an optional parameter list enclosed in parentheses. 

In this case, the parameter list contains time = "morning", 
indicating that time is an optional parameter with a default value of "morning".

The function body is indented, and within it, an f-string f"Good {time}" 
is used to print the greeting message. The curly braces {} enclose the time variable,
which will be replaced with its value when the function is called.

The function ends with a colon :.

In the provided code snippet, the function is defined but not called. 

To use this function, you would need to call it with an optional argument for time. 
For example, greet("afternoon") would print "Good afternoon", and greet("evening") would print "Good evening". 
If no argument is provided, the function will use the default value of "morning".
"""


def greet(time="morning"):
    print(f"Good {time}")


# call the function
greet("afternoon")
greet("evening")


# def sum(num1, num2):
#     print(num1 + num2)

# sum(23,30)
# sum(45,67)


# def sum(num1, num2):
#     return num1 + num2

# print(sum(23,30))
# print(sum(45,67))

def add_numbers(*args):
    # print(args)
    # print(type(args))
    # print(args[0])
    # print(args[1])
    # return args[0] + args[1]
    return sum(args)


sum_of_two_nums = add_numbers(20, 30)
print(sum_of_two_nums)


def print_names(**kwargs):
    for key in kwargs:
        print(kwargs[key])


print_names(first_name="Leslie", last_name="Mwangi")


def names(**kwargs):
    for key, value in kwargs.items():
        print(value)
        # print(f"{key} is {value}")


names(first_name="Joseph", last_name="Njoroge")
