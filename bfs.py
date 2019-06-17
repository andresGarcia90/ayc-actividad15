#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
#To make the code more efficient, you can use the deque object from the collections module instead of a list, 
# for implementing queue. This way you can use the popleft() method instead of the  pop(0) built-in function on queue. 
# This will result in a quicker code as popleft()has a time complexity of O(1) while pop(0) has O(n).

from collections import deque
import queue
import DisjointSet
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
        a = [DisjointSet.MakeSet(nodo)]
        listaDS.append(a)
    #print("listaDS antes de find set ",listaDS)
    #lAux = []
    #for lista in listaDS:
       # l.append([nodo.value])
       # l = [nodo.value for nodo in lista]
       # lAux.append(l)
    #print ("listaDS antes de findSet ",lAux)
    for arco in arcos:
        #print("antes de findset")
        #print("arco u ",arco.getArco()[0])
        #print("arco v ",arco.getArco()[1])
        cont = 0
        for lista in listaDS:
            for nodo in lista:
                #print("nodo en lista ",nodo.value)
                if (nodo.value == arco.getArco()[0]):
                    #print("JEJEJEJE, encontre u")
                    indu = cont
                else:
                    if (nodo.value == arco.getArco()[1]):
                        #print("JEJEJEJE, encontre v")
                        indv = cont
            cont = cont + 1
        #print("indice nodo u en listaDS",indu)
        #print("indice nodo v en listaDS",indv)
        #print("nodo u ",listaDS[indu])
        #print("nodo v ",listaDS[indv])
        representante_u = DisjointSet.findSet(listaDS[indu][0])
        representante_v = DisjointSet.findSet(listaDS[indv][0])
        #print("despues de findSet")
        #print("nodo u representante",u)
        #print("nodo v representante",v)
        #print("u v ",u,v)
        if (representante_u != representante_v):
            DisjointSet.joinSet(representante_u,representante_v)
            res2 = []
            for nodo in listaDS[indu]:
                res2.append(nodo)
            for nodo in listaDS[indv]:
                res2.append(nodo)
            #print(res2)
            if (indu < indv):
                listaDS.remove(listaDS[indu])
                listaDS.remove(listaDS[indv-1])
            else:
                listaDS.remove(listaDS[indv])
                listaDS.remove(listaDS[indu-1])
            listaDS.append(res2)
            #print("listaDS despues de append res de find set ",listaDS)
            lAux = []
            for lista in listaDS:
                l = [nodo.value for nodo in lista]
                lAux.append(l)
            #print ("listaDS despues de append res de findSet ",lAux)
    return lAux