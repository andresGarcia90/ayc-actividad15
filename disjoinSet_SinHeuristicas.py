        
def MakeSet_SinHeuristica(x):                   #O(1)
    return [x]

#creo que aca no me queda otra que considerar pasar por parametro el conjunto de sets 
#ademas asumo que el representativo de cualquier conjunto es el de la primer componente
#Siempre va a retornar un set porq en el conjunto conj al menos va a haber un set con x solamente
def findSet_SinHeuristica(x,con):               #O(n) en el peor caso busca en n sets de un elemento
    for arreglo in con:
        if (x in arreglo):
            return arreglo[0]

#este metodo recibe dos sets [] y el conjunto de sets con[[][][]...[]]
def union_SinHeuristica(x,y,con):
    #busco nevamente los arreglos
    arreglou = None
    arreglov = None
    for arreglo in con:                         #O(n) ya que busca dos sets pero no se repiten por definicion de dsijoin sets y recorre una sola vez el conjunto de conjuntos
        if (x in arreglo):                      #si encuentro x en el arreglo, guardo el arreglo en arreglou
           arreglou = arreglo
        if (y in arreglo):                      #si encuentro y en el arreglo, guardo el arrglo en arreglov
            arreglov = arreglo
    for item in arreglov:                       #O(n^2) ya que hace n veces extensiones de n elementos en el peor de los casos
        #x.append(item)                         #O(1) , es orden constante porque inserta en una lista enlazada
        arreglou.extend([item])                 #O(n) , es orden n porque lo que hace es crear un arreglo nuevo del tamaño del anterior mas el del extend y pasar todo uno a uno
    nuevo_con = []
    for item in con:                          #O(n) a lo sumo recorre los n items de conjunto de conjunto
        if(item != arreglov):
            nuevo_con.extend([item])          #agrego todos los conjuntos a un nuevo conjunto de conjuntos y 
            #nuevo_con.append(item)
    return nuevo_con                          #retorno el nuevo conjunto de conjuntos sin repeticion de conjuntos
    

