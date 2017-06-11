import pila

class Nodo_Cola():
    def __init__(self, info):
        self.info = info
        self.pila = pila.Pila()
        self.siguiente = None
            
class Cola():
    def __init__(self):
        self.frente = None
        self.ultimo = None
        
    def encolar(self,valor):
        nuevo = Nodo_Cola(valor)
        nuevo.siguiente = None
        
        if(self.frente == None):
            self.frente = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        
    def desencolar(self):
        if(self.frente==None):
            print("La pila esta vacia")
        else:
            eliminar = self.frente
            self.frente = self.frente.siguiente
            print("se desencolo")
            return eliminar
            del eliminar
        
        
        
    def mostrar(self):
        
        pos = 0
        aux = self.frente
        while(aux!=None):
            pos = pos + 1
            print("Valor:en pos"+ str(pos) , aux.info)
            aux = aux.siguiente
            
    def graficar(self):
        
        cadena = open("texto_cola.dot","w")
        cadena.write("digraph g{\n")
        cadena.write("rankdir=LR\n")
        cadena.write("")
        pos = 0
        aux = self.frente
        while(aux!=None):
            
            cadena.write(str(aux) + "[label = "+ " <"+ str(aux.info) + " >" +", shape =box, style=filled, fillcolor=red] \n")
            
            ##print("Valor: ", aux.info)
            aux = aux.siguiente

        aux2 = self.frente
        while(aux2!=None):
            cadena.write(str(aux2) +"->"+str(aux2.siguiente))
            aux2 = aux2.siguiente
        
        cadena.write("\n")
        cadena.write("}\n")
        cadena.close
        
        
        