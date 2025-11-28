# define the Vehicle class
class Vehicle:
    def __init__(self, name, kind, color, value=0):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
        if value < 0:
            raise ValueError("Value cannot be negative")

    def description(self):
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}"


car1 = Vehicle("Fer", "car", "red", 50)
car2 = Vehicle("Jump", "car", "blue", 10000)
print(car1.description())
print(car2.description())
