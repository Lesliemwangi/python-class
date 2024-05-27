# oop organizes code to have a blue print to make it easier to read
# oop is a way to organize code to make it easier to read

# OOP
# Principles of OOP
# 1. Abstraction -> Hide ipmlementation details. Hide what happens in the background
# 2. Inheritance ->uses classes 
# Allows us to create blue prints of objects with attributes and behaviour (methods)
# 3. Encapsulation
# 4. Polymorphsm
# 5. Composition

class Student:
    cohort = "SDF-FT09"
    def __init__(self, name, age, tm, is_architect=True):
        self.name = name
        self.age = age
        self.tm = tm
        self.is_architect = is_architect
        
    def do_codility(self):
        print("Solving codility program!")
    def learn(self):
        print("Going through canvas!")
    def get_age(self):
        print("Retrieving the name")
        return self._age
    def set_age(self, age):
        if(type(age) in(int, float)) and (18 <= age <= 130):
            print(f"setting the age to {age}")
            self._age = age
        else:
            print("Age is not valid")
            # age = property(get_age, set_age)
# instasiation
# remove print to remove the output none
stud1 = Student("Leslie", "23", "Nelson", False)
stud2 = Student("Victor", "18", "Hamida")
stud1.do_codility()
print(stud1.name)
print(stud1.tm)
print(stud1.is_architect)
print(stud1.cohort)
stud2.learn()
print(stud2.tm)
print(stud2.name)


   
    #     self.name = name
    #     self.age = age
    #     self.grade = grade
    #     def get_grade(self):
    #         return self.grade
    #     def get_name(self):
    #         return self.name

    #     def set_grade(self, grade):
    #         self.grade = grade
