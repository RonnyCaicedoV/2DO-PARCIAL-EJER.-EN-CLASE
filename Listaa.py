class lista:
    def __init__(self,list):
        self.list=list
        self.longitud=0
        
    def empty(self):
        return self.longitud == 0     
    
    
    def buscar(self,dato):  
        for pos in range(len(self.list)):
            if self.list[pos] == dato:
                return "El numero {} se encontro en la posicion {} ".format(dato,pos)   
        return -1        
        
    def insertar(self,dato):
        if self.buscar(dato) == -1:
            self.list += [dato]
            self.longitud += 1
            print ("El dato que no se encontro se asigno a la lista: {}".format(self.list))
        else:
            print("El numero que ingreso si se encuentra en la lista")
    
    
    def eliminar(self, dato):
        if self.buscar(dato) !=-1:
            self.list.remove(dato)
            print(self.list)
        else:
            print("El numero a eliminar no existe")