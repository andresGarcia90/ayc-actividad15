import Arbol
import DisjointSet


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

def buscarNodo(lista, elemento):
    for l in lista:
        if l.value == elemento:
            return l


def kruskal_con_conjunto(nodos,arcos):
    arcosOrdenados=[]
    #inserto arcos en la lista ordenada
    for arco in arcos:
        agregarElementoLista(arcosOrdenados, arco)
    print("k arcos ordenados",arcosOrdenados)
    #creo el arbol vacio
    t = Arbol.arbol()
    nodos_len = len(nodos)
    i = 0

    #creo los conjuntos de nodos
    listaDS = []
    for nodo in nodos:
        a = DisjointSet.MakeSet(nodos[i])
        i=i+1
        listaDS.append(a)
    print("listaDS: ",listaDS)
    i = 0
    while (i<nodos_len):
        arco = obtenerPrimero(arcosOrdenados)
        print("asd", arco[0][0], arco[0][1])
        u = buscarNodo(listaDS,arco[0][0])
        v = buscarNodo(listaDS,arco[0][1]) 
        # print("arcos: ",arco)
        u_conjunto = DisjointSet.findSet(u)
        v_conjunto = DisjointSet.findSet(v)
        if u_conjunto != v_conjunto:
            DisjointSet.joinSet(u_conjunto,u_conjunto)
            if i==0:
                aux = t.insertarRaiz(u)
                print("raiz ", aux.dato)
                print("obtener raiz", t.obtenerRaiz().dato)
                # t.insertar(t.obtenerRaiz,u,v)
                i=i+2
            else:
                # t.insertar(t.obtenerRaiz,u,v)
                i = i + 1

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



# lista = []

# agregarElementoLista(lista,[[0,1],10])
# print("lista: ", lista)
# agregarElementoLista(lista,[[0,3],30])
# print("lista: ", lista)
# agregarElementoLista(lista,[[1,3],20])
# print("lista: ", lista)

arcos= [[[0,1],10],[[0,2],30]]
print("arcos",arcos)
nodos = [0,1,2]
print("nodos", nodos)

kruskal_con_conjunto(nodos, arcos)