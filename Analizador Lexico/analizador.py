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
            
            
            if(self.cadena_analizada[self.i] == "+") or (self.cadena_analizada[self.i] == "-"):       #Operando Adicion
                if self.reales == 1:
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Adicion")
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Adicion")
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        print(strid, " Identificador")
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Adicion")
                else:
                    print(self.cadena_analizada[self.i], "   Op. Adicion")
            elif self.cadena_analizada[self.i]=="$":
                
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
                    self.csimbolos()  
                    self.identificador.append(self.cadena_analizada[self.i])
                    self.contador=1

            elif (self.caracter > 47 and self.caracter < 58):                   #Numeros
                if self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
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
                

            elif(self.cadena_analizada[self.i] == "*") or (self.cadena_analizada[self.i] == "/"):         #Operando Multiplicacion
                if self.reales == 1:
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        print(strid, " Identificador")
                    self.limpieza()
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")
                else:
                    print(self.cadena_analizada[self.i], "   Op. Multiplicación")

            elif(self.cadena_analizada[self.i] == "="):         #Operando Asignacion
                if self.reales == 1:
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    self.simbigual()
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    self.simbigual()
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        print(strid, " Identificador")
                    self.limpieza()
                    self.simbigual()
                else:
                    self.simbigual()
            

            elif(self.cadena_analizada[self.i] == "<") or (self.cadena_analizada[self.i] == ">") or (self.cadena_analizada[self.i] == "!"):    #Operando Relacional
                if self.reales == 1:
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    self.csim()
                    
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    self.csim()
                    
                elif self.contador ==1:
                    if self.reservadas():
                        pass
                    else:
                        strid= "".join(self.identificador)
                        print(strid, " Identificador")
                    self.limpieza()
                    self.csim()
                    
                else:
                    
                    
                    self.csim()
                    

            elif(self.cadena_analizada[self.i] == "&"):         #Operando And
                if self.reales == 1:
                    self.csimbolos()
                    strid= "".join(self.entero)
                    print(strid, " Real")
                    self.limpieza()
                    self.simbolos.append(self.cadena_analizada[self.i])
                    
                elif self.numeros ==1:
                    self.csimbolos()
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    self.simbolos.append(self.cadena_analizada[self.i])

                elif self.contador ==1:
                    self.csimbolos()
                    strid= "".join(self.identificador)
                    print(strid, " Identificador")
                    self.limpieza()   
                    self.simbolos.append(self.cadena_analizada[self.i])
                    
                else:
                    if len(self.simbolos) !=0:
                        if self.simbolos[-1] == self.cadena_analizada[self.i]:
                            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i], "   Op. And")
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
                    print(strid, " Real")
                    self.limpieza()
                    
                elif self.numeros ==1:
                    strid= "".join(self.entero)
                    print(strid, " Entero")
                    self.limpieza()
                    
                elif self.contador ==1:
                    self.csimbolos()
                    strid= "".join(self.identificador)
                    print(strid, " Identificador")
                    self.limpieza()
                    self.simbolos.append(self.cadena_analizada[self.i])
                    
                else:
                    if len(self.simbolos) !=0:
                        if self.simbolos[-1] == self.cadena_analizada[self.i]:
                            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i], "   Op. Or")
                            self.limpieza()
                        else:
                            self.csimbolos()
                            self.simbolos.append(self.cadena_analizada[self.i])
                            

                    
                    else:
                        self.simbolos.append(self.cadena_analizada[self.i])

                        continue
            elif (self.cadena_analizada[self.i]=="(") or (self.cadena_analizada[self.i]==")"):
                print(self.cadena_analizada[self.i], "   Parentesis")
            elif (self.cadena_analizada[self.i]=="{") or (self.cadena_analizada[self.i]=="}"):
                print(self.cadena_analizada[self.i], "   Llave")
            elif (self.cadena_analizada[self.i]==";"):
                print(self.cadena_analizada[self.i], "   Punto y coma")
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
            if self.reservadas():
                pass
            else:
                strid= "".join(self.identificador)
                print(strid, " Identificador")
                self.limpieza()

        elif self.numeros==1:
            strid= "".join(self.entero)
            print(strid, " Entero")
            self.limpieza()

        elif len(self.simbolos) != 0:
            print(self.cadena_analizada[self.i], "   Op. No valido")

            
            
    def csimbolos(self):
        if len(self.simbolos) !=0:
            strid= "".join(self.simbolos)
            print(strid, "   Op. No valido")
            self.limpieza()
            
    def csim(self):
        if(self.cadena_analizada[self.i+1]=="="):
            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i+1], "   Op. Relacional")
            self.i = self.i+1
            
                    
        else:
            if self.cadena_analizada[self.i]=="!":
                print(self.cadena_analizada[self.i], "   Op. Not")
            else:
                print(self.cadena_analizada[self.i], "   Op. Relacional")

    def simbigual(self):
        if(self.cadena_analizada[self.i+1]=="="):
            print(self.cadena_analizada[self.i] + self.cadena_analizada[self.i+1], "   Op. Asignación")
            self.i=self.i+1
                        
        else:
            print(self.cadena_analizada[self.i], "   Op. Asignación")


    def limpieza(self):
        self.contador=0
        self.identificador.clear()
        self.numeros=0
        self.entero.clear()
        self.reales = 0
        self.decimal.clear()
        self.bandera =0
        self.simbolos.clear()

    def reservadas(self):
        #print(self.identificador)
        strid= "".join(self.identificador)
        #print(strid)
        if "while" in strid:
            print(strid, "  Reservada")
            return True
        elif "if" in strid:
            print(strid, "  Reservada")
            return True
        elif "return" in strid:
            print(strid, "  Reservada")
            return True
        elif "else" in strid:
            print(strid, "  Reservada")
            return True
        elif "int" in strid:
            print(strid, "  Reservada")
            return True
        elif "float" in strid:
            print(strid, "  Reservada")
            return True
        else:
            
            return False




                
                

                

print("Ingrese la cadena de caracteres a analizar")
cad = input()


print("Cadena ingresada: ", cad)

cadena = analizador(cad)

cadena.lexico()
