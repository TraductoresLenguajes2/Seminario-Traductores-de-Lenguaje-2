import re
listaref = list()
globals()['contexto']=''
globals()['primera']=0
class codigo():
    def __init__(self):
        #self.bandera = bandera
        #self.codigo = codigo
        self.codigo = list()
        self.posicionvar = 4
        self.comienzo = 0
    def traductor61012(self, bandera, code):
        self.bandera = bandera
        self.code = code


        if self.bandera == 6:
            #print('Es una def var ' + str(self.code)) 
            self.codigo.append(str(self.code)+': db 0')

        if self.bandera == 10 or self.bandera == 12:
            if globals()['primera']==0:
                self.codigo.append('section.text \n')
                self.codigo.append('global '+str(self.code)+'\n')
                self.codigo.append(str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
                globals()['primera']=1
            else:
                patron = re.compile("[global]+")
                for indice in range(len(self.codigo)):
                    if patron.match(self.codigo[indice]) != None:
                        print(patron.search('global'))
                        print('siiiii')
                        #indice = self.codigo.index(obj)
                        #self.codigo.append
                        self.codigo[indice] = self.codigo[indice] + ', ' + str(self.code)
                        break
                        
                    else:
                        #self.codigo[indice] = self.codigo[indice] 
                        print("Sin coincidencias")
                self.codigo.append(str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
            globals()['contexto']= self.code   
    def traductor21(self, bandera, valor, var):
        self.bandera = bandera
        self.valor = valor
        self.var = var
        #numeros
        if self.bandera == 21:
            #print('Regla 211111')
            print(self.valor)
            print(self.var)
            #print('Es una def var ' + str(self.code)) 
            self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , 0x'+str(self.valor))
            listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))
            self.posicionvar +=4
        #id de parametro
        if self.bandera == 22:
            print('Regla 22')
            for obj in listaref:
                if obj.var == self.valor:

                    self.codigo.append('\tMOV rax, QWORD [rbp -' + str(obj.pos)+']')
                    break
            self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , rax')
            listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))
            '''
            print(self.valor)
            print(self.var)
            #print('Es una def var ' + str(self.code)) 
            self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , 0x'+str(self.valor))
            listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))
            self.posicionvar +=4
            '''
        #id
        if self.bandera == 23:
            #print('Regla 211111')
            print(self.valor)
            print(self.var)
            #print('Es una def var ' + str(self.code)) 
            self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , 0x'+str(self.valor))
            listaref.append(referencia(self.var, globals()['contexto'], self.posicionvar))
            self.posicionvar +=4

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
        
        while contador < self.partederecha:
            for obj in self.variables:
                for obj2 in listaref:
                    if obj.cad == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['contexto']:
                        if vuelta == 0:
                            if bandera ==0:
                                cad = cad + 'WORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad +'\n')
                            else:
                                cad2 = cad2 + 'WORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                            i = 0
                            vuelta += 1
                            contador +=1
                            
                        else:
                            if bandera ==0:
                                cad2 = cad2 + 'WORD [rbp -'+ str(obj2.pos)+']'
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
                                cad2 = cad2 + 'WORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')

                            #vuelta =0
                            
                                
                            i = 0
                            
                            contador +=1

                        if (vuelta ==2 or contador >= self.partederecha):
                            if self.bandera[0]=='+':
                                self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                            elif self.bandera[0]=='*':
                                self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                            self.bandera.pop(0)
                            
                            vuelta = 0
                            bandera = 1
                            cad = 'MOV rax, '
                            cad2 = 'MOV rdi, '
                            break
                    else:
                        i+1
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
                self.codigo.append('\t''MOV QWORD [rbp -'+ str(obj.pos)+'], ' + 'rax')

    def parametros(self, cantidad, nombre):
        self.cantidad = cantidad
        self.nombre = nombre
        i =0
        if self.comienzo == 0:
            self.comienzo = self.posicionvar +20
        else:
            self.comienzo = self.comienzo
        while i < cantidad:
            self.codigo.append('\tMOV QWORD [rbp -' +str(self.comienzo)+'], rdi ')
            listaref.append(referencia(self.nombre, globals()['contexto'], self.comienzo))
            i+=1
            self.comienzo+=4


    def traductorfunc(self):
        self.codigo.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'POP rbp \n\t' + 'ret \n\t')
        self.posicionvar = 4
        self.comienzo = 0
    def traductorretorno(self, cad, contexto):
        self.cad = cad
        self.contexto = contexto
        for obj in listaref:
            if self.cad == obj.var and self.contexto == obj.contexto:
                self.codigo.append('\t''MOV rax, QWORD [rbp -'+ str(obj.pos)+']')

    def llamadafuncion(self, enviados, llamado, nombre):
        self.enviados = enviados
        self.llamado = llamado
        self.nombre = nombre
        for obj in listaref:
            if self.enviados == obj.var and globals()['contexto'] == obj.contexto:
                self.codigo.append('\t''MOV rax, QWORD [rbp -'+ str(obj.pos)+']')
        self.codigo.append('\t''MOV rdi, rax')
        self.codigo.append('\n\t''call '+ str(nombre))
        for obj in listaref:
            if self.llamado == obj.var and globals()['contexto'] == obj.contexto:
                self.codigo.append('\n\t''MOV QWORD [rbp -'+ str(obj.pos)+'], rax')
    def codigoasm(self):
        pass
    def prueba(self):
        print('--------')
        for obj in self.codigo:
            print(obj)
        Archivo=open("ensamblador.txt","w")
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
