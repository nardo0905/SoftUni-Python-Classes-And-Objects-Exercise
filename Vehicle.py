class Vehicle:

    owner = None

    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {(money - self.price):.2f}'
        if money < self.price:
            return 'Sorry, not enough money'
        if self.owner is not None:
            return 'Car already sold'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = 'car'
model = 'BMW'
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, 'Peter'))
print(vehicle)
print(vehicle.buy(35000, 'George'))
print(vehicle)
print(vehicle.owner)
vehicle.sell()
print(vehicle.owner)
print(vehicle)
