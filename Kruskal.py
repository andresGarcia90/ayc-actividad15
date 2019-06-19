import Arbol
# import DisjointSet
import disjoinSet_SinHeuristicas
import Heap
import DisjointSetHeuristicas


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

def buscarNodo(listaDS, elemento):
    for l in listaDS:
        if l.value == elemento:
            return l

#Busca y retorna el arbol que tiene al nodo v o al nodo u            
def buscarNodosArboles(t_list,u):
    for arbol in t_list:
        if arbol.obtenerNodo(u.value):
            return arbol
    return None 

def buscarNodosArboles_sin_nodo(t_list,u):
    for arbol in t_list:
        if arbol.obtenerNodo(u):
            return arbol
    return None
        

def kruskal_con_conjunto(nodos,arcos):
    arcosOrdenados=[]
    #inserto arcos en una lista ordenada
    for arco in arcos:
        agregarElementoLista(arcosOrdenados, arco)
    #creo una lista de arboles
    t_list = []
    
    i = 0

    #creo los conjuntos disjuntos de nodos
    listaDS = []
    for nodo in nodos:
        a = [DisjointSetHeuristicas.MakeSet(nodo)]
        listaDS.append(a)

    listaDS_aux = listaDS.copy()

    i = 0
    while ( len(listaDS) > 1 and len(arcosOrdenados) > 0):
        arco = obtenerPrimero(arcosOrdenados)
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
                if (nodo.value == arco[0][0]):
                    indu = indice
                    nodoUencontrado = False
                else:
                    if (nodo.value == arco[0][1]):
                        indv = indice
                        nodoVencontrado = False
                j = j+1
                indicesEncontrados = nodoUencontrado & nodoVencontrado
            indice = indice + 1
        u = listaDS[indu][0]
        v = listaDS[indv][0]
       
        u_conjunto = DisjointSetHeuristicas.findSet(u)
        v_conjunto = DisjointSetHeuristicas.findSet(v)
        if u_conjunto != v_conjunto:
            DisjointSetHeuristicas.union(u,v)
            peso = arco[1]
            #caso de la raiz
            if (len(t_list) == 0):
                t = Arbol.arbol()
                raiz = t.insertarRaiz(u.value)
                t.insertar(raiz,u.value,v.value,peso)
                i=i+2
                t_list.append(t)
            #caso en que se inserto un elemento
            else:
                #busco si en la lista hay un arbol que contiene a los nodos.
                arbol_nuevo_u = buscarNodosArboles(t_list,u)
                arbol_nuevo_v = buscarNodosArboles(t_list,v)
                #Encontre un arbol de la lista que tiene al nodo
                if arbol_nuevo_u != None and arbol_nuevo_v != None:
                    nodo_aux_u = arbol_nuevo_u.obtenerNodo(u.value)
                    nodo_aux_v = arbol_nuevo_v.obtenerNodo(v.value)
                    #combinamos el arbol
                    arbol_nuevo_u.combinarArbol(nodo_aux_u.dato,arbol_nuevo_v,nodo_aux_v.dato,peso)
                    i = i+1
                    t_list.remove(arbol_nuevo_v)
                else:
                    if(arbol_nuevo_u != None):
                        nodo_aux_u = arbol_nuevo_u.obtenerNodo(u.value)
                        arbol_nuevo_u.insertar(arbol_nuevo_u.obtenerRaiz(), nodo_aux_u.dato, v.value, peso)
                        i = i+1
                        #print("nuevo Arbol",arbol_nuevo_u)
                    else:
                        if arbol_nuevo_v != None:
                            nodo_aux_v = arbol_nuevo_v.obtenerNodo(v.value)
                            arbol_nuevo_v.insertar(arbol_nuevo_v.obtenerRaiz(), nodo_aux_v.dato, u.value, peso)
                            i = i+1
                            #print("nuevo Arbol",arbol_nuevo_v)
                        else:
                            #Caso en que no encontre arbol
                            t = Arbol.arbol()
                            raiz = t.insertarRaiz(u.value)
                            t.insertar(raiz,u.value,v.value,peso)
                            i=i+2
                            t_list.append(t)

    return t_list[0]

    

def kruskal_con_heap(nodos,arcos):
    h = Heap.BinHeap()
    h.buildHeap(arcos)
    #creo una lista de arboles
    t_list = []
    
    i = 0

    #creo los conjuntos disjuntos de nodos
    listaDS = []
    for nodo in nodos:
        a = [DisjointSetHeuristicas.MakeSet(nodo)]
        listaDS.append(a)

    listaDS_aux = listaDS.copy()

    i = 0
    while ( h.size() > 0 and len(listaDS) > 1):
        arco = h.delMin()
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
                if (nodo.value == arco[0][0]):
                    indu = indice
                    nodoUencontrado = False
                else:
                    if (nodo.value == arco[0][1]):
                        indv = indice
                        nodoVencontrado = False
                j = j+1
                indicesEncontrados = nodoUencontrado & nodoVencontrado
            indice = indice + 1
        u = listaDS[indu][0]
        v = listaDS[indv][0]

        u_conjunto = DisjointSetHeuristicas.findSet(u)
        v_conjunto = DisjointSetHeuristicas.findSet(v)
        if u_conjunto != v_conjunto:
            DisjointSetHeuristicas.union(u,v)
            peso = arco[1]
            #caso de la raiz
            if (len(t_list) == 0):
                t = Arbol.arbol()
                raiz = t.insertarRaiz(u.value)
                t.insertar(raiz,u.value,v.value,peso)
                i=i+2
                t_list.append(t)
            #caso en que se inserto un elemento
            else:
                #busco si en la lista hay un arbol que contiene a los nodos.
                arbol_nuevo_u = buscarNodosArboles(t_list,u)
                arbol_nuevo_v = buscarNodosArboles(t_list,v)
                #Encontre un arbol de la lista que tiene al nodo
                if arbol_nuevo_u != None and arbol_nuevo_v != None:
                    nodo_aux_u = arbol_nuevo_u.obtenerNodo(u.value)
                    nodo_aux_v = arbol_nuevo_v.obtenerNodo(v.value)
                    #combinamos el arbol
                    arbol_nuevo_u.combinarArbol(nodo_aux_u.dato,arbol_nuevo_v,nodo_aux_v.dato,peso)
                    i = i+1
                    t_list.remove(arbol_nuevo_v)
                else:
                    if(arbol_nuevo_u != None):
                        nodo_aux_u = arbol_nuevo_u.obtenerNodo(u.value)
                        arbol_nuevo_u.insertar(arbol_nuevo_u.obtenerRaiz(), nodo_aux_u.dato, v.value, peso)
                        i = i+1
                        #print("nuevo Arbol",arbol_nuevo_u)
                    else:
                        if arbol_nuevo_v != None:
                            nodo_aux_v = arbol_nuevo_v.obtenerNodo(v.value)
                            arbol_nuevo_v.insertar(arbol_nuevo_v.obtenerRaiz(), nodo_aux_v.dato, u.value, peso)
                            i = i+1
                            #print("nuevo Arbol",arbol_nuevo_v)
                        else:
                            #Caso en que no encontre arbol
                            t = Arbol.arbol()
                            raiz = t.insertarRaiz(u.value)
                            t.insertar(raiz,u.value,v.value,peso)
                            i=i+2
                            t_list.append(t)

    return t_list[0]






    
                

def kruskal_2b_1(listaAdyacencia,arcos):
    listaDS = []
    arcosAux = arcos.copy()
    porIngresar = list(range(len(listaAdyacencia)))
    for nodo in porIngresar:
        a = [DisjointSetHeuristicas.MakeSet(nodo)]
        listaDS.append(a)
    arcosAux.sort(key=lambda tupla: tupla[1])
    #print("ordenados por peso ",arcosAux)
    tree = Arbol.arbol()
    listaTree = []
    while(len(arcosAux) != 0 and len(listaDS) > 1):
        arista = arcosAux[0][0]
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
                if (nodo.value == arista[0]):
                    indu = indice
                    nodoUencontrado = False
                else:
                    if (nodo.value == arista[1]):
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
            peso = arcosAux[0][1]
            if(tree.size == 0):
               raiz = tree.insertarRaiz(arista[0])
               tree.insertar(raiz,arista[0],arista[1],peso)
               listaTree.append(tree)
               porIngresar.remove(arista[0])
               porIngresar.remove(arista[1])
            else:
                if ((arista[0] in porIngresar) & (arista[1] in porIngresar)):
                    #arco = [u,v], u y v no fueron insertados en el árbol
                    tree = Arbol.arbol()
                    raiz = tree.insertarRaiz(arista[0])
                    tree.insertar(raiz,arista[0],arista[1],peso)
                    listaTree.append(tree)
                    porIngresar.remove(arista[0])
                    porIngresar.remove(arista[1])
                else: 
                    if ((arista[0] in porIngresar) & (arista[1] not in porIngresar)):
                        #arco = [u,v], u no fue insertado en el árbol, v sí
                        arb = buscarNodosArboles(listaTree,representante_v)
                        arb.insertar(arb.raiz,arista[1],arista[0],peso)
                        porIngresar.remove(arista[0])
                    else:
                        if ((arista[0] not in porIngresar) & (arista[1] in porIngresar)):
                            #arco = [u,v], v no fue insertado en el árbol, u sí
                            arb = buscarNodosArboles(listaTree,representante_u)
                            arb.insertar(arb.raiz,arista[0],arista[1],peso)
                            porIngresar.remove(arista[1])
                        else:
                            #arco = [u,v], u y v fueron insertados en el árbol
                            arb1 = buscarNodosArboles(listaTree,representante_u)
                            arb2 = buscarNodosArboles(listaTree,representante_v)
                            if((arb1.size) >= (arb2.size)):
                                listaTree.remove(arb2)
                                arb1.combinarArbol(arista[0],arb2,arista[1],peso)
                            else:
                                listaTree.remove(arb1)
                                arb2.combinarArbol(arista[1],arb1,arista[0],peso)
        arcosAux.remove(arcosAux[0])
    return listaTree[0]



    
def kruskal_2b_2(listaAdyacencia,arcos):
    listaDS = []
    arcosAux = arcos.copy()
    porIngresar = list(range(len(listaAdyacencia)))
    for nodo in porIngresar:
        a = disjoinSet_SinHeuristicas.MakeSet_SinHeuristica(nodo)
        listaDS.append(a)
    arcosAux.sort(key=lambda tupla: tupla[1])
    #print("ordenados por peso ",arcosAux)
    tree = Arbol.arbol()
    listaTree = []
    while(len(arcosAux) != 0 and len(listaDS) > 1):
        arista = arcosAux[0][0]
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
                if (nodo == arista[0]):
                    indu = indice
                    nodoUencontrado = False
                else:
                    if (nodo == arista[1]):
                        indv = indice
                        nodoVencontrado = False
                j = j+1
                indicesEncontrados = nodoUencontrado & nodoVencontrado
            indice = indice + 1
        representante_u = disjoinSet_SinHeuristicas.findSet_SinHeuristica(listaDS[indu][0],listaDS)
        representante_v = disjoinSet_SinHeuristicas.findSet_SinHeuristica(listaDS[indv][0],listaDS)
        if (representante_u != representante_v):
            listaDS = disjoinSet_SinHeuristicas.union_SinHeuristica(representante_u,representante_v,listaDS)
            peso = arcosAux[0][1]
            if(tree.size == 0):
               raiz = tree.insertarRaiz(arista[0])
               tree.insertar(raiz,arista[0],arista[1],peso)
               listaTree.append(tree)
               porIngresar.remove(arista[0])
               porIngresar.remove(arista[1])
            else:
                if ((arista[0] in porIngresar) & (arista[1] in porIngresar)):
                    tree = Arbol.arbol()
                    raiz = tree.insertarRaiz(arista[0])
                    tree.insertar(raiz,arista[0],arista[1],peso)
                    listaTree.append(tree)
                    porIngresar.remove(arista[0])
                    porIngresar.remove(arista[1])
                else: 
                    if ((arista[0] in porIngresar) & (arista[1] not in porIngresar)):
                        arb = buscarNodosArboles_sin_nodo(listaTree,representante_v)
                        arb.insertar(arb.raiz,arista[1],arista[0],peso)
                        porIngresar.remove(arista[0])
                    else:
                        if ((arista[0] not in porIngresar) & (arista[1] in porIngresar)):
                            arb = buscarNodosArboles_sin_nodo(listaTree,representante_u)
                            arb.insertar(arb.raiz,arista[0],arista[1],peso)
                            porIngresar.remove(arista[1])
                        else:
                            arb1 = buscarNodosArboles_sin_nodo(listaTree,representante_u)
                            arb2 = buscarNodosArboles_sin_nodo(listaTree,representante_v)
                            if((arb1.size) >= (arb2.size)):
                                listaTree.remove(arb2)
                                arb1.combinarArbol(arista[0],arb2,arista[1],peso)
                            else:
                                listaTree.remove(arb1)
                                arb2.combinarArbol(arista[1],arb1,arista[0],peso)
        arcosAux.remove(arcosAux[0])
    return listaTree[0]
