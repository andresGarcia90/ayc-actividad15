import Arbol
import DisjointSet
import Heap

#algo mas para probar


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

    listaDS_aux = listaDS.copy()

    i = 0
    while ( len(arcosOrdenados) > 0):
        arco = obtenerPrimero(arcosOrdenados)
        print("arco", arco[0][0], arco[0][1])
        u = buscarNodo(listaDS_aux,arco[0][0])
        v = buscarNodo(listaDS_aux,arco[0][1]) 
        u_conjunto = DisjointSet.findSet(u)
        v_conjunto = DisjointSet.findSet(v)
        if u_conjunto != v_conjunto:
            uv_conjunto = DisjointSet.joinSet(u_conjunto,v_conjunto)
            #caso de la raiz
            if (len(t_list) == 0):
                t = Arbol.arbol()
                aux = t.insertarRaiz(u.value)
                t.insertar(t.obtenerRaiz(),u.value,v.value,1)
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
                    arbol_nuevo_u.combinarArbol(nodo_aux_u.dato,arbol_nuevo_v,nodo_aux_v.dato,1)
                    i = i+1
                    t_list.remove(arbol_nuevo_v)
                else:
                    if(arbol_nuevo_u != None):
                        nodo_aux_u = arbol_nuevo_u.obtenerNodo(u.value)
                        arbol_nuevo_u.insertar(arbol_nuevo_u.obtenerRaiz(), nodo_aux_u.dato, v.value, 1)
                        i = i+1
                        print("nuevo Arbol",arbol_nuevo_u)
                    else:
                        if arbol_nuevo_v != None:
                            nodo_aux_v = arbol_nuevo_v.obtenerNodo(v.value)
                            arbol_nuevo_v.insertar(arbol_nuevo_v.obtenerRaiz(), nodo_aux_v.dato, u.value, 1)
                            i = i+1
                            print("nuevo Arbol",arbol_nuevo_v)
                        else:
                            #Caso en que no encontre arbol
                            t = Arbol.arbol()
                            aux = t.insertarRaiz(u.value)
                            t.insertar(t.obtenerRaiz(),u.value,v.value,1)
                            i=i+2
                            t_list.append(t)
            listaDS.append(uv_conjunto)
            listaDS.remove(v_conjunto)
            listaDS.remove(u_conjunto)

    print("tlist", len(t_list))
    print("retorno esto?",t_list[0].preorden(t_list[0].obtenerRaiz(),0))

    

def kruskal_con_heap(nodos,arcos):
    h = Heap.BinHeap()
    h.buildHeap(arcos)
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

    listaDS_aux = listaDS.copy()

    i = 0
    while ( h.size() > 0):
        arco = h.delMin()
        print("arco", arco[0][0], arco[0][1])
        u = buscarNodo(listaDS_aux,arco[0][0])
        v = buscarNodo(listaDS_aux,arco[0][1]) 
        u_conjunto = DisjointSet.findSet(u)
        v_conjunto = DisjointSet.findSet(v)
        if u_conjunto != v_conjunto:
            uv_conjunto = DisjointSet.joinSet(u_conjunto,v_conjunto)
            #caso de la raiz
            if (len(t_list) == 0):
                t = Arbol.arbol()
                aux = t.insertarRaiz(u.value)
                t.insertar(t.obtenerRaiz(),u.value,v.value,1)
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
                    arbol_nuevo_u.combinarArbol(nodo_aux_u.dato,arbol_nuevo_v,nodo_aux_v.dato,1)
                    i = i+1
                    t_list.remove(arbol_nuevo_v)
                else:
                    if(arbol_nuevo_u != None):
                        nodo_aux_u = arbol_nuevo_u.obtenerNodo(u.value)
                        arbol_nuevo_u.insertar(arbol_nuevo_u.obtenerRaiz(), nodo_aux_u.dato, v.value, 1)
                        i = i+1
                        print("nuevo Arbol",arbol_nuevo_u)
                    else:
                        if arbol_nuevo_v != None:
                            nodo_aux_v = arbol_nuevo_v.obtenerNodo(v.value)
                            arbol_nuevo_v.insertar(arbol_nuevo_v.obtenerRaiz(), nodo_aux_v.dato, u.value, 1)
                            i = i+1
                            print("nuevo Arbol",arbol_nuevo_v)
                        else:
                            #Caso en que no encontre arbol
                            t = Arbol.arbol()
                            aux = t.insertarRaiz(u.value)
                            t.insertar(t.obtenerRaiz(),u.value,v.value,1)
                            i=i+2
                            t_list.append(t)
            listaDS.append(uv_conjunto)
            listaDS.remove(v_conjunto)
            listaDS.remove(u_conjunto)

    print("tlist", len(t_list))
    print("retorno esto?",t_list[0].preorden(t_list[0].obtenerRaiz(),0))







    
                

def kruskal_2b_1(listaAdyacencia,arcos):
    listaDS = []
    arcosAux = arcos.copy()
    ingresar = list(range(len(listaAdyacencia)))
    #print("ing",ingresar)
    for nodo in ingresar:
        a = [DisjointSet.MakeSet(nodo)]
        listaDS.append(a)
    arcosAux.sort(key=lambda tupla: tupla[1])
    #print("ordenados por peso ",arcosAux)
    tree = Arbol.arbol()
    listaTree = []
    # len(ingresar)!=0 and listaTree != 1
    while(len(arcosAux) != 0):
        arista = arcosAux[0][0]
        #print("arista_POSTA ", arista)
        cont = 0
        indu = 0
        indv = 0
        for lista in listaDS:
            for nodo in lista:
                if (nodo.value == arista[0]):
                    indu = cont
                else:
                    if (nodo.value == arista[1]):
                        indv = cont
            cont = cont + 1
        representante_u = DisjointSet.findSet(listaDS[indu][0])
        representante_v = DisjointSet.findSet(listaDS[indv][0])
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
            if(tree.size == 0):
               raiz = tree.insertarRaiz(arista[0])
               peso = arcosAux[0][1]
               tree.insertar(raiz,arista[0],arista[1],peso)
               listaTree.append(tree)
               ingresar.remove(arista[0])
               ingresar.remove(arista[1])
               #print("ingresar ",ingresar)
            else:
                #print("OJO")
                if ((arista[0] in ingresar) & (arista[1] in ingresar)):
                    #print("CASO 0")
                    tree = Arbol.arbol()
                    raiz = tree.insertarRaiz(arista[0])
                    peso = arcosAux[0][1]
                    tree.insertar(raiz,arista[0],arista[1],peso)
                    listaTree.append(tree)
                    ingresar.remove(arista[0])
                    ingresar.remove(arista[1])
                    #print("ingresar ",ingresar)
                    #print("termina caso 0 t: ",len(listaTree))
                else: 
                    if ((arista[0] in ingresar) & (arista[1] not in ingresar)):
                        #print("CASO 1")
                        for arb in listaTree:
                            listaPre = arb.preorden2(arb.raiz)
                            if arista[1] in listaPre:
                                peso = arcosAux[0][1]
                                arb.insertar(arb.raiz,arista[1],arista[0],peso)
                                #print("ingresar ",ingresar)
                                #print("arista[0] ",arista[0])
                                ingresar.remove(arista[0])
                                listaPre.clear()
                                break
                    else:
                        if ((arista[0] not in ingresar) & (arista[1] in ingresar)):
                            #print("CASO 2")
                            for arb in listaTree:
                                listaPre = arb.preorden2(arb.raiz)
                                if arista[0] in listaPre:
                                    #print("ingresar ",ingresar)
                                    peso = arcosAux[0][1]
                                    arb.insertar(arb.raiz,arista[0],arista[1],peso)
                                    ingresar.remove(arista[1])
                                    listaPre.clear()
                                    break
                        else:
                            # COMENTARIO: ((arista[0] not in ingresar) & (arista[1] not in ingresar)):
                            #print("CASO 3")
                            arb2 = None
                            arb1 = None
                            peso = arcosAux[0][1]
                            for arb in listaTree:
                                listaPre = arb.preorden2(arb.raiz)
                                #print("lP ",listaPre)
                                if arista[0] in listaPre:
                                    arb1 = arb
                                    #if(arb2 != None):
                                    #    listaTree.remove(arb2)
                                    listaPre.clear()
                                if arista[1] in listaPre:
                                    arb2 = arb
                                    #if (arb1 != None):
                                    #    listaTree.remove(arb1)
                                    listaPre.clear()
                                listaPre.clear()
                            if((arb1.size) >= (arb2.size)):
                                listaTree.remove(arb2)
                                arb1.combinarArbol(arista[0],arb2,arista[1],peso)
                            else:
                                listaTree.remove(arb1)
                                arb2.combinarArbol(arista[1],arb1,arista[0],peso)
            #print("lT ,",listaTree)
        #else:
            #print("CASO 4")
        arcosAux.remove(arcosAux[0])
    return listaTree[0]




nodos =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
arcos = [[[16, 14], 625], [[19, 0], 666], [[2, 3], 235], [[17, 8], 84], [[18, 19], 678], [[14, 7], 540], [[1, 2], 349], [[15, 8], 304], [[14, 15], 588], [[13, 7], 282], [[5, 6], 413], [[6, 7], 481], [[13, 14], 410], [[0, 1], 151], [[17, 18], 220], [[8, 9], 428], [[9, 10], 767], [[10, 11], 654], [[15, 16], 232], [[11, 12], 736], [[4, 14], 979], [[3, 4], 250], [[19, 4], 375], [[17, 4], 440], [[7, 8], 997], [[4, 5], 654], [[5, 2], 530], [[14, 1], 518], [[12, 13], 509], [[8, 10], 381]]


kruskal_con_heap(nodos, arcos)