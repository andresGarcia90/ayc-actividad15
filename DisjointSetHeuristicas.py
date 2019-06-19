import Nodo

def MakeSet(x): #x valor
    return Nodo.Nodo(x)

def findSet(x): #x nodo
    if (x.padre != x):
        x.padre = findSet(x.padre)
    return x.padre

def link(x,y):
    if(x.rank > y.rank):
        y.padre = x
    else:
        x.padre = y
        if (x.rank == y.rank):
            y.rank = y.rank + 1

def union(x,y):
    link(findSet(x),findSet(y))