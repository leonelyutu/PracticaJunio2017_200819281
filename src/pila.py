
class Nodo_Pila():
    def __init__(self,info):
        self.info = info
        self.next = None
        print("Nueva instancia de nodo")



class Pila():
    def __init__(self):
        self.top = None
       # self.deep = None

    def size(self):
        pass

    def push(self,info):
        new = Nodo_Pila(info)
        new.next = None

        if(self.top == None):
            self.top = new
        else:
            new.next=self.top
            self.top = new

    def pop(self):
        valorinfo = 0
        if(self.top == None):
            print("Pila vacia")
        else:

            eliminar = self.top
            print("Se desapilo", eliminar.info)

            valorinfo = eliminar.info
            self.top = self.top.next

        return valorinfo




    def cima(self):

        if(self.top == None):
            print("Error.. Pila vacia")
        else:
            return self.top.info


    def view(self):

        aux = self.top
        while(aux!=None):
            print("valor:", aux.info)
            aux = aux.next
            
            
            

    def push_num(self, valor):
##        for xxx in range(1, 3):
##            print "Hello world"
        if ( valor=="*" or valor=='-' or valor=="+"):
            resultado = 0
            ope2 = self.pop()
##            print "*********************************"
##            print(ope2)
##            print "*********************************"
            ope1 = self.pop()
##            print(ope1)
            #resultado = self.operar(ope1, ope2, valor)
            if valor == '+':
                resultado = ope1 + ope2
                print "El resultado de operar " + str(ope1) + " " + valor + " " + str(ope2) + " es: " + str(resultado)

            elif valor == '-':
                resultado = ope1 - ope2
                print "El resultado de operar " + str(ope1) + " " + valor + " " + str(ope2) + " es: " + str(resultado)
            elif valor == '*':
                resultado = ope1 * ope2
                print "El resultado de operar " + str(ope1) + " " + valor + " " + str(ope2) + " es: " + str(resultado)
            self.push_num(resultado)
        else:
            val = int(valor)
            nuevo = Nodo_Pila(val)
            nuevo.next = self.top
            
            self.top = nuevo


#    def operar(self, op1, op2, operador):
#        resutl = 0
#
#        if operador == '+':
#            result = op1 + op2
#
#        elif operador == '-':
#            result = op1 - op2
#
#        elif operador == '*':
#            resutl = op1 * op2
#
#        return result
#
#



    def graficar(self):
        cadena = open("texto_Pila.dot","w")
        cadena.write("digraph g{\n")
        cadena.write("rankdir=LR\n")
        cadena.write("")
        
        aux = self.top
        while(aux!=None):
            cadena.write(str(aux) + "[label = "+ " <"+ str(aux.info) + " >" +", shape =box, style=filled, fillcolor=red] \n")
            ##print("valor:", aux.info)
            aux = aux.next
            
        aux2 = self.top
        while(aux2!=None):
            cadena.write(str(aux2) +"->"+str(aux2.next))
            aux2 = aux2.next
        
        
        cadena.write("\n")
        cadena.write("}\n")
        cadena.close
        
        
        
            