class BinHeap:
  #Constructor de la clase BinHeap
    def __init__(self):
        self.heapList = [0]           #inicializamos el heap con una lista con un elemento inicial que solamente se utiliza para que no de error en futuros metodos
        self.currentSize = 0          #para mantener el tamaño actual del heap
    
    #Metodo que retorna el tamaño actual del heap
    def size(self):
      return self.currentSize

    #percolate, para mantener la propiedad de los heaps desde la hoja hacia el padre
    def percUp(self,i):
        while i // 2 > 0:            #mientas el padre sea diferente de 0 (primer elemento)
          if self.heapList[i][0] < self.heapList[i // 2][0]:  # si el elemento es menor que el padre
             tmp = self.heapList[i // 2]                      #intercambiamos el elemento
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2                                          #recorremos hasta la raiz

    #metodo de insercion en el heap
    def insert(self,k):
      self.heapList.append(k)                     #agregamos el elemento al final de la lista con la funcion append() #O(1)
      self.currentSize = self.currentSize + 1     #aumentamos el tamaño del heap en 1
      self.percUp(self.currentSize)               #realizamos percolate para mantener la propiedad de los heaps       #O(logn)

    #percolate inverso, hacia abajo
    def percDown(self,i):                         
      while (i * 2) <= self.currentSize:        #mientras que i*2 sea menor que el tamaño actual del heal
          mc = self.minChild(i)                 #obtenemos el minimo hijo de i
          if self.heapList[i][1] > self.heapList[mc][1]:    #si el hijo es mas chico que el padre intercambiamos valores
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc                                 #actualizamos valor de i

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
              return i * 2
          else:
              return i * 2 + 1

    #metodo que elimina el menor elemento del heap
    def delMin(self):
      retval = self.heapList[1] #elemento a retornar
      self.heapList[1] = self.heapList[self.currentSize]  #movemos el ultimo elemento de la lista hasta la posicion de la raiz
      self.currentSize = self.currentSize - 1             #decrementamos el valor total ya que eliminamos un elemento
      self.heapList.pop()                             
      self.percDown(1)                                    #restauramos la propiedad del heap "bajando" la nueva raiz hasta su correcta posicion
      return retval                                       #orden logn en el caso de tener que hacer percdown hasta el fondo del arbol
    
    #metodo principal para la creacion de heaps
    #recibe como parametro una lista de keys
    def buildHeap(self,alist):                            
      i = len(alist) // 2                     #size de la mitad de la lista                 
      self.currentSize = len(alist)           #tamaño total del heap = tamaño de la lista de entrada
      self.heapList = [0] + alist[:]          #cargamos los nodos en la lista
      while (i > 0):
          self.percDown(i)                    #mientras i > 0 ordenamos , esto seria desde la mitad del arreglo hacia la raiz
          i = i - 1

# bh = BinHeap()
# bh.buildHeap( [[[5, 9], 2], [[8, 3], 83], [[4, 7], 412], [[0, 6], 454], [[8, 0], 101], [[3, 7], 1], [[1, 4], 679], [[7, 0], 846], [[1, 6], 459], [[8, 9], 893], [[8, 5], 85], [[9, 2], 766], [[2, 8], 336], [[3, 4], 980], [[5, 7], 181], [[7, 1], 683], [[0, 4], 77], [[3, 1], 556], [[2, 1], 872], [[9, 4], 862]])
