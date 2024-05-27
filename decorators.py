# Decorator: syntax that allows us to add functionality to an object without modifying its structure.
# Decorators provide us yet another way to write DRY code through providing extra functionality to functions beyond arguments.
# Decorator-> A function that takes another function as an argument, 
# adds a functionality and then returns another function without altering the sourcecode of the original function passed in

# A decorator is a special type of function that allows you to add extra functionality to an existing function, without modifying its structure. 
# This can help you write more DRY (Don't Repeat Yourself) code.


# To write your first decorator, you'll need to tie all of these concepts together. You will need to write a function that...

# 1. Takes a function as an argument.
# 2. Has an inner function defined inside of it.
# 3. Returns the inner function.
# 4. Calls the inner function with the original function's arguments.

def decorator_function(original_function):
    # inner function
    # This code accepts any number of positional arguments (*args) and any number of keyword arguments (**kwargs).
    # The positional arguments are packed into a tuple called args, and the keyword arguments are packed into a dictionary called kwargs.
    def wrapper_function(*args, **kwargs):
            # The .format() method in Python is used for string formatting.
            # It allows you to insert values into placeholders within a string.
            # The .format() method is used to insert the name of the original_function into the string 'wrapper executed this before {}'.
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function(*args, **kwargs)
    return wrapper_function

# The wrapper_function is the function that gets returned by the decorator_function. 
# It takes any number of arguments (*args and **kwargs) and prints a message before calling the original function with those arguments.

@decorator_function
def display():
    # When we execute the display function it will print out ('display function ran')
      print('display function ran')

# The variable decorated_display will pass the display_function to our decorator function
# The decorator_function will return the wrapper which is waiting to be executed
# The wrapper will execute the display function and print out the message

# # decorated_display = decorator_function(display)

# Decorated_display variable = wrapper_function that is waiting to be executed
# When the wrapper_function is executed, it executes the original function that is passed in and returned

# # decorated_display()

display()

@decorator_function
def display_info(name, age):
      print('display_info ran with arguments ({}, {})'.format(name, age))
      # The decorator_function will return the wrapper which is waiting to be executed
      # decorated_display_info = decorator_function(display_info)
      # Decorated_display_info variable = wrapper_function that is waiting to be executed

display_info('John', 25)





def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(1200)
# I'm off duty!
wash_dishes(1000)
# I'm off duty!
chop_vegetables(1200)
# Chopping the vegetables...