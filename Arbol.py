#Prueba algo

class nodo:
    padre = None
    hijos = None
    dato =  0
    #peso_padre
    def __init__(self, dato, peso):
        # crea un nodo
        self.hijos = None
        self.dato = dato
        self.peso_padre = peso
        
class arbol:
    def __init__(self):
        # inicializa la raiz
        self.raiz = None
        self.size = 0
        self.nodos = []

    def insertarRaiz(self,dato):
        self.raiz = self.agregarNodo(dato,0)
        self.nodos.append(self.raiz)
        return self.raiz
 
    def insertar(self, nodo, padre, dato, peso):
        #print("estoy aca", self, nodo.dato ,padre, dato, peso)
        if (nodo.dato == padre):
            if(nodo.hijos == None):
                nodo.hijos = []
            nodohijo = self.agregarNodo(dato,peso)
            nodohijo.padre = nodo
            nodo.hijos.append(nodohijo)
            self.nodos.append(nodohijo)
        else:
            if nodo.hijos != None:
                for h in nodo.hijos:
                    self.insertar(h,padre,dato,peso)

    def combinarArbol(self, dato1, arbol2, dato2,peso):
        #asumo que los dos arboles tienen los datos
        nodo1 = self.obtenerNodo(dato1)
        nodo2 = arbol2.obtenerNodo(dato2)
        #print("combinarArbol: nodo1", nodo1," nodo2 ",nodo2)
        self._combinarArbol(nodo1,arbol2,nodo2,peso)
        self.size = self.size + arbol2.size



    def _combinarArbol(self,nodo,arbol2,nodo2,peso):
        if (nodo2.padre == None):
            #print("combino la raiz")
            nodo2.padre = nodo
            nodo2.peso_padre = peso
            if nodo.hijos == None:
                nodo.hijos = []
            nodo.hijos.append(nodo2)
            #for n in arbol2.nodos:
            #    self.nodos.append(n)
            self.nodos.extend(arbol2.nodos)
        else:
            #print("caigo aca")
            arbol2.invertirArbol(nodo2,peso)
            if nodo.hijos == None:
                nodo.hijos = []
            nodo.hijos.append(nodo2)
            nodo2.padre = nodo              
            self.nodos.extend(arbol2.nodos)
            

    def invertirArbol(self,nodo,peso):
        if nodo.padre != None:
            nodoPadre = nodo.padre
            if nodo.hijos == None:
                nodo.hijos = []
            nodo.hijos.append(nodoPadre)
            nodo.padre = None
            self.invertirArbol(nodoPadre,peso)
            nodoPadre.padre = nodo
            #actualizar peso
            nodoPadre.peso_padre = nodo.peso_padre
            nodo.peso_padre = peso
            nodoPadre.hijos.remove(nodo)
            self.raiz = nodo      
        
    def obtenerNodo(self,dato):
        for n in self.nodos:
            if(n.dato == dato):
                return n 
        
    def obtenerRaiz(self):
        return self.raiz

    def agregarNodo(self, dato, peso):
        # crea un nuevo nodo y lo devuelve
        self.size = self.size+1
        return nodo(dato,peso)
 
    def preorden(self,nodo,nivel):
        if (nodo != self.raiz):
            print("nodo: ",nodo.dato, " padre: ",nodo.padre.dato , "peso al padre ",nodo.peso_padre," nivel ",nivel)
        else:
            print("nodo raíz: ",nodo.dato, " nivel ",nivel)
        if(nodo.hijos != None):
            for h in nodo.hijos:
                self.preorden(h,nivel+1)
    
    def preorden2(self,nodo,lista = []):
        lista.append(nodo.dato)
        if(nodo.hijos != None):
            for h in nodo.hijos:
                self.preorden2(h)
        return lista

    def preorden3(self,nodo,lista = []):
        lista.append(nodo)
        if(nodo.hijos != None):
            for h in nodo.hijos:
                self.preorden3(h)
        return lista


# arbol=arbol()
# print("creo el arbol",arbol)
# arbol.raiz = arbol.insertarRaiz(0)
# print("inserto la raiz: ",arbol.raiz.dato)
# arbol.insertar(arbol.raiz,0,1,1)
# arbol.insertar(arbol.raiz,0,2,1)
# arbol.insertar(arbol.raiz,1,3,1)
# arbol.insertar(arbol.raiz,2,4,1)
# print(arbol.preorden(arbol.raiz,0))

