class Archivo:
    def __init__(self,nombreArchivo, separador=" "):
          self.__archivo = nombreArchivo
          
        
    
    def leer(self):
        with open(self.__archivo, "r", encoding="UTF-8") as file:
            lista= []
            for linea in file:
               lista.append(linea[:-1])
        return lista
    
    
    
arch = Archivo("estudiantes.txt")
lista= arch.leer()
print(lista)