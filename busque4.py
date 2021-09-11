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
        
    def ordenar(self,orden):
        if orden == "asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["Nombre"] > self.__lista[sig]["Nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
        
        else:
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["Nombre"] < self.__lista[sig]["Nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
        
    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin = len(self.lista)-1
        inicio = 0
        enc = False
        while inicio <= fin and enc == False:
            medio = (inicio+fin)//2
            if self.lista[medio]["Nombre"] == buscado: enc= True
            elif self.lista[medio]["Nombre"] < buscado: inicio = medio+1
            else: fin = medio-1
            
        if enc: return medio
        else: return -1
            
            

notas = [
    {'Nombre':"Ana","n1":60,"n2":40},
    {'Nombre':"Dana","n1":20,"n2":40},
    {'Nombre':"Dany","n1":30,"n2":50},
    {'Nombre':"Dayana","n1":40,"n2":50},
    {'Nombre':"Erson","n1":50,"n2":40},
    {'Nombre':"Rommel","n1":55,"n2":40},
    
                
]

print(notas[3])
bus = Busqueda(notas)
pos = bus.busquedaBinaria("Erson")
if pos >= 0: print(bus.lista[pos])
else: print("No ese nombre en la lista")