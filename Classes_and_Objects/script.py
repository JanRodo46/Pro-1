# define the Vehicle class
class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 0

    def description(self):
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}"


car1 = Vehicle()
car1.name = "Fer"
car1.kind = "car"
car1.color = "red"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "car"
car2.color = "blue"
car2.value = 10000
print(car1.description())
print(car2.description())
