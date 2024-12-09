class Animal:
    alive = []  # Class attribute to keep track of all alive animals

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def check_health(self) -> None:
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)
            print(f"{self.name} has died.")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        state = "hidden" if self.hidden else "visible"
        print(f"{self.name} is now {state}.")


class Carnivore(Animal):
    def bite(self, target: str) -> None:
        if not isinstance(target, Herbivore):
            print(f"{self.name} can only bite herbivores")
            return
        if target.hidden:
            print(f"{target.name} is hiding. {self.name} cannot attack")
            return

        target.health -= 50
        print(f"{self.name} bites {target.name}, "
              f" health decreased on {target.health}.")
        target.check_health()
