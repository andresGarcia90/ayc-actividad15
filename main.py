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
import Kruskal
import Tabla

class Grafo:
    class Pesado:
        def __init__(self,arcoPeso):
            self.arco = arcoPeso[0]
            self.peso = arcoPeso[1]
            self.grafo = None
            self.tabla = None
            
        def getArco(self):
            return self.arco

    def __init__(self, n, a, cond = False):
        url = "http://cs.uns.edu.ar/~mom/AyC2019/grafo.php?nodos="+str(n)+"&arcos="+str(a)
        if cond:
            url += "&conexo=1"
        r = requests.get(url)
        self.grafo = json.loads(r.text)
        #r_aux = '{"nodos":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],"arcos":[[[16, 14], 625], [[19, 0], 666], [[2, 3], 235], [[17, 8], 84], [[18, 19], 678], [[14, 7], 540], [[1, 2], 349], [[15, 8], 304], [[14, 15], 588], [[13, 7], 282], [[5, 6], 413], [[6, 7], 481], [[13, 14], 410], [[0, 1], 151], [[17, 18], 220], [[8, 9], 428], [[9, 10], 767], [[10, 11], 654], [[15, 16], 232], [[11, 12], 736], [[4, 14], 979], [[3, 4], 250], [[19, 4], 375], [[17, 4], 440], [[7, 8], 997], [[4, 5], 654], [[5, 2], 530], [[14, 1], 518], [[12, 13], 509], [[8, 10], 381]]}'
        #self.grafo = json.loads(r_aux)
        self.nodos = self.grafo['nodos']
        self.arcos = [self.Pesado(x) for x in self.grafo['arcos']]

    def getPrimerArco(self):
        return self.arcos[0].arco
    def getPesoPrimerArco(self):
        return self.arcos[0].peso
    def addNode(self,x):
        self.nodos.append(x)
    def getJsonGrafo(self):
        return self.grafo

tabla = Tabla.Tabla()
#grafo = Grafo(10,10)
#grafo.addNode(5)
#grafo.addNode(6)
#grafo.addNode(7)
#start_time = time.time()
#g1 = grafo.getJsonGrafo()
#m1 = matrizador.grafo_a_Lista_De_Adyacencia(g1)
#m2 = matrizador.grafo_a_Lista_De_Adyacencia_Catedra(grafo)

#print("nodos: ")
#print(g1["nodos"])
#print("-------------------------------------------------")
#print(m1)
#print("-------------------------------------------------")
#print("")
#print(m2)
#print("-------------------------------------------------")
#print("")
#m3 = matrizador.grafo_a_Matriz_de_Adyacencia(grafo,True)
# print("Lista adyacencia del grafo")
# print(m1)
# print("-------------------------------------------------")
# print("")

# resultado = bfs.bfs_completo(m1,grafo.nodos)
# print("Foresta de arboles (1a)")
# print(resultado)
# print("-------------------------------------------------")
# print("")

# resultado = bfs.conexo_DS(grafo.nodos, grafo.arcos)
# print("Componentes conexos con Disjoint Set (1b)")
# print(resultado)
# print("-------------------------------------------------")
# print("")

# print("Grafo conexo para probrar 2b) 1)")
# grafo = Grafo(20,30,True)
# g1 = grafo.getJsonGrafo()
# m1 = matrizador.grafo_a_Lista_De_Adyacencia(g1)
# print("nodos: ")
# print(g1["nodos"])
# print("arcos: ")
# print(g1["arcos"])
# print("-------------------------------------------------")
# print("Lista adyacencia del grafo")
# print(m1)
# print("-------------------------------------------------")

# arcos = g1["arcos"]
# arbolMinimal = Kruskal.kruskal_2b_1(m1, arcos)
# print("Arbol minimal utilizando Disjoint Set con Heurísticas:")
# arbolMinimal.preorden(arbolMinimal.raiz,0)

# print("-------------------------------------------------")
# print("Arbol minimal utilizando un Heap invertido:")
# arbol_minimal_heap = Kruskal.kruskal_con_heap(grafo.nodos, arcos)
# arbol_minimal_heap.preorden(arbol_minimal_heap.raiz, 0)

# print("-------------------------------------------------")
# print("Arbol minimal utilizando un conjunto de arcos ordenados por su peso:")
# arbol_minimal_heap = Kruskal.kruskal_con_conjunto(grafo.nodos, arcos)
# arbol_minimal_heap.preorden(arbol_minimal_heap.raiz, 0)
#print("--- %s segundos ---" % (time.time()- start_time))
"""
Generar varios grafos. 

Realizar anÃ¡lisis empÃ­rico mediante timestamps.
"""


grafo_1 = Grafo(10,20)
grafo_2 = Grafo(150,1000)
grafo_3 = Grafo(200,3000)
grafo_4 = Grafo(300,10000)
grafo_5 = Grafo(400,1000)
grafo_6 = Grafo(500,10000)
indice = 1

grafos = [grafo_1,grafo_2,grafo_3,grafo_4,grafo_5,grafo_6]
resultados = []
for g in grafos:
    g1 = g.getJsonGrafo()
    m1 = matrizador.grafo_a_Lista_De_Adyacencia(g1)
    print("Ejecutando comprobaciones para ver si un grafo no-dirigido y pesado es conexo para el grafo %s de %s nodos con %s arcos:" %(indice,len(g.nodos),len(g.arcos)))
    start_time_conexo_bfs = time.time() 
    resultado1 = bfs.bfs_completo(m1,g.nodos)
    end_time_conexo_bfs = time.time()
    print("Comprobando con BFS..")
    #print(resultado1)
    start_time_conexo_ds = time.time()
    resultado2 = bfs.conexo_DS(g.nodos, g.arcos)
    end_time_conexo_ds = time.time()
    print("Comprobando con Disjoint Set..")
    #print(resultado2)
    if ((len(resultado1) == 1) & (len(resultado2) == 1)):
        flag = "sí"
    else:
        if (((len(resultado1) == 1) & (len(resultado2) != 1)) | ((len(resultado1) != 1) & (len(resultado2) == 1))):
            flag = "REVISAR"
        else:
            flag = "no"
    tabla.insertar_tabla1(indice,len(g.nodos),len(g.arcos),flag,"{0:.10f}".format(end_time_conexo_bfs-start_time_conexo_bfs),"{0:.10f}".format(end_time_conexo_ds-start_time_conexo_ds))
    indice = indice + 1
print("")
print("")
print("                                            TABLA DE RESULTADOS")
print("")
tabla.imprimir_tabla1()

print("")
print("-------------------------------------------------")
grafo_1 = Grafo(10,20,True)
grafo_2 = Grafo(150,1000,True)
grafo_3 = Grafo(200,3000,True)
grafo_4 = Grafo(300,10000,True)
grafo_5 = Grafo(400,25000,True)
grafo_6 = Grafo(500,50000,True)
indice = 1

grafos = [grafo_1,grafo_2,grafo_3,grafo_4,grafo_5,grafo_6]
resultados = []
for g in grafos:
    g1 = g.getJsonGrafo()
    m1 = matrizador.grafo_a_Lista_De_Adyacencia(g1)
    print("Ejecutando algoritmo de Kruskal para el grafo %s de %s nodos con %s arcos:" %(indice,len(g.nodos),len(g.arcos)))
    arcos = g1["arcos"]
    print("Obteniendo árbol minimal Disjoint Set con Heurísticas..")
    start_time_dsch = time.time()   
    arbol_minimal_DS_con_H = Kruskal.kruskal_2b_1(m1, arcos)
    end_time_dsch = time.time()
    #arbol_minimal_DS_con_H.preorden(arbol_minimal_DS_con_H.raiz,0)

    print("Obteniendo árbol minimal Disjoint Set sin Heurísticas..")
    start_time_dssh = time.time()   
 !!!!!   arbol_minimal_DS_sin_H = Kruskal.kruskal_2b_1(m1, arcos)
    end_time_dssh = time.time()
    #arbol_minimal_DS_sin_H.preorden(arbol_minimal_DS_sin_H.raiz,0)

    print("Obteniendo árbol minimal utilizando un Heap invertido..")
    start_time_minHeap = time.time()   
    arbol_minimal_heap = Kruskal.kruskal_con_heap(g.nodos, arcos)
    end_time_minHeap = time.time()
    #arbol_minimal_heap.preorden(arbol_minimal_heap.raiz, 0)

    print("Obteniendo árbol minimal utilizando un conjunto de arcos ordenados por su peso..")
    start_time_conjunto = time.time()   
    arbol_minimal_heap = Kruskal.kruskal_con_conjunto(g.nodos, arcos)
    end_time_conjunto = time.time()
    #arbol_minimal_heap.preorden(arbol_minimal_heap.raiz, 0)
    

    tabla.insertar_tabla2(indice, len(g.nodos),len(g.arcos),"sí","{0:.10f}".format(end_time_conjunto-start_time_conjunto), "{0:.10f}".format(end_time_minHeap-start_time_minHeap),"{0:.10f}".format(end_time_dsch-start_time_dsch),"{0:.10f}".format(00000))
    indice = indice + 1
print("")
print("")
print("                                            TABLA DE RESULTADOS")
print("")
tabla.imprimir_tabla2()