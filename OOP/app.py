"""
# OOP
------
Object-oriented programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. 
It aims to model real-world entities and their interactions. 
OOP promotes code reusability, modularity, and maintainability by encapsulating data and behavior within classes.

It allows us to think of the data in our program in terms of real-world objects, with properties(state) and behaviors(actions).
These objects can be passed throughout our program

A class is a blue print for creating objects.
An object is an instance of a class.
An instance is a specific object created from a class.
Self is a magic word that refers to a perticular intstance


In the provided code snippet, you can see the implementation of a simple class called Person. 
The class has attributes such as first_name, last_name, and age, and methods such as walk(). 
An object of the Person class is created, and its attributes and methods are accessed and utilized.

The code also demonstrates the use of various data types in Python, including strings, booleans, integers, floats, dictionaries, lists, 
tuples, sets, frozen sets, and None. 
These data types are essential for working with variables and data in Python.


# PRINCIPLES OF OOP
-------------------
Encapsulation -> The practise of building data and methods that operate on it into a single unit/ class.
              -> It also involves reatricting direct access to some of an object's components.
              -> "self._name" -> shows a private attribute. 
              
            TYPES OF ATTRIBUTES
              private
              public
              protected
              static
              
Inheritance -> The mechanism by which one class(child/derivative class)inherits the attributes & methods from another class(parent/base class)
            -> The child has all the attributes from the parent
            
Polymorphism -> The ability of different objects to respond to the same method in different ways
             -> It allows methods to do different things based on the object it is acting upon
             
Abstraction -> The concept of hiding the complex implementatin details and showing only the necessary features of an object.
            -> Simplifies interaction with the objects
            
          
            
# FUNDAMENTAL RELATIONS IN OOP
-------------------------------
Association -> Relationship btwn classes where each class has an independent existence and they are loosely connected
            -> It is often used to represent a simple connection between objects
            -> It enables us to build a scallable application
            -> A scalable application refers to the capability of a system, specifically a web application, 
            to handle an increased load efficiently, potentially even growing in capacity to accommodate that growth.
            
Aggregation -> Relationship where one class contain other classes but the parts can exist independently
            -> It is often used to represent a more complex relationship between objects
            -> It enables us to build a scallable application
            
Composition -> A strong relationship where one class is composed of other classes and the parts are essential to the existance
            -> The contained objects cannot exist without the container
Inheritance -> Relationship that allows a new class to inherit the properties and behaviors of another existing class
            -> It enables us to build a hierarchical relationship between classes
"super().__init__(name)" -> Is a Python language feature that allows a child class to call the constructor of its parent class.


# SIMPLIFIED EXPLANATION
------------------------
1. In Python, inheritance is a mechanism where a class (child class) inherits properties and methods from another class (parent class).
2. The super() function is a built-in Python function that returns a proxy object (temporary object of the parent class) 
that allows you to call methods of the parent class.
3. When you call super().__init__(name), it essentially means "call the constructor (__init__ method) of the parent class with the argument name".
4. The parent class's constructor is executed, initializing any attributes or performing any necessary operations.
5. This allows the child class to inherit the attributes and methods of the parent class, 
while also being able to add its own unique attributes and methods.

In summary, super().__init__(name) is used to call the constructor of the parent class from within a child class in Python, 
allowing the child class to inherit the parent class's attributes and methods while also initializing its own attributes.

"""

class Person:
    # age = 34
    # first_name = 'Leslie'
    # last_name = 'Mwangi'

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    
    # defining object behaviour through methods
    def walk(self):
        print(f'{self.first_name} is walking')

# creating an object by creating class instance
Leslie = Person("Leslie", "Mwangi", "24")

print(Leslie.first_name)

Joseph = Person("Joseph", "Njoroge", "34")

print(Joseph.last_name)
print(Joseph.walk())


# create a class of a car. add any attributes. add 2-3 methods that describes the car


# VARIABLES
# We use snake case naming convention
# class_name, attribute_name, method_name

# 1. String
# we use ""/''
first_name = "Leslie"
last_name = "Mwangi"
age = 24

# f-string -> used to achieve sting interpolation
print(f"{first_name} {last_name}")

# 2. Boolean -> true/ false
# they are statements that eveluate to true /false
is_student = True
is_teacher = False
print(is_student)
print(is_teacher)
print (1==1)
print (1=="1")

# 3. Integer -> whole numbers without decimals e.g 2,4,5,354
print(type(3))

# 4. Float -> decimal numbers e.g 2.3, 4.56
print(type(3.0))

# 5. Dictionary (dict) -> Collection of properties stored in key/value pairs
Person = {
    "first_name": "Leslie",
    "last_name": "Mwangi",
    "age": "24"
}
print(Person)
print(Person["first_name"])
print(f"{Person['first_name']} {Person['last_name']} {Person['age']}")

# 6. List -> arrays in js
scores = [33, 45, 69, 80]
for score in scores:
    print(score)
# print(scores)
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[0:2])

# addition off objects
scores.append(90)
print(scores)


# 7. Tuple -> similar to lists btu they are imutable
# they are defined using parentheses
scores_tuple = (33, 45, 69, 80)
print(scores_tuple)

names = ("Joseph", "victor")
print(type(names))
print(names)
print(names[0])
print(len(names))


# 8. Set -> unordered collection of unique items
# they are defined using curly brackets
scores_set = {33, 45, 69, 80}
print(scores_set)
print(type(scores_set))
print(len(scores_set))
# print(scores_set[0])

student_ids = {1, 2, 3, 4, 5, 4}
print(student_ids)
# it will print 1,2,3,4,5 because it removes duplicates in the code

# adding a set
student_ids.add(6)
print(student_ids)

# removing a set
student_ids.remove(4)
print(student_ids)

student_ids.discard(4)
print(student_ids)

# creating empty sets
cars = set(["Audi", "BMW", "Ford"])
cars.add("Mercedes")
cars.remove("Ford")
new_cars = {"Jeep", "G-Wagon", "Toyota"}
print(type(cars))
print(cars & new_cars)

print(cars | new_cars)
print(cars - new_cars)

# 9. Frozen Set

# null/undefined -> None
# print is console.js
# print is used to output data to the console
# return is used to 
print("Happy New Year")