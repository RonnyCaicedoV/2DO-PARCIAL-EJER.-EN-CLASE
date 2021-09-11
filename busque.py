class Busqueda:
    def __init__(self,listas=None):
        self.__lista= listas
        
    @property
    def lista(self):
        if self.__lista != None:
            return self.__lista
        else:
            print("Lista esta vacia")
    
    """ def busquedaLineal(self,buscado):
        lon = len(self,buscado)
        enc=False
        pos= 0
        while pos < lon and enc== False:
            if self.__lista[pos]["nombre"] == buscado: enc=True
            else: pos +=1
        if enc: return pos
        else: return -1 """
        
bus1 = Busqueda([2,4,6])
bus1.lista= [1,3,5]
print("bus1",bus1.lista)
bus2 = Busqueda(['Ana','Dan',"Abdo"])
print("bus2",bus2.lista)
            
        
        