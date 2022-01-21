class analizador:

    def __init__(self, cadena_para_analizar ):
        self.cadena_analizada = cadena_para_analizar +"$"
        self.identificador = list()
        self.entero= list()
        self.decimal = list()
        self.simbolos = list()
        self.contador=0
        self.caracter=0
        self.numeros=0
        self.reales=0
        self.bandera =0
        self.i=0
        
    #Posibilidad de usar try

    def lexico(self):
        while True:
            self.caracter = ord(self.cadena_analizada[self.i])
    
            if self.cadena_analizada[self.i]=="$":
                
                break

            elif (self.caracter > 64 and self.caracter<91) or (self.caracter>96 and self.caracter<123):     #Letras
                if self.reales == 1:
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1

                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1

                else:
                    
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1

            elif (self.caracter > 47 and self.caracter < 58):                   #Numeros
                if self.contador ==1:
                    self.identificador.append(self.cadena_analizada[self.i])
                    strid= "".join(self.identificador)
                    print(strid, " Identificador")
                    self.limpieza()
                    
                else:
                    self.numeros=1
                    self.entero.append(self.cadena_analizada[self.i])
            
            elif self.cadena_analizada[self.i] == ".":               #Punto Decimal
                if self.reales ==1:
                    print("Error, doble punto ingresado")  
                else:
                    self.decimal = self.entero
                    self.decimal.append(self.cadena_analizada[self.i])
                    self.reales = 1

            elif self.cadena_analizada[self.i] == " ":
                pass
            else:
                print(self.cadena_analizada[self.i], "     Op. Invalido")
            self.i = self.i +1
                

        #Comprobaciones Finales
        #Posibilidad de meter esto a otro metodo
        if self.reales==1:
            strid= "".join(self.entero)
            print(strid, " Real")
            self.limpieza()

        elif self.contador==1:
            
            strid= "".join(self.identificador)
            print(strid, " Identificador")
            self.limpieza()

        elif self.numeros==1:
            strid= "".join(self.entero)
            print(strid, " Entero")
            self.limpieza()

    

            
            
    


    def limpieza(self):
        self.contador=0
        self.identificador.clear()
        self.numeros=0
        self.entero.clear()
        self.reales = 0
        self.decimal.clear()
        self.bandera =0
        self.simbolos.clear()


              
                

                

print("Ingrese la cadena de caracteres a analizar")
cad = input()


print("Cadena ingresada: ", cad)

cadena = analizador(cad)

cadena.lexico()
