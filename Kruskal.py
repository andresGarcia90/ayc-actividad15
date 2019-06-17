import Arbol
import DisjointSet

def agregarElementoLista(lista, elemento):
    tope = len(lista)
    i = 0
    inserte = False
    if(tope == i):
        lista.append(elemento)
        inserte = True

    while (inserte != True and i < tope):
        if(lista[i][1] > elemento[1]):
            lista.insert(i,elemento)
            inserte = True
        i= i+1
    #quiere decir que el elemento va al final
    if(inserte == False):
        lista.append(elemento)

    return lista

def obtenerPrimero(lista):
    elemento = lista.pop(0)
    return elemento

def buscarNodo(lista, elemento):
    for l in lista:
        if l.value == elemento:
            return l


def kruskal_con_conjunto(nodos,arcos):
    arcosOrdenados=[]
    #inserto arcos en una lista ordenada
    for arco in arcos:
        agregarElementoLista(arcosOrdenados, arco)
    #creo una lista de arboles
    t_list = []
    #Obtengo el total de nodos
    nodos_len = len(nodos)
    
    i = 0

    #creo los conjuntos disjuntos de nodos
    listaDS = []
    for nodo in nodos:
        a = DisjointSet.MakeSet(nodos[i])
        i=i+1
        listaDS.append(a)

    i = 0
    while (i<nodos_len):
        arco = obtenerPrimero(arcosOrdenados)
        print("asd", arco[0][0], arco[0][1])
        u = buscarNodo(listaDS,arco[0][0])
        v = buscarNodo(listaDS,arco[0][1]) 
        u_conjunto = DisjointSet.findSet(u)
        v_conjunto = DisjointSet.findSet(v)
        if u_conjunto != v_conjunto:
            DisjointSet.joinSet(u_conjunto,u_conjunto)
            #caso de la raiz
            if (len(t_list) == 0):
                t = Arbol.arbol()
                aux = t.insertarRaiz(u)
                print("raiz ", aux.dato)
                print("obtener raiz", t.obtenerRaiz().dato)
                t.insertar(t.obtenerRaiz,u.dato,v.dato,1)
                i=i+2
                t_list.append(t)
            #caso en que se inserto un elemento
            else:
                #busco si en la lista hay un arbol que contiene a los nodos.
                arbol_nuevo = self.buscarNodosArboles(t_list,u,v)
                #Encontre un arbol de la lista que tiene al nodo
                if(arbol_nuevo != None):
                    nodo_aux_u = arbol_nuevo.obtenerNodo(u)
                    nodo_aux_v = arbol_nuevo.obtenerNodo(v)
                    if u != None:
                        arbol_nuevo.insertar(arbol_nuevo.obtenerRaiz(), u, v.dato, 1)
                    else:
                        arbol_nuevo.insertar(arbol_nuevo.obtenerRaiz(), v, u.dato, 1)
                        
                else:
                    #Caso en que no encontre arbol
                    t = Arbol.arbol()
                    aux = t.insertarRaiz(u)
                    t.insertar(t.obtenerRaiz,u,v)
                    i=i+2
                    t_list.append(t)
    

    
nodos = [0,1,2,3,4]
arcos = [[[0,1],10], [[0,3],30], [[0,2],40], [[1,3],20], [[2,4],50], [[3,4],60]]



kruskal_con_conjunto(nodos, arcos)