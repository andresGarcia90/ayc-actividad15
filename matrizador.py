import json
import sys

#Es posible representar un grafo de dos maneras: con una matriz de adyacencia util para grafos densos
#o con un diccionario (lista de adyacencia) para grafos poco densos

#Para este metodo hay que tener en cuenta que le web service provisto por la catedra genera un conjunto de arcos de la manera
#{arcos:[[[u,v],peso],...]} --- es decir el valor de la clave arcos es una lista de pares cuyo primer componente es un par [u,v] y el segundo el peso correspondiente a ese par
def grafo_a_Lista_De_Adyacencia(grafo):
    matrizAdy = dict()                                      #O(1)
    for arc in grafo["arcos"]:                              #O(arcos)
        #De ida
        if (matrizAdy.get(arc[0][0]) == None):              #O(1)
            matrizAdy.update({arc[0][0]:[arc[0][1]]})         #si no existen arcos desde u agrego la nueva entrada u y genero una lista con un nuevo componente v
        else:
            matrizAdy.get(arc[0][0]).append(arc[0][1])        #si existe la entrada, obtengo la lista correspondiente y le agrego v
        #De vuelta porque son no dirigidos
        if (matrizAdy.get(arc[0][1]) == None):             
            matrizAdy.update({arc[0][1]:[arc[0][0]]})         
        else:
            matrizAdy.get(arc[0][1]).append(arc[0][0])
    return matrizAdy

def grafo_a_Lista_De_Adyacencia_Catedra(grafo):
    matrizAdy = dict()                                      #O(1)
    for arc in grafo.arcos:                                 #O(arcos)
        #De ida
        if (matrizAdy.get(arc.arco[0]) == None):            #O(1)
            matrizAdy.update({arc.arco[0]:[arc.arco[1]]})         #si no existen arcos desde u agrego la nueva entrada u y genero una lista con un nuevo componente v
        else:
            matrizAdy.get(arc.arco[0]).append(arc.arco[1])        #si existe la entrada, obtengo la lista correspondiente y le agrego v
        #De vuelta porque son no dirigidos
        if (matrizAdy.get(arc.arco[1]) == None):             
            matrizAdy.update({arc.arco[1]:[arc.arco[0]]})         
        else:
            matrizAdy.get(arc.arco[1]).append(arc.arco[0])
    return matrizAdy

def grafo_a_Matriz_de_Adyacencia(grafo, peso = False):
    #primero genero la matriz de n*n donde n es la cantidad de nodos
    n = len(grafo.nodos)
    matrizAdy = [[0] * n for i in range(n)]
    if (peso == False):
        for arc in grafo.arcos:
            matrizAdy[arc.arco[0]][arc.arco[1]] = 1
            matrizAdy[arc.arco[1]][arc.arco[0]] = 1
    else:
        for arc in grafo.arcos:
            matrizAdy[arc.arco[0]][arc.arco[1]] = arc.peso
            matrizAdy[arc.arco[1]][arc.arco[0]] = arc.peso
    return matrizAdy