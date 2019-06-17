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