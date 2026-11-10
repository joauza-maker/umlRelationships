class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):  
    def honk(self):
        print("Beep beep!")

my_car = Car()
my_car.move()
my_car.honk()
