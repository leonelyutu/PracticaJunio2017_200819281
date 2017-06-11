
import menu
import pila
import matriz
import archivo
from xml.dom import minidom
import lista_circular_usuarios


class principal:
    def init(self):
        pass

    def main(self):

        print("Bienvenido, Practica Junio EDD")
        archivo_nuevo = archivo.archivo()
        lista_usuarios = lista_circular_usuarios.Lista()
        

        menu_1 = menu.menu() ##instancia de menu
        opcion = 0

        while(opcion != 3):
            opcion = menu_1.menu_1()
            #print(opcion)

            ########Acciones de opcion Crear Usuario###########
            if opcion == 1:
                print("Elijio Opcion", opcion)

                nombre = raw_input("Ingrese un Nombre\n")
                clave =  raw_input("Ingrese una clave\n")

                lista_usuarios.insertar_ultimo(nombre,clave)
                
                lista_usuarios.graficar() ##pendiente de revision
                
            ############Final de Acciones de Crear Usuario########

        #########Acciones de Ingreso al Sistema de usuario###############
            elif opcion == 2:

                print("Elijio Opcion", opcion)
                nombre = raw_input("Ingrese un Nombre\n")
                clave = raw_input("Ingrese una clave\n")

                contenedor_nodo = lista_usuarios.buscar_usuario_contrasenia(nombre,clave)

                ###acciones de usuario encontrado#####

                if(contenedor_nodo != None):
                    print("Bienvenido :",contenedor_nodo.info)

                    while(opcion != 6):
                        opcion = menu_1.menu_2()

                    ############Acciones de lectura de archivo#############
                        if opcion == 1:
                            
                            
                            
                                ##lectura = ""
                            
                            nombre_archivo = raw_input("Ingrese el nombre de archivo\n")
                            lectura_archivo = archivo_nuevo.leer(nombre_archivo)
                            contenedor_nodo.archivo_cargado = 1
                            ##print(lectura_archivo)

                ############# lectura de xml con xmldom#############################
                            
                            try:
                                xmldoc = minidom.parseString(lectura_archivo)


                                itemlist = xmldoc.getElementsByTagName("x")
                                for i in itemlist:
                                    print(i.firstChild.nodeValue)
                                    columnas = i.firstChild.nodeValue
                                    columnas = int(columnas)
                                itemlist = xmldoc.getElementsByTagName("y")
                                for i in itemlist:
                                    filas = i.firstChild.nodeValue
                                    filas = int(filas)
                                    print(i.firstChild.nodeValue)


                                    print(contenedor_nodo.matriz.conteo)
                                    if(contenedor_nodo.matriz.conteo == 0):
                                        contenedor_nodo.matriz.inicializar(filas,columnas)
                                    else:
                                        print("--------Ya se cargo una matriz en memmoria-----------")


                                itemlist = xmldoc.getElementsByTagName("operacion")
                                for i in itemlist:
                                    print(i.firstChild.nodeValue)
                                    cadena = i.firstChild.nodeValue
                                    cadena = cadena.split()
                                    infor = ""
                                    for cd in cadena:
                                        infor = infor + ' '+ cd
                                        
                                    contenedor_nodo.cola.encolar(infor)
                            except:
                                print("verifique nombre de archivo")

                       ###############Inicio de acciones de Mostrar Operaciones en Cola######################
                        if opcion == 2:
                            
                            
                            opcion_1 = 0
                            while(opcion_1 != 2):
                                opcion_1 = menu_1.menu_4()
                                
                                if opcion_1 == 1:
                                
                                    if(archivo_nuevo.contador == 0):
                                        print("---------debe Leer un archivo antes de ejecutar las acciones-----------")
                                    else:
                                        if contenedor_nodo.cola.frente != None:

                                            operaciones_cola = contenedor_nodo.cola.desencolar()
                ##                            print("Se desencolo", operaciones_cola)
                                            cadena = ""
                                            cadena = operaciones_cola.info
                ##                            print(operaciones_cola.info)

                                            cadena = operaciones_cola.info
                                            cadena = cadena.split()
                                            for cad in cadena:
                                                operaciones_cola.pila.push_num(cad)
                                                operaciones_cola.pila.graficar()
                                            print "Al operar la cadena: " + operaciones_cola.info +" : " +str(operaciones_cola.pila.top.info)
                                        else:
                                            print "No hay operaciones en la cola"

                                elif opcion_1 == 2:
                                            print('SALIENDO')

                       ##################Final de mostrar Operaciones en Cola##################################
                        
                        
                        
                        ##################Inicio de operaciones sobre la matriz########################
                        
                        if opcion == 3:
                            
                            if(archivo_nuevo.contador == 0):
                                print("---------debe Leer un archivo antes de ejecutar las acciones-----------")
                            else:
                                
                                print("Eligio la Opcion: " , opcion)
                                while(opcion != 5):
                                    opcion = menu_1.menu_3()

                                    if opcion == 1 :
                                        contenedor_nodo.matriz.llenar()

                                    if opcion == 2:
                                        contenedor_nodo.matriz.transpuesta()

                                    if opcion == 3:
                                        contenedor_nodo.matriz.imprimir()

                                    if opcion == 4:
                                        contenedor_nodo.matriz.imprimir_transpuesta()
                        
                        ##################Final de operaciones sobre la matriz#########################

                        ############# Inicio de acciones mostrar lista de usuarios  #################
                        if opcion == 4:
                            lista_usuarios.mostrar()
                            
                        ############# Final de acciones mostrar lista de usuarios ##########

                        ############### Inicio de acciones de Mostrar Cola #######################
                        if opcion == 5:
                            if(archivo_nuevo.contador == 0):
                                 print("-------------Debe leer un archivo antes de ejecutar acciones-----------")
                            else:
                                
                                contenedor_nodo.cola.mostrar()
                                contenedor_nodo.cola.graficar()
                        ###########Final de acciones de Mostrar Cola#########################


                else:######acciones de usuario no encontrado
                    print("Usuario no encotrado")

        ##########Final de acciones de Ingreso al Sistema ########

        ############Saliendo del Sistema #########################
            elif opcion == 3:
                print("Elijio Opcion", opcion)
                print("Saliendo del Sistema...")
       ############Final de Acciones Saliendo del Sistema #########

arranque = principal()
arranque.main()

