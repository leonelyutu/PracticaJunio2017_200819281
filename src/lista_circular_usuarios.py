import os
import sys
import matriz
import cola


class Nodo():
    def __init__(self, info, clave):
        self.info = info
        self.clave = clave
        self.siguiente = None
        self.anterior = None
        self.sesion = 0
        self.contenedor_cola = None
        self.archivo_cargado = 0
        self.cola = cola.Cola()
        self.matriz = matriz.matriz()
        
  ##      self.matriz = clase_matriz.mat()
    
        print("Nueva instancia de nodo")
        
    def get_sesion(self):
        return self.sesion
    
    def set_sesion(self,estado):
        self.sesion = estado
        
class Lista():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tam = 0
        print("Nueva instancia de Lista")
    
    def sesion(self,estado):
        self.sesion = estado
        
    def contenedor_de_cola(self,contenedor):
        self.contenedor_cola = contenedor
        
    def estado_sesion_actual(self):
        return self.sesion
    
    def obtener_contenedor_cola(self):
        return self.contenedor_cola
    
    
    def insertar_ultimo(self,valor,clave):
        print("Ingreso a Metodo insertar")
        

        if (self.primero == None):
            nuevo = Nodo(valor,clave)
            self.primero = nuevo
            self.ultimo = nuevo
            
            nuevo.siguiente =nuevo #opcional
            nuevo.anterior = nuevo #opcional
            self.tam = self.tam+1
            print("Ingreso a lista vacia")
        
        else:   
            if(self.buscar_en_lista(valor) == True):
                print("Elemento ya existe")
            else:
                nuevo = Nodo(valor,clave) #se puede hacer al inicio
                
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                
                nuevo.siguiente = self.primero
                self.ultimo = nuevo
                
                self.tam = self.tam+1

                print("Ingreso a utimo lista con nodo inicio")

            
    def buscar_en_lista(self,valor):
        aux = self.primero
        existe = False
        for x in range(self.tam):
           # print(aux.info) 
            if(aux.info == valor):
                existe = True
                break
            else:
                aux = aux.siguiente
        return existe
                
    def mostrar_lista(self):
        ultimo = false
        aux = self.primero
        while(aux!=None):
            print("Valor: ", aux.info)
            
            aux = aux.siguiente
        
    
    def mostrar(self):
        aux = self.primero
        for x in range(self.tam):
            print(aux.info,"->") 
            aux = aux.siguiente
        ##iteracion inversa
        aux2 = self.ultimo
        for x in range(self.tam):
            print(aux2.info) 
            aux2 = aux2.anterior

    def insertar_cola(self):
        self.cola.encolar(dato)
    
    def mostrar_colas(self):
        self.cola.mostrar()
        
    def buscar_usuario_contrasenia(self, nombre, clave):
        aux = self.primero
        encontrado = None
        existe = False
        for x in range(self.tam):
           # print(aux.info) 
            if(aux.info == nombre and aux.clave == clave):
                existe = True
                
                encontrado = aux 
                break
            else:
                aux = aux.siguiente 
        if(encontrado == None):
            print("Datos incorrectos")
        return encontrado
    
    def graficar(self):
        aux = self.primero
        cadena = open("texto.dot","w")
        cadena.write("digraph g{\n")
        cadena.write("rankdir=LR\n")
        
        ##impresion de elementos de lista circular
        
        aux = self.primero
        for x in range(self.tam):
            cadena.write(str(aux) + "[label = "+str(aux.info) +" shape =box, style=filled, fillcolor=red] \n")
            aux = aux.siguiente
        
        aux = self.primero
        for x in range(self.tam):
            cadena.write(str(aux) +"->"+str(aux.siguiente))
            #print(aux.info,"->") 
            aux = aux.siguiente
            
        aux2 = self.ultimo
        for x in range(self.tam):
            
            if(aux2 == self.primero):
                cadena.write(str(self.primero) + "->" +str(self.ultimo))
            else:
                cadena.write(str(aux2) +"->"+str(aux2.anterior))
            #print(aux2.info) 
            aux2 = aux2.anterior
    
        ##fin de impresion de elementos de lista circular
        
      
        
        ##inicio de impresion de colas de operaciones 
#        if(self.cola.frente == None):
#            print()
#        else:
#            aux3 = self.cola.frente
#            while(aux3!=None):
#                cadena.write(str(aux3) + "[label = "+str(aux3.info) +" shape =box, style=filled, fillcolor=red] \n")
#                ##print("Valor: ", aux.info)
#                aux3 = aux3.siguiente     
        ##fin de operacion de colas de operaciones
        
        cadena.write("}\n")
        cadena.close
        
        
       