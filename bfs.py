#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
#To make the code more efficient, you can use the deque object from the collections module instead of a list, 
# for implementing queue. This way you can use the popleft() method instead of the  pop(0) built-in function on queue. 
# This will result in a quicker code as popleft()has a time complexity of O(1) while pop(0) has O(n).

from collections import deque
import queue
import DisjointSetHeuristicas
import Arbol

def bfs_completo(matriz,nodos):
    blancos = [False] * len(nodos)
    foresta = []
    for u in nodos:
        if(blancos[u] == False):
            arbol = bfs(u,matriz,blancos)
            foresta.append(arbol)
    return foresta

def bfs(u, matriz, blancos):
    cola = queue.Queue()
    blancos[u] = True
    cola.put(u)
    pertenecientes = []
    
    while (not cola.empty()):
        actual = cola.get()
        pertenecientes.append(actual)
        if(actual in matriz):
            for v in matriz.get(actual):
                if(blancos[v]==False):
                    blancos[v] = True
                    cola.put(v)
    return pertenecientes

def conexo_DS(nodos,arcos):
    listaDS = []
    for nodo in nodos:
        a = [DisjointSetHeuristicas.MakeSet(nodo)]
        listaDS.append(a)
    for arco in arcos:
        indu = 0
        indv = 0
        indicesEncontrados = False
        indice = 0
        nodoUencontrado = False
        nodoVencontrado = False
        while ((indice < len(listaDS)) & (indicesEncontrados == False)):
            j = 0
            while (j < len(listaDS[indice])):
                nodo = listaDS[indice][j]
                if (nodo.value == arco.getArco()[0]):
                    indu = indice
                    nodoUencontrado = False
                else:
                    if (nodo.value == arco.getArco()[1]):
                        indv = indice
                        nodoVencontrado = False
                j = j+1
                indicesEncontrados = nodoUencontrado & nodoVencontrado
            indice = indice + 1
        u = listaDS[indu][0]
        v = listaDS[indv][0]
        representante_u = DisjointSetHeuristicas.findSet(u)
        representante_v = DisjointSetHeuristicas.findSet(v)
        if (representante_u != representante_v):
            DisjointSetHeuristicas.union(u,v)
            nuevoConjuntoDisjunto = []
            nuevoConjuntoDisjunto.extend(listaDS[indu])
            nuevoConjuntoDisjunto.extend(listaDS[indv])
            if (indu < indv):
                listaDS.remove(listaDS[indu])
                listaDS.remove(listaDS[indv-1])
            else:
                listaDS.remove(listaDS[indv])
                listaDS.remove(listaDS[indu-1])
            listaDS.append(nuevoConjuntoDisjunto)
            lAux = []
            for lista in listaDS:
                l = [nodo.value for nodo in lista]
                lAux.append(l)
    return lAux