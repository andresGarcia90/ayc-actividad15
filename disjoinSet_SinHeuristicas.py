        
def MakeSet_SinHeuristica(x):
    return [x]

#creo que aca no me queda otra que considerar pasar por parametro el conjunto de sets 
#ademas asumo que el representativo de cualquier conjunto es el de la primer componente
#Siempre va a retornar un set porq en el conjunto conj al menos va a haber un set con x solamente
#nada eso 
def findSet_SinHeuristica(x,con):
    for arreglo in con:
        if (x in arreglo):
            return arreglo[0]

#este metodo recibe dos sets [] y el conjunto de sets con
def union_SinHeuristica(x,y,con):

    #busco nevamente los arreglos
    arreglou = None
    arreglov = None
    for arreglo in con:
        if (x in arreglo):
           arreglou = arreglo
        if (y in arreglo):
            arreglov = arreglo
    for item in arreglov:
        #x.append(item)                         #O(1)
        arreglou.extend([item])                 #O(n)
        
    
    nuevo_con = []
    for item in con:
        if(item != arreglov):
            nuevo_con.extend([item])          #agrego todos los conjuntos a un nuevo conjunto de conjuntos y 
            #nuevo_con.append(item)
    return nuevo_con                          #actualizo el conjunto de conjuntos a nuevo conjunto de conjuntos
    

