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
grafo = Grafo(20,30,True)
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

arcos = g1["arcos"]
arbolMinimal = bfs.kruskal_2b_1(m1, arcos)
print("Arbol minimal")
arbolMinimal.preorden(arbolMinimal.raiz,0)

print("--- %s segundos ---" % (time.time()- start_time))
"""
Generar varios grafos. 

Realizar anÃ¡lisis empÃ­rico mediante timestamps.
"""