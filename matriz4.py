import os
class Matriz:
    def __init__(self, nfilas, ncols):
        self.matriz = []
        self.noFilas= nfilas
        self. noCols= ncols
        
    def ingresar(self):
        self.matriz= []
        for fila in range(self.noFilas):
            columnaas= []
            for col in range(self.noCols):
                valor= input("Fila[{}] Col[{}]: ".format(fila,col))
                columnaas.append(valor)
            self.matriz.append(columnaas)
        #print(self.matriz)
        
    
    
    def mostrar(self):
        os.system("cls")
        print("------------")
        for fila in range(len(self.matriz)):
            #print(self.matriz[fila])
            for col in range(len(self.matriz[fila])):
                print(" [{}] ".format(self.matriz[fila][col]), end=" ")
            print()
        print("------------")
        
    
        
        
        
        
        
numeros=[]
mat= Matriz(2,2)
mat.ingresar()
mat.mostrar()

        