class Vehicle:
    def __init__(self) -> None:
        pass

    def go(self, city: str) -> None:
        print(f"Go to {city}")


class Car(Vehicle):
    def wash(self) -> None:
        print("Washing the car...")


class Train(Vehicle):
    def buy_ticket(self) -> None:
        print("Buying the ticket...")


car = Car()
car.wash()  # "Washing the car..."
car.go("London")  # "Go to London"

train = Train()
train.buy_ticket()  # "Buying the ticket..."
train.go("Berlin")
