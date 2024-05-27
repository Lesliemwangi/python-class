# single line comment

"""
multi line comment
"""
# when you put the = in the argument it becomes the keyword
def greet(time = "morning"):
    # print("Hello World")
    # print("How are you?")
    print(f"Good {time}")
# call the function
greet()
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
    
sum_of_two_nums = add_numbers(20,30)
print(sum_of_two_nums)

