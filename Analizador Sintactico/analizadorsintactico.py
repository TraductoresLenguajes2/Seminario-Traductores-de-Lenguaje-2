import numpy as np

listalexico = list()
import numpy as np
tabla3 = [2, 0, 0, 1],\
        [0, 0, -1, 0],\
        [0, 3, -3, 0],\
        [2, 0, 0, 4],\
        [0, 0, -2, 0]
tbl2 = np.array(tabla3)



tabla2 = [2, 0, 0, 1],\
        [0, 0, -1, 0],\
        [0, 3, 0, 0],\
        [4, 0, 0, 0],\
        [0, 0, -2, 0]
tbl = np.array(tabla2)

lr = [2, 0, 1],\
     [0, -1, 0],\
     [0, -2, 0]

lrt = np.array(lr)

pila = list()

class lexico:
    def __init__(self, cadena, tipo, pos):
        self.cad = cadena
        self.tipo = tipo
        self.pos = pos

class analizador:
    def __init__(self, cadena_para_analizar):
        self.cadena_analizada = cadena_para_analizar +"~"
        self.edo = 0
        self.i = 0
        self.tmp =""
        self.continua = True
        self.tipo=list()
        self.aux = 0
        

    def lexico(self):
        
        while self.continua:
            c = self.cadena_analizada[self.i]
            
            if self.edo == 0:                                                   #General
                if c >= "0" and c <= "9":
                    self.edo = 1
                    self.tmp +=c
                
                elif c == "E":
                    self.tmp +=c
                    self.tipo.append(3)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.continua = False

                elif c >= "a" and c <= "z" or c >= "A" and c <= "Z" or c == "_":
                    self.edo = 4
                    self.tmp += c
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "'" or c=='"':
                    self.edo = 9
                    self.tmp +=c

                elif (c == "*") or (c == "/"):
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(6)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()

                elif (c == "=") or (c == "!"):    #Simbolos
                    self.limpieza()
                    self.edo = 5
                    self.tmp +=c
                
                elif (c == "<") or (c == ">"):    #Simbolos
                    self.limpieza()
                    self.edo = 6
                    self.tmp +=c
                elif (c == "|"):    #Simbolos
                    self.limpieza()
                    self.edo = 7
                    self.tmp +=c
                elif (c == "&"):    #Simbolos
                    self.limpieza()
                    self.edo = 8
                    self.tmp +=c

                
                elif (c == "+") or (c == "-"):
                    if self.aux == 1:
                        self.tipo.append(1)
                        objlex = lexico(self.tmp, self.tipo[-1], 0)
                        listalexico.append(objlex)
                        self.limpieza()

                    elif self.aux == 2:
                        
                        self.limpieza()
                    if c =="+":
                        self.tmp +=c
                        self.tipo.append(1)
                        objlex = lexico(self.tmp, self.tipo[-1], 0)
                        listalexico.append(objlex)
                        self.limpieza()
                        self.edo = 0
                    else:
                        self.tmp +=c
                        self.tipo.append(5)
                        objlex = lexico(self.tmp, self.tipo[-1], 0)
                        listalexico.append(objlex)
                        self.limpieza()
                        self.edo = 0
                    
                
                elif c == "$":
                    self.tmp +=c
                    self.tipo.append(2)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.edo = 0
                elif c == "(":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.edo = 0
                    self.limpieza()
                elif c == ")":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.edo = 0

                elif c == "{":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.edo = 0
                    self.limpieza()
                elif c == "}":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.edo = 0
                    

                
                elif c == "~":
                    self.continua=False
                
            elif self.edo == 1:                                     #Numeros
                if c >= "0" and c <= "9":
                    self.edo = 1
                    self.tmp +=c

                elif c == ".":
                    self.edo = 2
                    self.tmp += c

                elif c == " ":
                    self.edo = 0
                    self.tipo.append(1)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                    #self.tmp +=c

                elif c == "~":
                    self.tipo.append(1)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.continua = False
                else:
                    self.edo = 0
                    self.aux = 1
                    self.i-=1

            elif self.edo == 2:                                 #Float
                if c >= "0" and c <= "9":
                    self.edo = 3
                    self.tmp +=c
            
            elif self.edo == 3:                                 #Terminacion Num
                if c >= "0" and c <= "9":
                    self.edo = 3
                    self.tmp +=c
                    self.tipo.append(2)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 0
                    self.i-=1

            elif self.edo == 4:                                                                         #Letras
                if c >= "a" and c <= "z" or c >= "A" and c <= "Z" or c == "_" or c >= "0" and c <= "9":
                    self.edo = 4
                    self.tmp +=c
                elif c == " ":
                    self.reservado()
                    self.limpieza()
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    self.reservado()
                    self.continua = False
                else:
                    self.reservado()
                    self.edo = 0
                    self.limpieza()
                    self.i-=1
                    self.aux=2
            
            elif self.edo == 5:                                 #Terminacion Simbolo
                if c == "=":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(11)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    if self.cadena_analizada[self.i-1]=="=":
                        self.edo = 0
                        #self.tmp +=c
                        self.tipo.append(18)
                        objlex = lexico(self.tmp, self.tipo[-1], 0)
                        listalexico.append(objlex)
                        self.limpieza()
                    else:
                        self.limpieza()
                    self.continua = False
                else:
                    if self.cadena_analizada[self.i-1]=="=":
                        self.edo = 0
                        #self.tmp +=c
                        self.tipo.append(18)
                        objlex = lexico(self.tmp, self.tipo[-1], 0)
                        listalexico.append(objlex)
                        self.limpieza()
                    else:
                        self.limpieza()
                    self.i-=1

            elif self.edo == 6:                                 #Terminacion Simbolo
                if c == "=":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(7)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    self.edo = 0
                    #self.tmp +=c
                    self.tipo.append(7)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    #self.limpieza()
                    self.continua = False
                else:
                    self.edo = 0
                    #self.tmp +=c
                    self.tipo.append(7)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                    self.i-=1

            elif self.edo == 7:                                 #Terminacion Simbolo
                if c == "|":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(7)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 0
                    self.limpieza()
                    self.i-=1

            elif self.edo == 8:                                 #Terminacion Simbolo
                if c == "&":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(7)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 0
                    self.limpieza()
                    self.i-=1
            
            elif self.edo == 9:                                 #Terminacion Simbolo
                if c == "'" or c == '"':
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(3)
                    objlex = lexico(self.tmp, self.tipo[-1], 0)
                    listalexico.append(objlex)
                    self.limpieza()
                

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 9
                    self.tmp +=c
                    

            self.i+=1

        print(self.edo)
        print(self.cadena_analizada)
        print(self.tmp)
        self.edo = 0
        self.i = 0
        self.tmp =""
        self.continua = True
        bandera =0
        '''
        if self.edo== 1:
            print("es entero")
            
        elif self.edo== 2:
            print("es float")
        '''
    def reservado(self):
        #if self.edo== 4:
            #print("es variable")
        strid = self.tmp
        if "while" == strid:
            self.tipo.append(20)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "if" == strid:
            self.tipo.append(19)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "return" == strid:
            self.tipo.append(21)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "else" == strid:
            self.tipo.append(22)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "int" == strid:
            self.tipo.append(4)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "float" == strid:
            self.tipo.append(4)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "void" == strid:
            self.tipo.append(4)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        else:
            #print("es variable")
            self.tipo.append(0)
            objlex = lexico(self.tmp, self.tipo[-1], 0)
            listalexico.append(objlex)
            #return False
        #else:
           # pass
    
    def limpieza(self):
        self.edo = 0
        #self.i = 0
        self.tmp =""
        self.continua = True

    def buscar(self, str):
        for objlex in listalexico:
            if objlex.cad == str:
                return objlex.tipo
            else:
                pass
                #print("No encontrado")



print("Ingrese la cadena de caracteres a analizar")
cad = input()

print("Cadena ingresada: ", cad)
divcad = cad.split()
divcad.append("$")

divcad.append("E")
for i in range (len(divcad)):
    cadena = analizador(divcad[i])
    cadena.lexico()

divcad2 = list()
print('------------------------')
print("Leido        Tipo        Pos")
for objlex in listalexico:
    print(objlex.cad, f"{'':>9}", objlex.tipo, f"{'':>9}", objlex.pos)
    divcad2.append(objlex.cad)
divcad.clear()    
divcad=divcad2
auxelimna = (len(divcad)-2)*2
fila = 0
columna = 0
accion =0
acept = False

pila.append("$")
pila.append(0)



i=0
    
while True:
    fila = pila[-1]
    columna = cadena.buscar(divcad[i])
    accion = tbl2[fila,columna]
    #pila.append(columna)
    #pila.append(accion)
    if accion == 0:
        print('Error')
        break
    elif accion > 0:
        i+=1
        pila.append(columna)
        pila.append(accion)
        print('Desplazamiento')
    elif accion  <0:
        if accion == -1:
            print('Aceptado')
            break
        else:
            print('Regla')
            while auxelimna != 0:
                pila.pop()
                auxelimna-=1
            divcad[i-1]="E"
            i-=1
'''

print("Ingrese la cadena de caracteres a analizar")
cad = input()

print("Cadena ingresada: ", cad)
divcad = cad.split()

print("Cadena dividida: ", divcad)
for i in range (len(divcad)):
    cadena = analizador(divcad[i])
    cadena.lexico()
print('------------------------')
print("Leido        Tipo        Pos")
for objlex in listalexico:
    print(objlex.cad, f"{'':>9}", objlex.tipo, f"{'':>9}", objlex.pos )
    #f"{'':<20}", formato2, f"{'':>9}"
'''
