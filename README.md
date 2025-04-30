# BuilderPattternBasic

This repository demonstrates the **Builder Pattern** in Python, showcasing how to construct a `Car` object with customizable attributes such as engine type, number of seats, color, sunroof, and navigation system.

The Builder Pattern is a design pattern used to separate the construction of a complex object from its representation, allowing the same construction process to create different representations.

## Project Overview

In this example, we create a `Car` class with the following attributes:

- Engine type (e.g., V8, V6)
- Number of wheels (default is 4)
- Number of seats (default is 5)
- Car color (default is Black)
- Whether the car has a sunroof (default is False)
- Whether the car has a navigation system (default is False)

A `CarBuilder` class is used to progressively build the `Car` object by setting these attributes using method chaining.

## Features

- Demonstrates the use of the Builder Pattern for object construction.
- The `CarBuilder` class allows flexibility in creating different `Car` objects with varying attributes.
- Defaults are provided for certain attributes like wheels, seats, color, sunroof, and navigation system.

Usage
Here’s how you can create Car objects with different configurations using the Builder Pattern:
```
builder = Car.CarBuilder()

# Creating a car with customized attributes
car1 = builder.set_engine("V8").set_color("Red").set_seats(5).set_sunroof(True).build()
print(car1)

# Creating another car with different specifications (defaults for sunroof and navigation)
car2 = builder.set_engine("V6").set_color("Blue").set_seats(4).build()
print(car2)
```
This will print the following output:
```
Car [engine=V8, wheels=4, seats=5, color=Red, sunroof=True, navigation_system=False]
Car [engine=V6, wheels=4, seats=4, color=Blue, sunroof=False, navigation_system=False]
```
