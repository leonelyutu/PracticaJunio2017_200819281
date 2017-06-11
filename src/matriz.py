class matriz():
    def __init__(self):
        self.filas = 0;
        self.columnas = 0;
        self.conteo = 0
        self.filas_t = 0
        self.columnas_t = 0
        self.M = []
        self.T = []
        
        
    def inicializar(self,filas,columnas):
        self.conteo = self.conteo +1
        
        self.filas = filas
        self.columnas = columnas
        
        for i in range(self.filas):
            self.M.append([0]*self.columnas)
        
     
            
    def inicializar_transpuesta(self):
        self.filas_t = self.columnas
        self.columnas_t = self.filas
       
        for i in range(self.filas_t):
            self.T.append([0]*self.columnas_t)
                 
    def llenar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.M[i][j] = int((raw_input("Introduzca un valor en la posicion (%d,%d): " %(i,j) )))

    def transpuesta(self):
        self.inicializar_transpuesta()
        for i in range(self.filas_t):
            for j in range(self.columnas_t):
                self.T[i][j] = self.M[j][i]
                    
    def imprimir_transpuesta(self):
         for i in range(len(self.T)):
            print "[",
            for j in range(len(self.T[i])):
                print'{:3>s}'.format(str(self.T[i][j])),
            print"]"
    
    def imprimir(self):
        for i in range(len(self.M)):
            print "[",
            for j in range(len(self.M[i])):
                print'{:3>s}'.format(str(self.M[i][j])),
            print"]"
        

    
    
