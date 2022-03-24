from asyncio.windows_events import NULL
from dataclasses import dataclass
from genericpath import exists
import numpy as np
from anytree import Node, RenderTree

listalexico = list()


pila = list()
lisreglas = list()
auxregl = list()
matrizreglas = list()
listavariables = list()
listavar = list()
listafunciones = list()
listadefiniciones = list()
listadefinicion = list()
listadefinicionarbol = list()
listaparametros = list()
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
root = Node(10)
globals()['bandera']=0
#actual = Node(5, parent=root)
class Nodo:
    def __init__(self, data):
        self.data = data
        #self.root = Node(10)
        #self.actual = Node
        self.contadordefinicion =0
        

class DefVar(Nodo):
    def __init__(self, data, tipo, lv):
        Nodo.__init__(self, data)
        self.tipo = tipo
        self.lv = lv
    def eliminaVar(self):
        pila.pop()
        pila.pop()
        pila.pop()
        self.lv = pila.pop()
        pila.pop()
        self.data = pila.pop()
        pila.pop()
        self.tipo = pila.pop()
        listavariables.append(DefVar(self.tipo, self.data, self.lv))
        globals()['actual']= Node(DefVar(self.tipo, self.data, self.lv), parent = root)
        #actual =Node(DefVar(self.tipo, self.data, self.lv), parent = root)
        '''
        if len(listaparametros)!=0:
             globals()['actual']= Node(DefVar(self.tipo, self.data, self.lv), parent = root)
             globals()['parametro'].parent = globals()['actual']
        else:
            globals()['actual']= Node(DefVar(self.tipo, self.data, self.lv), parent = root)
        '''
        if len(listavar)!=0:
            #print("no vacia")
            for i in range(len(listavar)):
               # print(i)
                auxiliar = listavar.pop(0)
                #rint(auxiliar.data)
                #print(self.tipo)
                auxiliar.data = self.tipo
                listavar.append(auxiliar)
                #globals()['actual']= Node(auxiliar, parent = root)
            
    def eliminalistaVar(self):
        pila.pop()
        pila.pop()
        pila.pop()
        self.data = pila.pop()
        pila.pop()
        pila.pop()
        listavariables.append(DefVar('Unknown ', self.data, self.lv))
        listavar.append(DefVar('Unknown ', self.data, self.lv))
    def __repr__(self):
        aux = ("Variable""\n \t \t \t" "Tipo: "+str(self.data.cad)+ " ID: "+str(self.tipo.cad)+ " Contexto:"+str(self.lv))
        return aux

class DefFunc(Nodo):
    def __init__(self, data, id, tipo):
        Nodo.__init__(self, data)
        self.id = id
        self.tipo = tipo

    def eliminaFunc(self):
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        id =pila.pop()
        pila.pop()
        tipo= pila.pop()
        listafunciones.append(DefFunc(self.data, id, tipo))
        if len(listaparametros)!=0:
             globals()['auxiliarFunc'] = Node(DefFunc(self.data, id, tipo), parent = root)
             for i in range (len(listaparametros)):
                auxiliar = listaparametros.pop()
                auxiliar.parent = globals()['auxiliarFunc']
             #globals()['parametro'].parent = globals()['auxiliarFunc']
             #globals()['auxiliarBlo'].parent =globals()['parametro']
             globals()['auxiliarBlo'].parent =auxiliar
        else:
            globals()['auxiliarFunc'] = Node(DefFunc(self.data, id, tipo), parent = root)
            globals()['auxiliarBlo'].parent = globals()['auxiliarFunc'] 


    def __repr__(self):
        aux = ("DefFunc""\n" "Tipo: "+str(self.tipo.cad)+ " ID: "+str(self.id.cad))
        return aux
class Parametros(Nodo):
    def __init__(self, data, id, tipo):
        Nodo.__init__(self, data)
        self.id = id
        self.tipo = tipo
    def eliminaPara(self):
        pila.pop()
        pila.pop()
        pila.pop()
        self.id = pila.pop()
        pila.pop()
        self.tipo= pila.pop()
        globals()['parametro'] = Node(Parametros(self.data, self.id, self.tipo), parent = root)
        listaparametros.append(globals()['parametro'])
        #actual = Node(DefLocal(self.data), parent = root)
    def eliminalistaPara(self):
        pila.pop()
        pila.pop()
        pila.pop()
        self.id = pila.pop()
        pila.pop()
        self.tipo= pila.pop()
        pila.pop()
        pila.pop()
        globals()['parametro'] = Node(Parametros(self.data, self.id, self.tipo), parent = root)
        listaparametros.append(globals()['parametro'])
        #actual = Node(DefLocal(self.data), parent = root)
    def __repr__(self):
        aux = ('Parametros' '\n'+ ' Tipo: '+str(self.tipo.cad)+' Id: '+str(self.id.cad))
        return aux
class DefLocal(Nodo):
    def __init__(self, data):
        Nodo.__init__(self, data)
        self.banderalocal=0

    def eliminaVar(self):
        pila.pop()
        pila.pop()
        print(self.banderalocal)
        if self.banderalocal==0:
            globals()['auxiliarLocal'] = Node(DefLocal(self.data), parent = root)
            globals()['actual'].parent = globals()['auxiliarLocal']
            if len(listavar)!=0:
                #print("no vacia2")
                for i in range(len(listavar)):
                    auxiliar = listavar.pop(0)
                    globals()['actual']= Node(auxiliar, parent = globals()['auxiliarLocal'])

            self.banderalocal=1
        else:
            globals()['actual'].parent = globals()['auxiliarLocal']
            
        #actual = Node(DefLocal(self.data), parent = root)
    def flagreset(self):
        self.banderalocal=0
    def eliminaSen(self):
        pila.pop()
        pila.pop()
    def __repr__(self):
        aux = ('DefLocal')
        return aux
#globals()['auxiliar45'] = 0 
class DefLocales(Nodo):
    def __init__(self, data):
        Nodo.__init__(self, data)
        self.banderalocal=0
    def eliminaDef(self):
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        if self.banderalocal == 0: 
            globals()['auxiliarLocales'] = Node(DefLocales(self.data), parent = root)
            globals()['auxiliarLocal'].parent = globals()['auxiliarLocales'] 
            self.banderalocal=1
        else:
            globals()['auxiliarLocal'].parent = globals()['auxiliarLocales'] 
          
        
    def __repr__(self):
        aux = ('DefLocales')
        return aux
class BloqFunc(Nodo):
    def __init__(self, data):
        Nodo.__init__(self, data)
    def eliminaBlo(self):
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        globals()['auxiliarBlo'] = Node(BloqFunc(self.data), parent = root)
        globals()['auxiliarLocales'].parent = globals()['auxiliarBlo'] 
    def __repr__(self):
        aux = ('BloqueFunc')
        return aux
class Argumentos(Nodo):
    pass
class LlamadaFunc(Nodo):
    pass
class Definicion(Nodo):
    def __init__(self, data, ultima):
        Nodo.__init__(self, data)
        self.ultima = ultima
    def eliminaDefVar(self):
        pila.pop()
        pila.pop()
        for obj in listavariables:
            if obj == self.ultima:
                globals()['auxiliarVar']= Node(Definicion(self.data, obj), parent = root)
                globals()['actual'].parent = globals()['auxiliarVar']
                listadefinicionarbol.append(globals()['auxiliarVar'])
                #print(obj)

                #globals()['auxiliarDefinicion'] = Node(Definicion(self.data, obj), parent = root)
                #globals()['auxiliarFunc'].parent = globals()['auxiliarDefinicion']
                #listadefinicionarbol.append(globals()['auxiliarDefinicion'])
                listadefinicion.append(obj)
    def eliminaDef(self):
        pila.pop()
        pila.pop()
        for obj in listafunciones:
            if obj == self.ultima:
                globals()['auxiliarDefinicion'] = Node(Definicion(self.data, obj), parent = root)
                globals()['auxiliarFunc'].parent = globals()['auxiliarDefinicion']
                listadefinicionarbol.append(globals()['auxiliarDefinicion'])
                #-------------------------------
                listadefinicion.append(obj)
                
                self.contadordefinicion+=1
                #USar 4 variables, solo esas
                #un if en las definiciones, por cada momento solo se podran manejar de a 4

    def __repr__(self):
        aux = ("Definicion")
        return aux

    



class Definiciones(Nodo):
    def __init__(self, data, ultimadef):
        Nodo.__init__(self, data)
        self.ultimadef = ultimadef
    def eliminaDefiniciones(self):
        
        pila.pop()
        pila.pop()
        pila.pop()
        pila.pop()
        definicion = self.ultimadef
        listadefiniciones.append(definicion)
        globals()['auxiliarDefiniciones'] = Node(Definiciones(self.data, definicion), parent = root)
        auxiliar= listadefinicionarbol.pop()
        auxiliar.parent = globals()['auxiliarDefiniciones'] 
    def __repr__(self):
        aux = ("Definiciones")
        return aux
class Programa(Nodo):
    def __init__(self, data):
        Nodo.__init__(self, data)

    def programaexitoso(self):
        pila.pop()
        pila.pop()
        root.name = "Programa"
class Termino(Nodo):
    pass
class Sentencia(Nodo):
    pass
class Expresion(Nodo):
    pass

class variable:
    def __init__(self, tipo, id, contexto):
        self.tipo = tipo
        self.id = id
        self.contexto = contexto
    def __repr__(self):
        aux = ("Tipo: "+str(self.tipo)+ " ID: "+str(self.id)+ " Contexto:"+str(self.contexto))
        return aux

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

listadeflocal= list()
listadeflocales= list()
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
                    self.limpieza()
                    self.edo = 0
                    
                
                elif c == ",":
                    self.tmp +=c
                    self.tipo.append(13)
                    objlex = terminal(self.tmp, 'Coma', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
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
                    self.limpieza()
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
                    self.limpieza()
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
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, 'Entero', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
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
                    
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    self.tipo.append(2)
                    objlex = terminal(self.tmp, 'Real', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
                    self.continua = False
                else:
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, 'Entero', self.tipo[-1])
                    listalexico.append(objlex)
                    self.limpieza()
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
                                self.buscaregla(obj.aux, eliminar)
                                #eliminar = obj.elementos *2
                                #while eliminar != 0:
                                #    pila.pop()
                                #    eliminar-=1
                                fila = pila[-1].pos
                                accion = matrizreglas[fila][obj.num]   
                                pila.append(obj.regla)
                                accion= estado(str(accion), accion, accion, accion)
                                pila.append(accion)
                            else:
                                pila.append(obj.regla)
                                pila.append(accion)
                            break
                        
                
    def buscaregla(self, num, cantidad):
        if num == 1:                        #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            programa = Programa('Data')
            programa.programaexitoso()
            #defvar = DefVar('Data','Data','Data')
            #defvar.eliminaVar()
        elif num == 3:                          #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            if len(listadefiniciones)==0:
                definiciones = Definiciones('Data', 'Data')
                definiciones.eliminaDefiniciones()
            else:
                definiciones = Definiciones('Data', listadefinicion[-1])
                definiciones.eliminaDefiniciones()
        elif num == 4:                              #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            #print('Estoy en regla 4')
            definicion = Definicion('Data',listavariables[-1])
            definicion.eliminaDefVar()
        elif num == 5:                              #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            if len(listafunciones)==0:
                print('Vacia')
                definicion = Definicion('Data')
                definicion.eliminaDef()
            else:
                #print('No Vacia')
                #print(listafunciones[-1])
                definicion = Definicion('Data', listafunciones[-1])
                definicion.eliminaDef()
            listadeflocal.clear()
            listadeflocales.clear()
        
        elif num == 6:                          #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            defvar = DefVar('Data','Data','Data')
            defvar.eliminaVar()
            #print('Variable Definida')
            '''
            while cantidad != 0:
                if cantidad ==3:
                    id = pila.pop().cad
                elif cantidad ==1:
                    tipo = pila.pop().cad
                else:
                   pila.pop()
                cantidad-=1
            contex=0
            listavariables.append(variable(tipo, id, contex))
            '''
        elif num == 8:
            defvar = DefVar('Data','Data','Data')
            defvar.eliminalistaVar()
        elif num == 9:                                                  #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            deffun =DefFunc('Data', 'ID', 'Tipo')
            deffun.eliminaFunc()
        elif num == 10:
            pass
        elif num == 11:                                             #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            defpara = Parametros('Data','Id','Tipo')
            defpara.eliminaPara()
        elif num == 12:
            pass
        elif num == 13:                                             #Hechaaaaaaaaaaaaaaaaaaaaaaaaa Casiiiiii
            defpara = Parametros('Data','Id','Tipo')
            defpara.eliminalistaPara()
        elif num == 14:                                                 #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            #listadeflocal.clear()
            bloquefun = BloqFunc('Data')
            bloquefun.eliminaBlo()
        elif num == 16:                                                 #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            if len(listadeflocales)==0:
                deflocales = DefLocales('Data')
                deflocales.eliminaDef()
                listadeflocales.append(deflocales)
            else:
                auxiliar = listadeflocales[-1]
                auxiliar.eliminaDef()
        elif num == 17:                                                 #Hechaaaaaaaaaaaaaaaaaaaaaaaaa
            if len(listadeflocal)==0:
                deflocal = DefLocal('Data')
                deflocal.eliminaVar()
                listadeflocal.append(deflocal)
            else:
                auxiliar = listadeflocal[-1]
                auxiliar.eliminaVar()
        elif num == 18:
            deflocal = DefLocal('Data')
            deflocal.eliminaSen()
        elif num == 20:
            pass
        elif num == 21:
            pass
        elif num == 23:
            pass
        elif num == 24:
            pass
        elif num == 28:
            pass
        elif num == 30:
            pass
        elif num == 32:
            pass
        elif num == 33:
            pass
        elif num == 34:
            pass
        elif num == 35:
            pass
        elif num == 36:
            pass
        elif num == 37:
            pass
        elif num == 38:
            pass
        elif num == 40:
            pass
        elif num == 47:
            pass
        elif num == 48:
            pass
        elif num == 52:
            pass

        else:
            while cantidad != 0:
                pila.pop()
                cantidad-=1
                                    
    def limpieza(self):
        self.edo = 0
        #self.i = 0
        self.tmp =""
        self.continua = True

    
                #print("No encontrado")



#print("Ingrese la cadena de caracteres a analizar")
#cad = input()
cad = "int main(){\
            int a, b, c, d;\
            float a;\
            int a;\
        }\
        void menu(){\
            int a, b, c, d;\
            float a;\
            int a;\
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

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
#aux = Nodo('Data')
#aux.imprimir()
'''
print('Variables')
for obj in listavariables:
    print(obj)
print('Funciones')
for obj in listafunciones:
    print(obj)
print('Definicion')
for obj in listadefinicion:
    print(obj)

print('Definiciones')
for obj in listadefiniciones:
    print(obj)
'''

#for obj in lisreglas:
#    print(obj.aux, obj.num, obj.elementos, obj.regla)