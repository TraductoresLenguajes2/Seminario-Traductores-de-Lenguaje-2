import re
listaref = list()
globals()['contexto']=''
globals()['primera']=0
class codigo():
    def __init__(self):

        self.codigo = list()
        self.posicionvar = 4
        self.comienzo = 0
        self.codigoif = list()
    def traductor61012(self, bandera, code):
        self.bandera = bandera
        self.code = code


        if self.bandera == 6:
            self.codigo.append(str(self.code)+': db 0')

        if self.bandera == 10 or self.bandera == 12:
            if globals()['primera']==0:
                self.codigo.append('section .text \n')
                self.codigo.append('global '+str(self.code)+'\n')
                self.codigo.append('\n'+str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
                globals()['primera']=1
            else:
                patron = re.compile("[global]+")
                for indice in range(len(self.codigo)):
                    if patron.match(self.codigo[indice]) != None:

                        self.codigo[indice] = self.codigo[indice] + ', ' + str(self.code) 
                        break
                        
                    else:
                        pass
                self.codigo.append('\n'+str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
            globals()['contexto']= self.code   
    def traductor21(self, bandera, valor, var):
        self.bandera = bandera
        self.valor = valor
        self.var = var
        bandera = 0
        posicionaux =0
        #numeros
        if self.bandera == 21:

            for obj in listaref:
                if self.var == obj.var and obj.contexto == globals()['contexto']:
                    bandera = 1
                    posicionaux = obj.pos
                    break
                else:
                    bandera = 0
            if bandera ==1:
                self.codigo.append('\tMOV WORD [rbp -' + str(posicionaux)+'] , '+str(self.valor)+'\n')
            elif bandera == 0:
                self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , '+str(self.valor)+'\n')
                listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))
                self.posicionvar +=4
        #id de parametro
        if self.bandera == 22:

            for obj in listaref:
                if obj.var == self.valor:

                    self.codigo.append('\tMOV rax, QWORD [rbp -' + str(obj.pos)+']\n')
                    break
            self.codigo.append('\tMOV QWORD [rbp -' + str(self.posicionvar)+'] , rax \n\t')
            listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))

        #id
        if self.bandera == 23:

            self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , '+str(self.valor))
            listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))
            self.posicionvar +=4
    def traductorif(self, operacion, variables, banderaelse):
        self.operacion = operacion
        self.variables = variables
        self.encontrado = list()
        for obj in self.variables:
            for obj2 in listaref:
                if obj.cad == obj2.var:
                    self.encontrado.append(obj2)
                    break
        vuelta = 0
        for obj in self.encontrado:
            if vuelta == 0:
                self.codigo.insert(-2,'\tMOV ax, WORD[rbp -'+str(obj.pos) +']')
                vuelta+=1
            else:
                self.codigo.insert(-2,'\n\tMOV bx, WORD[rbp -'+str(obj.pos) +']')
                self.codigo.insert(-2,'\n\tCMP ax, bx')
                break
        if self.operacion.cad == '>':
            self.codigo.insert(-2,'\n\tjg if\n')
        elif self.operacion.cad == '<':
            self.codigo.insert(-2,'\n\tjl if\n')
        elif self.operacion.cad == '==':
            self.codigo.insert(-2,'\n\tjn if\n')
            
        #self.codigo.append('\nif:\n\t')
        auxiliar= self.codigo.pop(-2)
        self.codigo.insert(-1, auxiliar)
        self.codigoif.append('\nif:\n')
        aux = self.codigo.pop()
        self.codigoif.append(aux)
        self.codigoif.append('\tjmp regreso')
        self.codigo.append('regreso:\n\t')
        

    def traductoroperacion(self, bandera, var1, variables, contexto, num):
        self.bandera = bandera
        self.var1 = var1
        self.variables = variables
        self.contexto = contexto
        self.partederecha = num
        i =0
        contador = 0
        vuelta = 0
        bandera = 0
        banderarealizada = 0
        cad = 'MOV rax, '
        cad2 = 'MOV rdi, '
        banderadigito =0
        while contador < self.partederecha:
            for obj in self.variables:
                
                for obj2 in listaref:
                    if obj.cad == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['contexto'] or obj.cad.isdigit() and banderadigito==0:
                        if vuelta == 0:
                            if bandera ==0:
                                if obj.cad.isdigit():
                                    cad = cad + ''+obj.cad
                                    banderadigito=1
                                else:
                                    cad = cad + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad +'\n')
                            else:
                                if obj.cad.isdigit():
                                    cad2 = cad2 + ''+obj.cad
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                            i = 0
                            vuelta += 1
                            contador +=1
                            
                        else:
                            if bandera ==0:
                                if obj.cad.isdigit():
                                    cad2 = cad2 + ''+obj.cad
                                    
                                    
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                                vuelta += 1
                            else:
                                if self.bandera[0]=='+':
                                    self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                                self.bandera.pop(0)
                                #self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                banderarealizada= 1
                                vuelta -= 1
                                cad = 'MOV rax, '
                                cad2 = 'MOV rdi, '
                                cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')

                            #vuelta =0
                            
                                
                            i = 0
                            
                            contador +=1

                        if (vuelta ==2 or contador >= self.partederecha):
                            try:
                                if self.bandera[0]=='+':
                                    self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                                self.bandera.pop(0)
                            except:
                                pass
                            
                            vuelta = 0
                            bandera = 1
                            cad = 'MOV rax, '
                            cad2 = 'MOV rdi, '
                            break
                    else:
                        i+1
                        banderadigito=0
        '''
        
        for obj in self.variables:
            for obj2 in listaref:
                if obj.cad == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['contexto']:
                    if vuelta == 0:
                        cad = cad + 'QWORD [rbp -'+ str(obj2.pos)+']'
                        self.codigo.append('\t' + cad +'\n')
                        i = 0
                        vuelta = 1
                        break
                    else:
                        cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                        self.codigo.append('\t' + cad2+'\n')
                        i = 0
                else:
                    i+1
        '''
        #self.codigo.append('\t'+'ADD rax, rdi'+'\n')

        for obj in listaref:
            if self.var1 == obj.var and self.contexto == obj.contexto:
                self.codigo.append('\t''MOV QWORD [rbp -'+ str(obj.pos)+'], ' + 'rax\n')

    def parametros(self, cantidad, nombre):
        self.cantidad = cantidad
        self.nombre = nombre
        i =0
        if self.comienzo == 0:
            self.comienzo = self.posicionvar +20
        else:
            self.comienzo = self.comienzo
        while i < cantidad:
            self.codigo.append('MOV QWORD [rbp -' +str(self.comienzo)+'], rdi \n')
            listaref.append(referencia(self.nombre, globals()['contexto'], self.comienzo))
            i+=1
            self.comienzo+=4


    def traductorfunc(self):
        if globals()['contexto']=='main':
            self.codigo.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'MOV rax, 60 \n\t'+'MOV rdi, 0 \n\t' + 'syscall \n\t')
        else:
            self.codigo.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'POP rbp \n\t' + 'ret \n\t')
        self.posicionvar = 4
        self.comienzo = 0
        for obj in self.codigoif:
            self.codigo.append(obj)
    def traductorretorno(self, cad, contexto):
        self.cad = cad
        self.contexto = contexto
        for obj in listaref:
            if self.cad == obj.var and self.contexto == obj.contexto:
                self.codigo.append('MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')

    def llamadafuncion(self, enviados, llamado, nombre):
        self.enviados = enviados
        self.llamado = llamado
        self.nombre = nombre
        for obj in listaref:
            if self.enviados == obj.var and globals()['contexto'] == obj.contexto:
                self.codigo.append('\t''MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')
        self.codigo.append('\t''MOV rdi, rax')
        self.codigo.append('\n\t''call '+ str(nombre))
        for obj in listaref:
            if self.llamado == obj.var and globals()['contexto'] == obj.contexto:
                self.codigo.append('\n\t''MOV QWORD [rbp -'+ str(obj.pos)+'], rax\n\t')
    
    def funcionprint(self, valor):
        for obj in listaref:
            if obj.var == valor and globals()['contexto'] == obj.contexto:
                self.codigo.insert(0, 'section .data  \n\tprimr: db  "La impresion es := %lf",10,0 \nsection .bss \n\tresp: resq 2\n')
                self.codigo.insert(2, '\nextern printf\n')
                self.codigo.append('\n\tPUSH qword[rbp -'+str(obj.pos)+']')
                self.codigo.append('\n\tFILD dword[rsp]')
                self.codigo.append('\n\tFSTP qword[rel resp]')
                self.codigo.append('\n\tADD rsp, 8')
                self.codigo.append('\n\tMOVSD xmm0,qword[rel resp]')
                self.codigo.append('\n\tMOV rdi, primr')
                self.codigo.append('\n\tMOV al, 1')
                self.codigo.append('\n\tcall printf WRT ..plt \n\t')
    def codigotraducido(self):
        print('-----------------------------------')
        for obj in self.codigo:
            print(obj)
        Archivo=open("ensamblador.asm","w")
        for i in range(len(self.codigo)):
            Archivo.write(self.codigo[i])   
        del self.codigo[:]
        Archivo.close()

class referencia():
    def __init__(self, var, contexto, pos):
        self.var = var
        self.contexto = contexto
        self.pos = pos

    def __repr__(self):
        aux = ("Variable: "+str(self.var)+ " Contexto: "+str(self.contexto)+ " Pos: "+str(self.pos))
        return aux
