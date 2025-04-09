# Car class with encapsulation
def print(param):
    pass


class Car:
    def __init__(self, brand, speed):
        self.__brand = brand  # Private attribute
        self.__speed = speed  # Private attribute

    # Method to accelerate
    def accelerate(self, increase):
        self.__speed += increase
        print(f"{self.__brand} is now going at {self.__speed} km/h.")

 # Getter for speed
    def get_speed(self):
        return self.__speed

# Main function
if __name__ == "__main__":
    my_car = Car("Toyota", 50)
    my_car.accelerate(20)  # Output: Toyota is now going at 70 km/h.
    print(f"Current Speed: {my_car.get_speed()} km/h")
