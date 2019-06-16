# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:44:49 2019

@author: Martin
"""

import requests
import json
import matrizador
import time
import bfs

class Grafo:
    class Pesado:
        def __init__(self,arcoPeso):
            self.arco = arcoPeso[0]
            self.peso = arcoPeso[1]
            self.grafo = None
            
        def getArco(self):
            return self.arco

    def __init__(self, n, a, cond = False):
        url = "http://cs.uns.edu.ar/~mom/AyC2019/grafo.php?nodos="+str(n)+"&arcos="+str(a)
        if cond:
            url += "&conexo=1"
        r = requests.get(url)
        self.grafo = json.loads(r.text)
       # r_aux = '{"nodos": [0,1,2,3,4],"arcos": [[[0,1],10], [[0,3],30], [[0,2],40], [[1,3],20], [[2,4],50], [[3,4],60]]}'
       # self.grafo = json.loads(r_aux)
        r_aux2 ='{"nodos":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],"arcos":[[[5, 6], 920], [[2, 3], 373], [[9, 0], 639], [[1, 2], 82], [[8, 6], 13], [[0, 1], 331], [[7, 8], 463], [[6, 7], 342], [[8, 9], 499], [[4, 5], 196]]}'
        self.grafo = json.loads(r_aux2)
        self.nodos = self.grafo['nodos']
        self.arcos = [self.Pesado(x) for x in self.grafo['arcos']]

    def getPrimerArco(self):
        return grafo.arcos[0].arco
    def getPesoPrimerArco(self):
        return grafo.arcos[0].peso
    def addNode(self,x):
        self.nodos.append(x)
    def getJsonGrafo(self):
        return self.grafo

#Grafo(nodo,arco,cond = False)

grafo = Grafo(10,10)
#grafo.addNode(5)
#grafo.addNode(6)
#grafo.addNode(7)
start_time = time.time()
g1 = grafo.getJsonGrafo()
m1 = matrizador.grafo_a_Lista_De_Adyacencia(g1)
#m2 = matrizador.grafo_a_Lista_De_Adyacencia_Catedra(grafo)

print("nodos: ")
print(g1["nodos"])
print("-------------------------------------------------")
#print(m1)
#print("-------------------------------------------------")
#print("")
#print(m2)
#print("-------------------------------------------------")
#print("")
#m3 = matrizador.grafo_a_Matriz_de_Adyacencia(grafo,True)
print("Lista adyacencia del grafo")
print(m1)
print("-------------------------------------------------")
print("")

resultado = bfs.bfs_completo(m1,grafo.nodos)
print("Foresta de arboles (1a)")
print(resultado)
print("-------------------------------------------------")
print("")

resultado = bfs.conexo_DS(grafo.nodos, grafo.arcos)
print("Componentes conexos con Disjoint Set (1b)")
print(resultado)
print("-------------------------------------------------")
print("")

print("Grafo conexo para probrar 2b) 1)")
#grafo = Grafo(10,10,True)
g1 = grafo.getJsonGrafo()
m1 = matrizador.grafo_a_Lista_De_Adyacencia(g1)
print("nodos: ")
print(g1["nodos"])
print("arcos: ")
print(g1["arcos"])
print("-------------------------------------------------")
print("Lista adyacencia del grafo")
print(m1)
print("-------------------------------------------------")

bfs.kruskal_2b_1(grafo.nodos, g1["arcos"])

print("--- %s segundos ---" % (time.time()- start_time))
"""
Generar varios grafos. 

Realizar anÃ¡lisis empÃ­rico mediante timestamps.
"""