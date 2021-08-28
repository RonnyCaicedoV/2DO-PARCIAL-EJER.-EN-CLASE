import os
class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz
        
    def mostrar(self):
        os.system("cls")
        for fila in range(len(self.matriz)):
            #print(self.matriz[fila])
            for col in range(len(self.matriz[fila])):
                print(" [{}] ".format(self.matriz[fila][col]), end=" ")
            print()
        print("------------")
            
    def buscar(self,buscado):

        resp = {}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == buscado:
                    resp["fila"] = fila
                    resp["col"]=col
                    break
            if resp: break
        return resp
    
    def buscarW(self,buscado):

        resp = {}
        fila=0
        enc = False
        while fila < len(self.matriz) and enc==False:
            col=0
            while col < len(self.matriz[fila]) and enc==False:
                if self.matriz[fila][col] == buscado:
                    resp["fila"] = fila
                    resp["col"]=col
                    enc=True
                else: col +=1
            fila +=1
        return resp
            
                
                    
                
            
            
numeros = [[11,20,15],[10,25,30],[11,21,31]]

mat = Matriz(numeros)
resp = mat.buscar(225)
if resp:print(resp)
else:print("dato no encontrado")