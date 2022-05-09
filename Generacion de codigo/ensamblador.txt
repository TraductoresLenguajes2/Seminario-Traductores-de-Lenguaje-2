section.text 
global sum
, menusum:
 	PUSH rbp 
	MOV rbp, rsp 
	SUB rsp, 48 
		MOV QWORD [rbp -24], rdi 	MOV rax, QWORD [rbp -24]	MOV WORD [rbp -4] , rax	MOV rax, QWORD [rbp -4]
	ADD rsp, 48 
	MOV rsp, rbp 
	POP rbp 
	ret 
	menu:
 	PUSH rbp 
	MOV rbp, rsp 
	SUB rsp, 48 
		MOV WORD [rbp -4] , 0x2	MOV WORD [rbp -8] , 0x2	MOV rax, WORD [rbp -8]
	MOV rdi, WORD [rbp -8]
	MUL rax, rdi
	MOV rdi, WORD [rbp -4]
	ADD rax, rdi
	MOV rdi, WORD [rbp -8]
	ADD rax, rdi
	MOV QWORD [rbp -8], rax	MOV rax, QWORD [rbp -8]
	ADD rsp, 48 
	MOV rsp, rbp 
	POP rbp 
	ret 
	