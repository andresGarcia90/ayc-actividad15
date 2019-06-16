import Arbol;

arbol = Arbol.arbol()
#print("creo el arbol",arbol)

arbol.raiz = arbol.insertarRaiz(0)
#print("inserto la raiz: ",arbol.raiz.dato)
#0
#1 2
#3 4
arbol.insertar(arbol.raiz,0,1,10)
arbol.insertar(arbol.raiz,0,2,20)
arbol.insertar(arbol.raiz,1,3,30)
arbol.insertar(arbol.raiz,2,4,40)

arbol.preorden(arbol.raiz,0)

arbol2 = Arbol.arbol()
arbol2.raiz = arbol2.insertarRaiz(5)
arbol2.insertar(arbol2.raiz,5,6,10)
arbol2.insertar(arbol2.raiz,5,7,20)
arbol2.insertar(arbol2.raiz,6,8,30)
arbol2.insertar(arbol2.raiz,7,9,40)

# arbol2.preorden(arbol2.raiz,0)

arbol.combinarArbol(1,arbol2,8)

print("combinados")
arbol.preorden(arbol.raiz, 0)
# print(arbol.obtenerNodo(2))

# arbol2 = None
# print("rompemos las referencias")
# arbol.preorden(arbol.raiz, 0)

# print("arbol2 invertido")

# nodo8 = arbol2.obtenerNodo(8)
# arbol2.invertirArbol(arbol2.obtenerNodo(8))
# arbol2.preorden(arbol2.raiz, 0)