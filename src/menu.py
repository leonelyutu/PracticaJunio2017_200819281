class menu():
    def __init(self):
        print()
    
    def menu_1(self):
        
        print("-----Ingresando al Menu principal--")
        print("         1. Crear Usuario")
        print("       2. Ingresar al Sistema")
        print("            3. Salir..")
        print("-----------------------------------")
        opcion = 0
        
        opcion = self.tratamiento()
        if(opcion == 0):
            print("Por favor intente co un numero del 1 al 9")
        return opcion 
       

    def tratamiento(self):
        try:
            numero = int(input("-----Elija una opcion-------\n"))
            return numero
        except:
            print("Parece que hay un error")
            return 0
    
    def menu_2(self):
        
        print("Ingersando al Sistema...")
        print("1. Leer Archivo")
        print("2. Resolver Operaciones")
        print("3. Operar la Matriz")
        print("4. Mostrar Usuarios")
        print("5. Mostrar Cola")
        print("6. Cerrar Secion")
        
        opcion = self.tratamiento()
        if(opcion == 0):
            print("Por favor intente co un numero del 1 al 9")
        return opcion 
        
        
    def validar_opcion_dos(self,opcion):
        if(opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6):
            return 1
        else:
            return 0
        
        
    def menu_3(self):
        
        print("Ingersando a Operaciones sobre la matriz")
        print("1. Ingresar Datos")
        print("2. Operar transpuesta")
        print("3. Mostrar matriz original")
        print("4. Mostrar matriz transpuesta")
        print("5. Regresa")
      
        opcion = self.tratamiento()
        if(opcion == 0):
            print("Por favor intente con un numero del 1 al 9\n")
        return opcion 
        
    def menu_4(self):
        print("Ingersando a Operaciones sobre la Cola")
        print("1. Operar")
        print("2. Regresar")
        
        opcion = self.tratamiento()
        if(opcion == 0):
            print("Por favor intente con un numero del 1 al 9")
        return opcion 