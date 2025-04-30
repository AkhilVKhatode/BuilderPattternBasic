class Car:
    def __init__(self, builder):
        self.engine = builder.engine
        self.wheels = builder.wheels
        self.seats = builder.seats
        self.color = builder.color
        self.sunroof = builder.sunroof
        self.navigation_system = builder.navigation_system

    def __str__(self):
        return f"Car [engine={self.engine}, wheels={self.wheels}, seats={self.seats}, color={self.color}, sunroof={self.sunroof}, navigation_system={self.navigation_system}]"

    # CarBuilder nested class
    class CarBuilder:
        def __init__(self):
            self.engine = None
            self.wheels = 4  # Default value
            self.seats = 5   # Default value
            self.color = "Black"  # Default value
            self.sunroof = False  # Default value
            self.navigation_system = False  # Default value

        # Builder methods to set attributes
        def set_engine(self, engine):
            self.engine = engine
            return self

        def set_wheels(self, wheels):
            self.wheels = wheels
            return self

        def set_seats(self, seats):
            self.seats = seats
            return self

        def set_color(self, color):
            self.color = color
            return self

        def set_sunroof(self, sunroof):
            self.sunroof = sunroof
            return self

        def set_navigation_system(self, navigation_system):
            self.navigation_system = navigation_system
            return self

        # Build method to create a Car object
        def build(self):
            return Car(self)  # Return a new Car created using the builder's values


# Main code for testing
if __name__ == "__main__":
    # Creating a car using the Builder pattern
    builder = Car.CarBuilder()
    car1 = builder.set_engine("V8").set_color("Red").set_seats(5).set_sunroof(True).build()
    print(car1)

    # Creating another car with different specifications
    car2 = builder.set_engine("V6").set_color("Blue").set_seats(4).build()  # Sunroof and Navigation are default
    print(car2)
