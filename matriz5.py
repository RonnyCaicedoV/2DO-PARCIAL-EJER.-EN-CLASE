import os
class Matriz:
    def __init__(self, nfilas, ncols):
        self.matriz = []
        self.noFilas= nfilas
        self. noCols= ncols
        
    def ingresar(self):
        os.system("cls")
        self.matriz= []
        for fila in range(self.noFilas):
            columnaas= []
            for col in range(self.noCols):
                valor= input("Fila[{}] Col[{}]: ".format(fila,col))
                columnaas.append(valor)
            self.matriz.append(columnaas)
        #print(self.matriz)
        
    
    
    def mostrar(self):
        #os.system("cls")
        print("------------")
        for fila in range(len(self.matriz)):
            #print(self.matriz[fila])
            for col in range(len(self.matriz[fila])):
                print(" [{}] ".format(self.matriz[fila][col]), end=" ")
            print()
        print("------------")
        
    def sumar (self,mat2):
        sumaMatriz= []
        for fila in range(self.noFilas):
            columnaas= []
            for col in range(self.noCols):
                valor= self.matriz[fila][col] + mat2[fila][col]
                columnaas.append(valor)
            sumaMatriz.append(columnaas)
        
        return sumaMatriz
        
        
        
        
numeros=[]
mat1= Matriz(2,2)
mat1.ingresar()
mat2= Matriz(2,2)
mat2.ingresar()
mat1.mostrar()
mat2.mostrar()
mat2.matriz = mat2.sumar(mat1.matriz)
mat1.mostrar()
