## because of the methods the code redunandancy and increase the code reusability and maintainability.
# there is one level UP in python know as OOP (Object Oriented Programming) which is a programming paradigm that uses objects and classes to structure code. It allows for encapsulation, inheritance, and polymorphism, making it easier to manage and scale complex applications.

class car:
    model = ""
    year = 0
    def __init__(self, make, model, year):
        self.make = make #object attribute
        self.model = model
        self.year = year # self is like this in java and c++ it is used to refer to the current instance of the class.

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has stopped.")

    def honk(self):
        print(f"The {self.year} {self.make} {self.model} is honking: Beep Beep!")