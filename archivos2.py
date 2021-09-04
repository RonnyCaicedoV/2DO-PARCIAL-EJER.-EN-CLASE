class Archivo:
    def __init__(self,nombreArchivo):
          self.__archivo = nombreArchivo
          
          
          
          
          
    def escribir(self,datos,modo):
        with open(self.__archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")
                
                
                
                

arch = Archivo("estudiantes.txt")
articulos = [[1,"Aceite", "Girasol",2.50,200],[2,"Leche","Nido",1.50,300]]
arch.escribir(["Saul", "Danna", "Ronaldo"], "w")