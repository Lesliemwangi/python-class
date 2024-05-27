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