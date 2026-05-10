class Car:
    def __init__(self, reg, max_speed):
        self.registration_number = reg
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print(car.registration_number)
print(car.maximum_speed)
print(car.current_speed)
print(car.travelled_distance)