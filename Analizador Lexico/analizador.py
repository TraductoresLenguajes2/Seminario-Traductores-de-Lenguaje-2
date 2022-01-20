
from unicodedata import decimal


class analizador:

    def __init__(self, cadena_para_analizar ):
        self.cadena_analizada = cadena_para_analizar
        self.identificador = list()
        self.entero= list()
        self.decimal = list()
        self.contador=0
        self.caracter=0
        self.numeros=0
        self.reales=0
        
    #Posibilidad de usar try, considerar escenario 1.23.4, considerar a strid para meterlo al init

    def lexico(self):
        for i in range(len(self.cadena_analizada)):
            self.caracter = ord(self.cadena_analizada[i])
            #print(str(i))
            if(self.cadena_analizada[i] == "+") or (self.cadena_analizada[i] == "-"):       #Operando Adicion
                if self.contador ==1:
                    strid= "".join(self.identificador)
                    print(strid, " Identificador")
                    self.limpieza()
                    print(self.cadena_analizada[i], "   Op. Adicion")
                else:
                    print(self.cadena_analizada[i], "   Op. Adicion")

            elif (self.caracter > 64 and self.caracter<91) or (self.caracter>96 and self.caracter<123):     #Letras
                if self.reales == 1:
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    self.identificador.append(self.cadena_analizada[i])
                    self.contador=1

                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    self.identificador.append(self.cadena_analizada[i])
                    self.contador=1

                else:
                    self.identificador.append(self.cadena_analizada[i])
                    self.contador=1

            elif (self.caracter > 47 and self.caracter < 58):                   #Numeros
                if self.contador ==1:
                    self.identificador.append(self.cadena_analizada[i])
                    strid= "".join(self.identificador)
                    print(strid, " Identificador")
                    self.limpieza()
                    #self.entero.append(self.cadena_analizada[i])
                    #self.numeros=1
                else:
                    self.numeros=1
                    self.entero.append(self.cadena_analizada[i])
            
            elif self.cadena_analizada[i] == ".":               #Punto Decimal
                if self.reales ==1:
                    print("Error, doble punto ingresado")  
                else:
                    self.decimal = self.entero
                    self.decimal.append(self.cadena_analizada[i])
                    self.reales = 1
                

            elif(self.cadena_analizada[i] == "*") or (self.cadena_analizada[i] == "/"):         #Operando Multiplicacion
                if self.contador ==1:
                    strid= "".join(self.identificador)
                    print(strid, " Identificador")
                    self.limpieza()
                    print(self.cadena_analizada[i], "   Op. Multiplicación")
                else:
                    print(self.cadena_analizada[i], "   Op. Multiplicación")


        #Comprobaciones Finales
        #Posibilidad de meter esto a otro metodo
        if self.contador==1:
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




                
                

                

print("Ingrese la cadena de caracteres a analizar")
cad = input()


print("Cadena ingresada: ", cad)

cadena = analizador(cad)

cadena.lexico()
