class Microwave:
    def __init__(self, brand, power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self):
        if self.turned_on:
            print(f'Microwave {self.brand} is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is turned on.')

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave {self.brand} is now turned off.')
        else:
            self.turned_off = True

    def run(self, seconds):
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds.')
        else:
            print(f'please turn on your microwave first...')

    def __add__(self, other):
        return f'{self.brand} + {other.brand}'

    def __mul__(self, other):
        return f'{self.brand} * {other.brand}'


smeg = Microwave('canon', 15)
smeg.turn_on()
smeg.run(45)
smeg.turn_off()

bosch = Microwave('bosch', 22)
bosch.turn_on()
bosch.run(45)
bosch.turn_off()

print(smeg + bosch)
print(smeg*bosch)
