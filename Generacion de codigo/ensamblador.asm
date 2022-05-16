section .data  
	primr: db  "La impresion es := %lf",10,0 
	section .bss 
	resp: resq 2
section .text 

	extern printf, scanf
global menu
menu:
 	PUSH rbp 
	MOV rbp, rsp 
	SUB rsp, 48 
		MOV WORD [rbp -4] , 2
	PUSH qword[rbp -4]
	FILD dword[rsp]
	FSTP qword[rel resp]
	ADD rsp, 8
	MOVSD xmm0,qword[rel resp]
	MOV rdi, primr
	MOV rdi, primr
	call printf WRT ..plt
	ADD rsp, 48 
	MOV rsp, rbp 
	POP rbp 
	ret 
	