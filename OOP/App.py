def read():
    print(f"{Leslie['first_name']} is reading")


Leslie = {
    "first_name": "Leslie",
    "last_name": "Mwangi",
    "read": lambda: print(f"{Leslie['first_name']} is reading")
    # "age": 24,
    # "isStudent": True,
    # "isTeacher": False,
    # "isArchitect": False,
    # "cohort": "Nelson"
}
print(Leslie["first_name"])
print(Leslie["last_name"])

Joseph = {
    "first_name": "Joseph",
    "last_name": "Njoroge",

}
print(Joseph['first_name'])
print(Joseph['last_name'])


"""
CLASSES
"""


class Student:
    cohort = "SDF-FT09"

    def __init__(self, first_name):
        self.first_name = first_name

    def read(self):
        return (f"{self.first_name} is reading")

    # Victor = Student ("Victor")
    # print(Victor.read())


# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


#     # Insertion
#     mids = Student(first_name="Hamida", last_name="Mstafa")
#     print(mids.first_name)


class Student:
    cohort = "SDF-FT09"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def teach(self):
        return f"{self.first_name} {self.last_name} is teaching"
    
    @classmethod
    def sleeping(cls):
        print("The student is sleeping")


# Creating an instance of the Student class
mids = Student(first_name="Hamida", last_name="Mstafa")

# Example usage
print(f"Student Name: {mids.first_name} {mids.last_name}")
print(mids.first_name)
print(mids.cohort)
print(mids.teach())


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        return wrapper
    
@decorator
def say_hello():
    print("Hello!")
