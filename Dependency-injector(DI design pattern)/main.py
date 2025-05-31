# main.py
from container import Container

container = Container()
car = container.car_provider1()  # DI framework injects Engine automatically
car = container.car_provider2()  # DI framework injects Engine automatically

print(car.drive())  # Output: "Engine started!"