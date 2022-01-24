

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
        self.tipo=list()
        self.escadena=0
        self.cadena =list()
        self.veces=0
        
    #Limpiar codigo, probar si la solucion usada en los != funciona en los and y eso

    def lexico(self):
        while True:
            self.caracter = ord(self.cadena_analizada[self.i])
            
            if self.cadena_analizada[self.i]=="$":
                #self.tipo.append(23)
                #print(self.cadena_analizada[self.i], " Reservada Tipo", self.tipo[-1])
                break
            elif(self.cadena_analizada[self.i] == "+") or (self.cadena_analizada[self.i] == "-"):       #Operando Adicion
                if self.reales == 1:
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    self.tipo.append(5)
                    print(self.cadena_analizada[self.i], "   Op. Adicion Tipo", self.tipo[-1])
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    self.tipo.append(5)
                    print(self.cadena_analizada[self.i], "   Op. Adicion Tipo", self.tipo[-1])
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        self.tipo.append(0)
                        strid= "".join(self.identificador)
                        print(strid, " Identificador Tipo", self.tipo[-1])

                    self.limpieza()
                    self.tipo.append(5)
                    print(self.cadena_analizada[self.i], "   Op. Adicion Tipo", self.tipo[-1])
                else:
                    self.tipo.append(5)
                    print(self.cadena_analizada[self.i], "   Op. Adicion Tipo", self.tipo[-1])
            

            elif (self.caracter > 64 and self.caracter<91) or (self.caracter>96 and self.caracter<123):     #Letras
                if self.reales == 1:
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1

                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1
                elif self.escadena==1:
                    self.cadena.append(self.cadena_analizada[self.i])
                    self.veces =1
                
                else:
                    self.csimbolos()  
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1 

            elif(self.cadena_analizada[self.i]=='"') or (self.cadena_analizada[self.i]=="'"):   #Comillas para cadenas
                if self.veces!=1:
                    self.escadena=1
                else:
                    #self.identificador.append(self.cadena_analizada[self.i])
                    strid= "".join(self.cadena)
                    self.tipo.append(3)
                    print(strid, " Cadena Tipo", self.tipo[-1])
                    self.limpieza()
                    self.veces=0
                    self.escadena=2
            

            elif (self.caracter > 47 and self.caracter < 58):                   #Numeros
                if self.contador ==1:
                    #En caso de querer evitar identificadores del tipo "while1" ajustar sangria
                    #if self.reservadas():
                     #   pass
                    #else:
                    self.identificador.append(self.cadena_analizada[self.i])
                    strid= "".join(self.identificador)
                    self.tipo.append(0)
                    print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()         #No mover
                    
                    
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
                

            elif(self.cadena_analizada[self.i] == "*") or (self.cadena_analizada[self.i] == "/"):         #Operando Multiplicacion
                if self.reales == 1:
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        self.tipo.append(0)
                    print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")
                else:
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")

            elif(self.cadena_analizada[self.i] == "="):         #Operando Asignacion
                if self.reales == 1:
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    self.simbigual()
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    self.simbigual()
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        self.tipo.append(0)
                    print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()
                    self.simbigual()
                else:
                    self.simbigual()
            

            elif(self.cadena_analizada[self.i] == "<") or (self.cadena_analizada[self.i] == ">") or (self.cadena_analizada[self.i] == "!"):    #Operando Relacional
                if self.reales == 1:
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    self.csim()
                    
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    self.csim()
                    
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        self.tipo.append(0)
                        print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()
                    self.csim()
                    
                else:
                    
                    
                    self.csim()
                    

            elif(self.cadena_analizada[self.i] == "&"):         #Operando And
                if self.reales == 1:
                    self.csimbolos()
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    self.simbolos.append(self.cadena_analizada[self.i])
                    
                elif self.numeros ==1:
                    self.csimbolos()
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    self.simbolos.append(self.cadena_analizada[self.i])

                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        self.tipo.append(0)
                        print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()   
                    self.simbolos.append(self.cadena_analizada[self.i])
                    
                else:
                    if len(self.simbolos) !=0:
                        if self.simbolos[-1] == self.cadena_analizada[self.i]:
                            self.tipo.append(9)
                            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i], "   Op. And Tipo", self.tipo[-1])
                            self.limpieza()
                        else:
                            self.csimbolos()                           
                            self.simbolos.append(self.cadena_analizada[self.i])

                    else:
                        self.simbolos.append(self.cadena_analizada[self.i])
                        
                        continue
                    

            elif(self.cadena_analizada[self.i] == "|"):         #Operando Or
                if self.reales == 1:
                    strid= "".join(self.entero)
                    self.tipo.append(2)
                    print(strid, " Real Tipo", self.tipo[-1])
                    self.limpieza()
                    
                    
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    self.tipo.append(1)
                    print(strid, " Entero Tipo", self.tipo[-1])
                    self.limpieza()
                    
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        self.tipo.append(0)
                        print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()
                    self.simbolos.append(self.cadena_analizada[self.i])
                    
                else:
                    if len(self.simbolos) !=0:
                        if self.simbolos[-1] == self.cadena_analizada[self.i]:
                            self.tipo.append(8)
                            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i], "   Op. Or Tipo", self.tipo[-1])
                            self.limpieza()
                        else:
                            self.csimbolos()
                            self.simbolos.append(self.cadena_analizada[self.i])
 
                    else:
                        self.simbolos.append(self.cadena_analizada[self.i])
                        continue

            elif (self.cadena_analizada[self.i]=="("):  #Simbolos restantes   
                if self.numletras():
                    self.tipo.append(14)
                    print(self.cadena_analizada[self.i], "   Parentesis Tipo", self.tipo[-1])
                else:
                    self.tipo.append(14)
                    print(self.cadena_analizada[self.i], "   Parentesis Tipo", self.tipo[-1])

            elif (self.cadena_analizada[self.i]==")"):
                self.tipo.append(15)
                print(self.cadena_analizada[self.i], "   Parentesis Tipo", self.tipo[-1])

            elif (self.cadena_analizada[self.i]=="{") :
                if self.numletras():
                    self.tipo.append(16)
                    print(self.cadena_analizada[self.i], "   Llave Tipo", self.tipo[-1])
                else:
                    self.tipo.append(16)
                    print(self.cadena_analizada[self.i], "   Llave Tipo", self.tipo[-1])


            elif (self.cadena_analizada[self.i]=="}"):
                if self.numletras():
                    self.tipo.append(17)
                    print(self.cadena_analizada[self.i], "   Llave Tipo", self.tipo[-1])
                else:
                    self.tipo.append(17)
                    print(self.cadena_analizada[self.i], "   Llave Tipo", self.tipo[-1])
            elif (self.cadena_analizada[self.i]==";"):
                if self.numletras():
                    self.tipo.append(12)
                    print(self.cadena_analizada[self.i], "   Punto y coma Tipo" , self.tipo[-1])
                else:
                    self.tipo.append(12)
                    print(self.cadena_analizada[self.i], "   Punto y coma Tipo" , self.tipo[-1])

            elif self.cadena_analizada[self.i] == " ":  #Espacio
                if self.contador ==1:
                    if self.reservadas():
                        pass
                    
                    else:
                        self.identificador.append(self.cadena_analizada[self.i])
                        strid= "".join(self.identificador)
                        self.tipo.append(0)
                        print(strid, " Identificador Tipo", self.tipo[-1])
                    self.limpieza()
                if self.escadena ==1:
                    strid= "".join(self.cadena)
                    print(strid,"   Invalido, falta cierre")
                    self.veces=0
                    self.limpieza()
                    self.escadena=2


            else:
                print(self.cadena_analizada[self.i], "     Op. Invalido")

            self.i = self.i + 1  #Aumentamos contador

           


        
        
        self.comprobaciones()
    #Comprobaciones Finales antes de terminar el analisis
    def comprobaciones(self):
        if self.reales==1:
            strid= "".join(self.entero)
            self.tipo.append(2)
            print(strid, " Real Tipo", self.tipo[-1])
            self.limpieza()

        elif self.contador==1:
            if self.reservadas():
                pass
            else:
                strid= "".join(self.identificador)
                self.tipo.append(0)
                print(strid, " Identificador Tipo", self.tipo[-1])
                self.limpieza()

        elif self.numeros==1:
            strid= "".join(self.entero)
            self.tipo.append(1)
            print(strid, " Entero Tipo", self.tipo[-1])
            self.limpieza()

        elif len(self.simbolos) != 0:
            print(self.cadena_analizada[self.i], "   Op. No valido")
        self.tipo.append(23)
        print(self.cadena_analizada[self.i], " Reservada Tipo", self.tipo[-1])

    #Comprobacion acerca de las posibilidades anteriores a los simbolos
    def numletras(self):
        if self.reales == 1:
            strid= "".join(self.entero)
            self.tipo.append(2)
            print(strid, " Real Tipo", self.tipo[-1])
            self.limpieza()
                    
                    
        elif self.numeros ==1:
            strid= "".join(self.entero)
            self.tipo.append(1)
            print(strid, " Entero Tipo", self.tipo[-1])
            self.limpieza()
                    
        elif self.contador ==1:
            if self.reservadas():
                pass
            else:
                strid= "".join(self.identificador)
                self.tipo.append(0)
                print(strid, " Identificador Tipo", self.tipo[-1])
            self.limpieza()
        
    #Rechazar simbolos que no son validos (Posibilidad de remover)        
    def csimbolos(self):
        if len(self.simbolos) !=0:
            strid= "".join(self.simbolos)
            print(strid, "   Op. No valido")
            self.limpieza()
    #Comprobador de simbolos concatenados        
    def csim(self):
        if(self.cadena_analizada[self.i+1]=="="):
            self.tipo.append(7)
            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i+1], "   Op. Relacional Tipo", self.tipo[-1])
            self.i = self.i+1       
        else:
            if self.cadena_analizada[self.i]=="!":
                self.tipo.append(10)
                print(self.cadena_analizada[self.i], "   Op. Not Tipo", self.tipo[-1])
            else:
                self.tipo.append(7)
                print(self.cadena_analizada[self.i], "   Op. Relacional Tipo", self.tipo[-1])

    #Comprobar si son 2 simbolos de igual o uno solo
    def simbigual(self):
        if(self.cadena_analizada[self.i+1]=="="):
            self.tipo.append(11)
            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i+1], "   Op. Asignación Tipo", self.tipo[-1])
            self.i=self.i+1
                        
        else:
            self.tipo.append(11)
            print(self.cadena_analizada[self.i], "   Op. Asignación Tipo", self.tipo[-1])

    #Limpiar listas y contadores auxiliares
    def limpieza(self):
        self.contador=0
        self.identificador.clear()
        self.numeros=0
        self.entero.clear()
        self.reales = 0
        self.decimal.clear()
        self.bandera =0
        self.simbolos.clear()
        self.cadena.clear()

    #Comprobar si el identificador no es una palabra reservada
    def reservadas(self):
        strid= "".join(self.identificador)
        if "while" == strid:
            self.tipo.append(20)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        elif "if" == strid:
            self.tipo.append(19)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        elif "return" == strid:
            self.tipo.append(21)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        elif "else" == strid:
            self.tipo.append(22)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        elif "int" == strid:
            self.tipo.append(4)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        elif "float" == strid:
            self.tipo.append(4)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        elif "void" == strid:
            self.tipo.append(4)
            print(strid, " Reservada Tipo", self.tipo[-1])
            return True
        else:
            return False


                
                
#Inicio del programa
print("Ingrese la cadena de caracteres a analizar")
cad = input()


print("Cadena ingresada: ", cad)

cadena = analizador(cad)

cadena.lexico()
