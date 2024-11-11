class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person_instance = Person("Alice", 30, "Female")

# Call the introduce method
person_instance.introduce()


# Attributes:
# name, age, and gender are set up as instance attributes in the __init__ method.

# introduce Method:
# The introduce method formats a string that introduces the person, using the instance’s attributes.

# Creating an Instance and Displaying Information:
# An instance of Person named person_instance is created with sample data.
# Calling introduce() on person_instance displays the introduction message.
