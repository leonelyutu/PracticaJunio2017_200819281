import os.path
from xml.dom import minidom


class archivo():
    def __init__(self):
        self.contador = 0
        


    def leer(self,nombre):##falta parametro nombre de archivo
        
        if (os.path.isfile(nombre)):
            self.contador = self.contador + 1
            infile = open(nombre, 'r')
            print('>>> Lectura completa del fichero')
            linea = infile.read()
            #print(linea)
            infile.close()

            ##print(linea)
            ##utilizacion de la funcion de lectura xmls
            xmldoc = minidom.parseString(linea)
            # obtenemos el valor del tag <x>
            print
            print ("Imprimir campos")
            print ("----------------------")
            itemlist = xmldoc.getElementsByTagName("x")
            for i in itemlist:
                i.firstChild.nodeValue

            itemlist = xmldoc.getElementsByTagName("y")
            for i in itemlist:
                i.firstChild.nodeValue

            itemlist = xmldoc.getElementsByTagName("operacion")
            for i in itemlist:
                i.firstChild.nodeValue

            return linea
        else:
            print("archivo no existe")
      