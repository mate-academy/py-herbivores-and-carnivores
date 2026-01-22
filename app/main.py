class Animal:
    # lista com todos os animais vivos (instâncias)
    alive = []

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hidden = False
        # adicionar à lista de vivos
        Animal.alive.append(self)

    def __repr__(self):
        # formato pedido: {Name: Bagira, Health: 100, Hidden: False}
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        # alterna o estado hidden
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey):
        # só pode morder Herbivore
        if not isinstance(prey, Herbivore):
            return  # não faz nada se não for herbívoro

        # não morde se a presa estiver escondida
        if prey.hidden:
            return

        # reduzir saúde em 50 (mínimo 0)
        prey.health -= 50
        if prey.health <= 0:
            prey.health = 0
            # remover dos vivos, se presente
            try:
                Animal.alive.remove(prey)
            except ValueError:
                pass
# write your code here
