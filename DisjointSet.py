import Nodo



def MakeSet(x): #x valor
    return Nodo.Nodo(x)

def findSet(x): #x nodo
    if (x.padre != x):
        x.padre = findSet(x.padre)
    return x.padre

def joinSet(x,y):
    if(x.profundidad < y.profundidad):
        y.profundidad +=1
        x.padre = y
        return y
    else:
        x.profundidad +=1
        y.padre = x
        return x
