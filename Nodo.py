
class Nodo:
    def __init__(self, x):
        self.value = x
        self.padre = self
        self.rank = 0