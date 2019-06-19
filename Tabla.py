
#esta clase se implemento para generar una tabla de visualizacion de datos de manera ordenada.
class Tabla:
    def __init__(self):
        self.head = ["n° Grafo", "Nodos", " Arcos  ", "    Flag-conexo  ", "       BFS     ", "  Disjoin-set   "]
        self.head_2 = ["n° Grafo", "Nodos", " Arcos ", "Flag-conexo", "   Kruskal Arcos  ", "  Kruskal MinHeap  ", "  Kruskal c/h   ","  Kruskal s/h   "]
        self.linea = 84
        self.linea_2 = 122
        self.datos = []
        self.datos_2 = []

    def insertar_tabla1(self,n,nodos,arcos,flag,bfs,ds):
        dato = [n,nodos,arcos,flag,bfs,ds]
        self.datos.append(dato)

    def insertar_tabla2(self,n,nodos,arcos,flag,ka,km,kch,ksh):
        dato = [n,nodos,arcos,flag,ka,km,kch,ksh]
        self.datos_2.append(dato)

    def imprimir_tabla1(self):
        s = ""
        for h in self.head:
            s = s + "| "+ h +" "
        s = s + "| "
        print(s)
        print(" ","-"*self.linea)

        for d in self.datos:
            print("| "," "*(4-len("  ")),d[0]," "*(3-len(str(d[0]))),"| ", d[1], " "*(3-len(str(d[1]))), "| ", d[2], " "*(6-len(str(d[2]))), "|       ", d[3], " "*(9-len(str(d[3]))), "|  ", d[4], " "*(12-len(str(d[4]))), "|  ", d[5], " "*(13-len(str(d[5]))), "| " )
        print(" ","-"*self.linea)
        print("")
        print("")

    def imprimir_tabla2(self):
        s = ""
        for h in self.head_2:
            s = s + "| "+ h +" "
        s = s + "| "
        print(s)
        print(" ","-"*self.linea_2)
        for d in self.datos_2:
            print("| "," "*(4-len("  ")),d[0], " "*(3-len(str(d[0]))),"| ", d[1], " "*(3-len(str(d[1]))), "| ", d[2], " "*(5-len(str(d[2]))), "|    ",d[3]," "*(6-len(str(d[3]))),"|   ",d[4]," "*(14-len(str(d[4]))),"|    ",d[5]," "*(14-len(str(d[5]))),"| ",d[6]," "*(14-len(str(d[6]))),"| ",d[7]," "*(14-len(str(d[7]))),"| ")
        print(" ","-"*self.linea_2)
        print("")
        print("")








# #1era parte
# head = ["n° Grafo", "Nodos", "Arcos", "Flag-conexo", "  BFS   ", "Disjoin-set"]

# datos = [[0,10,20,"si",True,True],[1,100,200,"si",False,False]]

# #2da Parte
# head_2 = ["n° Grafo", "Nodos", "Arcos", "Flag-conexo", "Kruskal Arcos", "Kruskal MinHeap", "Kruskal c/h ","Kruskal s/h "]

# datos_2 = [[0,10,20,"si",0.11123,0.121345,0.123456,0.123456], [1,100,200,"si",123.11123,213.121345,123.123456,123.123456]]

t = Tabla()
# t.insertar_tabla1(0,10,20,'si',True,True)
# t.insertar_tabla1(1,100,200,'si',False,False)
# t.insertar_tabla2(0,10,20,'si',0.11123,0.121345,0.123456,0.123456)
# t.insertar_tabla2(1,100,200,'si',123.11123,213.121345,123.123456,123.123456)

# t.imprimir_tabla1()
# t.imprimir_tabla2()




# t.insertar_tabla2(1    ,  10      ,  20   ,     "sí"      ,    0.0009982586  ,     0.0011141300  ,  0.1141307354  ,  0.1141307354 )
# t.insertar_tabla2(2    ,  150     ,  1000  ,     "sí"      ,    0.2508542538  ,     0.1908674240  ,  0.1141307354  ,  0.1141307354 )
# t.insertar_tabla2(3    ,  200     ,  3000  ,     "sí"      ,    1.7468590736  ,     0.8640789986  ,  0.1099717617  ,  0.1141307354 )
# t.insertar_tabla2(4    ,  300     ,  10000  ,     "sí"      ,    15.8205623627  ,     5.7362244129  ,  0.2242536545  ,  0.1141307354 )
# t.insertar_tabla2(5    ,  400     ,  25000  ,     "sí"      ,    88.8754143715  ,     16.8085939884  ,  0.4907774925  ,  0.1141307354 )
# t.insertar_tabla2(6    ,  500     ,  50000  ,     "sí"      ,    294.1808199883  ,     33.6111192703  ,  0.6490764618  ,  0.1141307354 )


# t.insertar_tabla1(     1    ,  10   ,  20   ,     "sí"      ,   0.0009922981  ,   0.0019958019  )
# t.insertar_tabla1(     2    ,  150  ,  1000  ,     "sí"      ,   0.0019934177  ,   0.3121240139  )
# t.insertar_tabla1(     3    ,  200  ,  3000  ,     "sí"      ,   0.0019938946  ,   0.7026546001  )
# t.insertar_tabla1(     4    ,  300  ,  10000  ,     "sí"      ,   0.0025513172  ,   3.4381537437  )
# t.insertar_tabla1(     5    ,  400  ,  1000  ,     "no"      ,   0.0045695305  ,   0.5452449322  )
# t.insertar_tabla1(     6    ,  500  ,  1000  ,     "no"      ,   0.0009987354  ,   0.7040302753  )





# t.imprimir_tabla2()
# t.imprimir_tabla1()



# t.insertar_tabla1(     1    ,  10   ,  20   ,   "sí"    , 0.0010087490  ,   0.0010087490  ) 
# t.insertar_tabla1(     2    ,  150  ,  1000 ,   "sí"    ,  0.0010087490  ,   0.1585950851  ) 
# t.insertar_tabla1(     3    ,  200  ,  3000 ,   "sí"    ,  0.0019953251  ,   0.6074497700  ) 
# t.insertar_tabla1(     4    ,  300  ,  10000,   "sí"    ,   0.0039892197  ,   3.1835587025  ) 
# t.insertar_tabla1(     5    ,  400  ,  1000 ,   "no"    ,  0.0030226707  ,   0.5046510696  ) 
# t.insertar_tabla1(     6    ,  500  ,  10000,   "sí"    ,   0.0050160885  ,   6.0090534687  )
# t.imprimir_tabla1()