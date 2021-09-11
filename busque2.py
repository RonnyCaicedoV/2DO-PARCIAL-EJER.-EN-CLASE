class Busqueda:
    def __init__(self,listas=None):
        self.__lista= listas
        
    @property
    def lista(self):
        if self.__lista != None:
            return self.__lista
        else:
            print("Lista esta vacia")
    
    def busquedaLineal(self,buscado):
        lon = len(self,buscado)
        enc=False
        pos= 0
        while pos < lon and enc== False:
            if self.__lista[pos]["nombre"] == buscado: enc=True
            else: pos +=1
        if enc: return pos
        else: return -1
        
        
notas = [
    {'Nombre':"Dany","n1":20,"n2":40},
    {'Nombre':"Dana","n1":30,"n2":50},
    {'Nombre':"Dayana","n1":40,"n2":50},
    {'Nombre':"Andrew","n1":50,"n2":40},
    {'Nombre':"Rommel","n1":55,"n2":40},
    {'Nombre':"Yamilet","n1":60,"n2":40},
                
]

print(notas[3])
bus = Busqueda(notas)
print(bus.busquedaLineal("Andrew"))