#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
#To make the code more efficient, you can use the deque object from the collections module instead of a list, 
# for implementing queue. This way you can use the popleft() method instead of the  pop(0) built-in function on queue. 
# This will result in a quicker code as popleft()has a time complexity of O(1) while pop(0) has O(n).

from collections import deque
import queue
import DisjointSetHeuristicas
import Arbol

#metodo que realiza el recorrido bfs y retorna un conjunto con el/los arboles resultantes
def bfs_completo(matriz,nodos):
    blancos = [False] * len(nodos)      #marcamos todos los nodos como blancos
    foresta = []                        #inicializamos un arreglo para almacenar la foresta
    for u in nodos:                     #por cada nodo O(n)
        if(blancos[u] == False):            #si no esta marcado como blanco
            arbol = bfs(u,matriz,blancos)   #realizamos un recorrido bfs
            foresta.append(arbol)           #almacenamos el resultado
    return foresta                          #de esta manera tendremos mas de un arbol en foresta si son disconexos

#este metodo calcula el recorrido bfs a partir de un nodo dado, una matriz de todos los nodos y una cola de nodos blancos
def bfs(u, matriz, blancos):
    cola = queue.Queue()                #creamos una cola
    blancos[u] = True                   #marcamos el nodo seleccionado como blanco
    cola.put(u)                         #lo ingresamos a la cola
    pertenecientes = []                 #creamos una lista para ir almacenando nodos recorridos a partir del inicial(arbol resultante)
    
    while (not cola.empty()):           #mientras la cola no este vacia
        actual = cola.get()                 #obtenemos el siguiente de la cola
        pertenecientes.append(actual)       #agregamos el nodo actual a pertenecientes
        if(actual in matriz):               #si el actual esta en la matriz
            for v in matriz.get(actual):    #por cada nodo adyacente al actual
                if(blancos[v]==False):      #si el nodo adyacente no es blanco
                    blancos[v] = True       #lo marcamos como blanco
                    cola.put(v)             #lo añadimos a la cola
    return pertenecientes

def conexo_DS(nodos,arcos):
    listaDS = []
    for nodo in nodos:                                      #O(n)
        a = [DisjointSetHeuristicas.MakeSet(nodo)]          
        listaDS.append(a)
    for arco in arcos:                                      #O(a)
        indu = 0
        indv = 0
        indicesEncontrados = False
        indice = 0
        nodoUencontrado = False
        nodoVencontrado = False
        while ((indice < len(listaDS)) & (indicesEncontrados == False)):    #O(n)
            j = 0
            while (j < len(listaDS[indice])):
                nodo = listaDS[indice][j]
                if (nodo.value == arco.getArco()[0]):
                    indu = indice
                    nodoUencontrado = True
                else:
                    if (nodo.value == arco.getArco()[1]):
                        indv = indice
                        nodoVencontrado = True
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
            for lista in listaDS:                   #O(n)
                l = [nodo.value for nodo in lista]
                lAux.append(l)
    return lAux