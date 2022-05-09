import numpy as np

listalexico = list()


pila = list()
lisreglas = list()
auxregl = list()
matrizreglas = list()

def reglas():
    file = open('compilador.lr', 'r')
    line = file.readlines()
    for l in line:
        l = l.rstrip()
        matrizreglas.append(l.split('\t'))

    for i in range (len(matrizreglas)):
        for j in range(len(matrizreglas[i])):
            matrizreglas[i][j] = int(matrizreglas[i][j])
    file.close()

def auxreglas():
    n = 1
    file = open('rgl.txt', 'r')
    line = file.readlines()
    for l in line:
        l = l.rstrip()
        auxregl.append(l.split('\t'))

    for obj in auxregl:
        #obj = Regla(int(obj[0]), int(obj[1]), str(obj[2]))
        obj = Regla(n, int(obj[0]), int(obj[1]), str(obj[2]))
        n+=1
        lisreglas.append(obj)
    file.close()

def buscar(str):
        for objlex in listalexico:
            if objlex.cad == str:
                return objlex
            else:
                pass

class Regla:
    def __init__(self, aux, num, elementos, regla):
        self.aux = aux
        self.num = num
        self.elementos = elementos
        self.regla = regla

    

class elementopila:
    def __init__(self, cadena, tipo, pos):
        self.cad = cadena
        self.tipo = tipo
        self.pos = pos

    def __repr__(self):
        return str(self.__dict__)

class terminal(elementopila):
    def __init__(self, cadena, tipo, pos):
        elementopila.__init__(self, cadena, tipo, pos)

class noterminal(elementopila):
    def __init__(self, cadena, tipo, pos):
        elementopila.__init__(self, cadena, tipo, pos)

class estado(elementopila):
    def __init__(self, cadena, tipo, pos, estado):
        elementopila.__init__(self, cadena, tipo, pos)
        self.estado = estado


class analizador:
    def __init__(self, cadena_para_analizar):
        self.cadena_analizada = cadena_para_analizar +"~"
        self.edo = 0
        self.i = 0
        self.tmp =""
        self.continua = True
        self.tipo=list()
        self.aux = 0
        

    def anlexico(self):
        
        while self.continua:
            c = self.cadena_analizada[self.i]
            
            if self.edo == 0:                                                   #General
                if c >= "0" and c <= "9":
                    self.edo = 1
                    self.tmp +=c
                    
                elif c == "E":
                    self.tmp +=c
                    self.tipo.append(3)
                    objlex = noterminal("E","E",self.tipo[-1])
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
                    objlex = terminal(self.tmp, 'Op. Mul', self.tipo[-1])
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
                        self.tipo.append(5)
                        objlex = terminal(self.tmp, 'Op. Suma', self.tipo[-1])
                        listalexico.append(objlex)
                        self.limpieza()

                    elif self.aux == 2:
                        
                        self.limpieza()
                    if c =="+":
                        self.tmp +=c
                        self.tipo.append(5)
                        objlex = terminal(self.tmp, 'Op. Suma', self.tipo[-1])
                        listalexico.append(objlex)
                        self.limpieza()
                        self.edo = 0
                    else:
                        self.tmp +=c
                        self.tipo.append(5)
                        objlex = terminal(self.tmp, 'Op. Suma', self.tipo[-1])
                        listalexico.append(objlex)
                        self.limpieza()
                        self.edo = 0

                elif c == ";":
                    self.tmp +=c
                    self.tipo.append(12)
                    objlex = terminal(self.tmp, 'Punto y coma', self.tipo[-1])
                    listalexico.append(objlex)
                    self.edo = 0
                
                elif c == ",":
                    self.tmp +=c
                    self.tipo.append(13)
                    objlex = terminal(self.tmp, 'Coma', self.tipo[-1])
                    listalexico.append(objlex)
                    self.edo = 0
                    
                
                elif c == "$":
                    self.tmp +=c
                    self.tipo.append(23)
                    objlex = terminal(self.tmp, 'Op. $', self.tipo[-1])
                    listalexico.append(objlex)
                    self.edo = 0
                elif c == "(":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = terminal(self.tmp, 'Parentesis', self.tipo[-1])
                    listalexico.append(objlex)
                    self.edo = 0
                    self.limpieza()
                elif c == ")":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = terminal(self.tmp, 'Parentesis', self.tipo[-1])
                    listalexico.append(objlex)
                    self.edo = 0

                elif c == "{":
                    self.tmp +=c
                    self.tipo.append(16)
                    objlex = terminal(self.tmp, 'Corchete', self.tipo[-1])
                    listalexico.append(objlex)
                    self.edo = 0
                    self.limpieza()
                elif c == "}":
                    self.tmp +=c
                    self.tipo.append(17)
                    objlex = terminal(self.tmp, 'Corchete', self.tipo[-1])
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
                    objlex = terminal(self.tmp, 'Entero', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
                    #self.tmp +=c

                elif c == "~":
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, 'Entero', self.tipo[-1])
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
                    objlex = terminal(self.tmp, 'Real', self.tipo[-1])
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
                    objlex = terminal(self.tmp, 'Op. Igualdad', self.tipo[-1])
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
                        objlex = terminal(self.tmp, 'Op. Igual', self.tipo[-1])
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
                        objlex = terminal(self.tmp, 'Op. Igual', self.tipo[-1])
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
                    objlex = terminal(self.tmp, 'Op. Relacional', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    self.edo = 0
                    #self.tmp +=c
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, 'Op. Relacional', self.tipo[-1])
                    listalexico.append(objlex)
                    #self.limpieza()
                    self.continua = False
                else:
                    self.edo = 0
                    #self.tmp +=c
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, 'Op. Relacional', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
                    self.i-=1

            elif self.edo == 7:                                 #Terminacion Simbolo
                if c == "|":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(8)
                    objlex = terminal(self.tmp, 'Op. Or', self.tipo[-1])
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
                    self.tipo.append(9)
                    objlex = terminal(self.tmp, 'Op. And', self.tipo[-1])
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
                    objlex = terminal(self.tmp, 'Cadena', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
                

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 9
                    self.tmp +=c
                    

            self.i+=1

        #print(self.edo)
        #print(self.cadena_analizada)
        #print(self.tmp)
        self.edo = 0
        self.i = 0
        self.tmp =""
        self.continua = True
        bandera =0

    def reservado(self):
        #if self.edo== 4:
            #print("es variable")
        strid = self.tmp
        if "while" == strid:
            self.tipo.append(20)
            objlex = terminal(self.tmp, 'Ciclo', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "if" == strid:
            self.tipo.append(19)
            objlex = terminal(self.tmp, 'Condicional', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "return" == strid:
            self.tipo.append(21)
            objlex = terminal(self.tmp, 'Retorno', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "else" == strid:
            self.tipo.append(22)
            objlex = terminal(self.tmp, 'Condicional', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "int" == strid:
            self.tipo.append(4)
            objlex = terminal(self.tmp, 'Tipo', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "float" == strid:
            self.tipo.append(4)
            objlex = terminal(self.tmp, 'Tipo', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        elif "void" == strid:
            self.tipo.append(4)
            objlex = terminal(self.tmp, 'Tipo', self.tipo[-1])
            listalexico.append(objlex)
            #print(strid, " Reservada Tipo", self.tipo[-1])
            #return True
        else:
            #print("es variable")
            self.tipo.append(0)
            objlex = terminal(self.tmp, 'Identificador', self.tipo[-1])
            listalexico.append(objlex)
            #return False
        #else:
           # pass
    def analizadorsintactico(self, i, auxelimna2, divcad2):
        while True:
            #print(pila)
            for obj in pila:
                try:
                    print(obj.cad, end='')
                except:
                    print(obj, end='')
            print(end='\t |')
            fila = pila[-1].pos
            
            columna = buscar(divcad2[i])
            accion = matrizreglas[fila][columna.pos]
            accion= estado(str(accion), accion, accion, accion)
            if accion.estado == 0:
                print('Error')
                break
            elif accion.estado > 0:
                i+=1
                pila.append(columna)
                pila.append(accion)
                print('Desplazamiento', accion.cad)
            elif accion.estado  <0:
                if accion.estado == -1:
                    print('R0')
                    break
                else:
                    #print('Regla')
                    for obj in lisreglas:
                        #if accion.estado == (obj.num -20) * -1:
                        if accion.estado == (obj.aux +1) * -1:
                            print('R'+str(obj.aux), obj.regla)
                            #print(obj.num, obj.regla)
                            accion = matrizreglas[fila][obj.num]
                            accion= estado(str(accion), accion, accion, accion)
                            if obj.elementos !=0:
                                eliminar = obj.elementos *2
                                while eliminar != 0:
                                    pila.pop()
                                    eliminar-=1
                                fila = pila[-1].pos
                                accion = matrizreglas[fila][obj.num]   
                                pila.append(obj.regla)
                                accion= estado(str(accion), accion, accion, accion)
                                pila.append(accion)
                            else:
                                pila.append(obj.regla)
                                pila.append(accion)
                            break
                        
                    #while auxelimna2 != 0:
                        #pila.pop()
                        #auxelimna2-=1
                    #divcad2[i-1]="E"
                    #i+=1
    
    def limpieza(self):
        self.edo = 0
        #self.i = 0
        self.tmp =""
        self.continua = True

    
                #print("No encontrado")



#print("Ingrese la cadena de caracteres a analizar")
#cad = input()
cad = "void menu(){\
        if (z < x)\
        {\
            x = 0;\
        }\
        }"
print("Cadena ingresada: ", cad)
divcad = cad.split()
divcad.append("$")

#divcad.append("E")
for i in range (len(divcad)):
    cadena = analizador(divcad[i])
    cadena.anlexico()

divcad2 = list()
print('------------------------')
#print("Leido        Tipo        Pos")
print('Leido', f"{'':>9}", 'Tipo', f"{'':>9}", 'Pos', f"{'':<9}")
for objlex in listalexico:
    print(objlex.cad, f"{'|':>11}", objlex.tipo, f"{'|':>9}", objlex.pos)
    divcad2.append(objlex.cad)
divcad.clear()    
divcad=divcad2
auxelimna = (len(divcad)-2)*2
fila = 0
columna = 0
accion =0
acept = False

#pila.append("$")
pila.append(buscar("$"))
pila.append(estado("0",0,0,0))

print('------------------------')
reglas()
auxreglas()
cadena.analizadorsintactico(0, auxelimna, divcad)
#for obj in lisreglas:
#    print(obj.aux, obj.num, obj.elementos, obj.regla)
#for obj in matrizreglas:
#    print(obj)

