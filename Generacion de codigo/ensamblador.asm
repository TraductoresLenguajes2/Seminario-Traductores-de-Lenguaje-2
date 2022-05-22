section .data  
	primr: db  "La impresion es := %lf",10,0 
section .bss 
	resp: resq 2
section .text 

extern printf
global main

main:
 	PUSH rbp 
	MOV rbp, rsp 
	SUB rsp, 48 
		MOV WORD [rbp -4] , 2
	MOV WORD [rbp -8] , 4
	MOV ax, WORD[rbp -4]
	MOV bx, WORD[rbp -8]
	CMP ax, bx
	jg if
MOV rax, QWORD [rbp -4]
regreso:
	
	PUSH qword[rbp -8]
	FILD dword[rsp]
	FSTP qword[rel resp]
	ADD rsp, 8
	MOVSD xmm0,qword[rel resp]
	MOV rdi, primr
	MOV al, 1
	call printf WRT ..plt 
	MOV rax, QWORD [rbp -8]

	ADD rsp, 48 
	MOV rsp, rbp 
	MOV rax, 60 
	MOV rdi, 0 
	syscall 
	
if:
	MOV WORD [rbp -8] , 5
	jmp regreso