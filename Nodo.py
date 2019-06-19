
#Clase que implementa un nodo, contiene valor, referencia al padre(inicialmente el mismo) y valor de rank
class Nodo:
    def __init__(self, x):
        self.value = x
        self.padre = self
        self.rank = 0