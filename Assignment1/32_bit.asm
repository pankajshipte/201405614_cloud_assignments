extern	printf

        SECTION .data

	a:	dd	3	; int a=5;
fmt:    db "a=%d, b=2, a+b=%d", 10, 0


        SECTION .text
        global main
main:
	
	mov	eax,[a]
	add	eax,2
	mov	edi,fmt
	mov	esi,[a]
	mov	edx,eax
	mov	eax,0
        call    printf


	mov	eax,0
	ret
