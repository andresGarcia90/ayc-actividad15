class Tabla:
    def __init__(self):
        self.head = ["n° Grafo", "Nodos", "Arcos", "Flag-conexo", "  BFS   ", "Disjoin-set"]
        self.head_2 = ["n° Grafo", "Nodos", "Arcos", "Flag-conexo", "  Kruskal Arcos ", "  Kruskal MinHeap", "  Kruskal c/h ","  Kruskal s/h "]
        self.linea = 64
        self.linea_2 = 103
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
            print("| "," "*(4-len("  ")),d[0]," "*(3-len(str(d[0]))),"| ", d[1], " "*(3-len(str(d[1]))), "| ", d[2], " "*(3-len(str(d[2]))), "|    ", d[4], " "*(6-len(str(d[4]))), "|  ", d[4], " "*(5-len(str(d[4]))), "|   ", d[5], " "*(7-len(str(d[5]))), "| " )
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
            print("| "," "*(4-len("  ")),d[0], " "*(3-len(str(d[0]))),"| ", d[1], " "*(3-len(str(d[1]))), "| ", d[2], " "*(3-len(str(d[2]))), "|    ",d[3]," "*(6-len(str(d[3]))),"|   ",d[4]," "*(9-len(str(d[4]))),"|    ",d[5]," "*(10-len(str(d[5]))),"| ",d[6]," "*(10-len(str(d[6]))),"| ",d[7]," "*(10-len(str(d[7]))),"| ")
        print(" ","-"*self.linea_2)
        print("")
        print("")








# #1era parte
# head = ["n° Grafo", "Nodos", "Arcos", "Flag-conexo", "  BFS   ", "Disjoin-set"]

# datos = [[0,10,20,"si",True,True],[1,100,200,"si",False,False]]

# #2da Parte
# head_2 = ["n° Grafo", "Nodos", "Arcos", "Flag-conexo", "Kruskal Arcos", "Kruskal MinHeap", "Kruskal c/h ","Kruskal s/h "]

# datos_2 = [[0,10,20,"si",0.11123,0.121345,0.123456,0.123456], [1,100,200,"si",123.11123,213.121345,123.123456,123.123456]]

# t = Tabla.Tabla()
# t.insertar_tabla1(0,10,20,'si',True,True)
# t.insertar_tabla1(1,100,200,'si',False,False)
# t.insertar_tabla2(0,10,20,'si',0.11123,0.121345,0.123456,0.123456)
# t.insertar_tabla2(1,100,200,'si',123.11123,213.121345,123.123456,123.123456)

# t.imprimir_tabla1()
# t.imprimir_tabla2()