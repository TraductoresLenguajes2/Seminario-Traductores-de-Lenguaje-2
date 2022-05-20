section .data  
	primr: db  "La impresion es := %lf",10,0 
section .bss 
	resp: resq 2
section .text 

extern printf
global sum
, main
sum:
 	PUSH rbp 
	MOV rbp, rsp 
	SUB rsp, 48 
	MOV QWORD [rbp -24], rdi 
	MOV rax, QWORD [rbp -24]
	MOV rdi, 2
	ADD rax, rdi

	ADD rsp, 48 
	MOV rsp, rbp 
	POP rbp 
	ret 
	
main:
 	PUSH rbp 
	MOV rbp, rsp 
	SUB rsp, 48 
		MOV WORD [rbp -4] , 7
	MOV WORD [rbp -8] , 2
	MOV rax, QWORD [rbp -4]
	MOV rdi, rax
	call sum
	MOV QWORD [rbp -8], rax
	
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
	