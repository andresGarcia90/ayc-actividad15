
#Esta clase implementa un nodo de arbol con padre hijos y dato asociado
class nodo:
    padre = None
    hijos = None
    dato =  0
    #constructor de la clase padre
    def __init__(self, dato, peso):
        # crea un nodo
        self.hijos = None
        self.dato = dato
        self.peso_padre = peso

#clase que implementa la estructura de datos arbol
class arbol:
    def __init__(self):
        # inicializa la raiz
        self.raiz = None
        self.size = 0
        self.nodos = []
    #metodo para insertar un nodo y definirlo como raiz
    def insertarRaiz(self,dato):
        self.raiz = self.agregarNodo(dato,0)
        self.nodos.append(self.raiz)
        return self.raiz
    #metodo insertar de arbol, toma un nodo, su valor, el padre y el peso
    def insertar(self, nodo, padre, dato, peso):
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
    #Metodo que dado dos arboles los combina en uno resultante
    def combinarArbol(self, dato1, arbol2, dato2,peso):
        #asumo que los dos arboles tienen los datos
        nodo1 = self.obtenerNodo(dato1)
        nodo2 = arbol2.obtenerNodo(dato2)
        #print("combinarArbol: nodo1", nodo1," nodo2 ",nodo2)
        self._combinarArbol(nodo1,arbol2,nodo2,peso)
        self.size = self.size + arbol2.size



    def _combinarArbol(self,nodo,arbol2,nodo2,peso):
        if (nodo2.padre == None):               #si el nodo2 es raiz
            #print("combino la raiz")
            nodo2.padre = nodo
            nodo2.peso_padre = peso
            if nodo.hijos == None:
                nodo.hijos = []             
            nodo.hijos.append(nodo2)            #inserto el nodo2 en la lista de hijos del primer nodo   
            #for n in arbol2.nodos:
            #    self.nodos.append(n)
            self.nodos.extend(arbol2.nodos)
        else:                                   #sino 
            #print("caigo aca")
            arbol2.invertirArbol(nodo2,peso)    #invierto el arbol nodo2
            if nodo.hijos == None:
                nodo.hijos = []
            nodo.hijos.append(nodo2)            #agrego el nodo2 en hijos de nodo
            nodo2.padre = nodo                  #defino a nodo como padre de nodo2
            self.nodos.extend(arbol2.nodos)
            
    #Metodo que dado un nodo lo lleva desde su posicion en la jerarquia de arbol hasta la raiz del mismo    O(logn)
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

    #Metodo que retorna el nodo que contiene el dato
    def obtenerNodo(self,dato):
        for n in self.nodos:
            if(n.dato == dato):
                return n 
    #getter de raiz
    def obtenerRaiz(self):
        return self.raiz
    #creo un nodo nuevo
    def agregarNodo(self, dato, peso):
        # crea un nuevo nodo y lo devuelve
        self.size = self.size+1
        return nodo(dato,peso)
    #Recorrido en preorden
    def preorden(self,nodo,nivel):
        if (nodo != self.raiz):         #si el nodo no es la raiz
            print("nodo: ",nodo.dato," "*(2-len(str(nodo.dato))), " padre: ",nodo.padre.dato ," "*(2-len(str(nodo.padre.dato))), "peso al padre: ",nodo.peso_padre," "*(3-len(str(nodo.peso_padre)))," nivel: ",nivel)
        else:
            print("raíz: ",nodo.dato," "*(3-len(str(nodo.dato))), " nivel ",nivel)
        if(nodo.hijos != None):
            for h in nodo.hijos:                #por cada hijo de nodo
                self.preorden(h,nivel+1)        #realizo el preorden de cada uno en el nivel siguiente
