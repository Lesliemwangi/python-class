# SEQUENCES LAB

def print_fibonacci(length):
    if length == 0:
        print('[]')
    elif length == 1:
        print('[0]')
    else:
        fib = [0, 1]
        for i in range(2, length):
            fib.append(fib[i - 1] + fib[i - 2])
            
# What is the meaning of this code "fib.append(fib[i - 1] + fib[i - 2])" 
# The code snippet fib.append(fib[i - 1] + fib[i - 2]) is part of a function that generates the 
# Fibonacci sequence up to a given length.

# Here's what it does:
# Inside a loop that runs from the 2nd index (i = 2) to the desired length (i < length), 
# the code calculates the next number in the Fibonacci sequence by 
# adding the previous two numbers (fib[i - 1] and fib[i - 2]).

# The calculated number is then appended to the fib list using the append() method.
# This way, the function builds the Fibonacci sequence iteratively, 
# starting from the first two numbers (0 and 1). The resulting sequence is stored in the fib list, 
# which is then printed in the desired format.

        print('[' + ', '.join(map(str, fib)) + ']')
        
#  What is the meaning of this code "print('[' + ', '.join(map(str, fib)) + ']')"
# The code snippet print('[' + ', '.join(map(str, fib)) + ']') is part of a function that 
# prints the Fibonacci sequence in a formatted manner.

# Here's what it does:
# The map() function is used to convert each number in the fib list to a string. 
# This is necessary because the join() method concatenates elements of a list into a string, 
# but it requires all elements to be of the same type.


# The join() method is then used to concatenate all the string elements of the fib list into a single string, 
# separated by commas. The resulting string is enclosed in square brackets ([]) 
# to form a valid representation of the Fibonacci sequence.
# Finally, the print() function is used to display the formatted Fibonacci sequence.

# DATA STRUCTURES
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:

        print(f"{food['name']} 🌶")
        print(f"{food['cuisine']} 🌶")
        print(f"{food['heat_level']} 🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶")
        print()
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    spiciest_foods = get_spicy_food_by_cuisine(spiciest_foods, cuisine)
    return spiciest_foods
    # return [food for food in spicy_foods if food["cuisine"] == cuisine]

def print_spiciest_foods(spicy_foods):
    
    for food in spicy_foods:
        print(f"{food['name']} 🌶")
        print(f"{food['cuisine']} 🌶")
        print(f"{food['heat_level']} 🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶��🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶")
        print()
    
    
    # spiciest_foods = get_spiciest_foods(spicy_foods)
    # print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods



