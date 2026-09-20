.model small
.stack 100h

.data
num1      dw 10
num2      dw 20
num3      dw 30
resultado dw ?

.code
main proc
    mov ax, @data
    mov ds, ax

    ; ENTRADA: valores almacenados en variables
    mov ax, num1
    mov bx, num2
    mov cx, num3

    ; PROCESAMIENTO: suma de los tres números
    add ax, bx
    add ax, cx

    ; GUARDAR RESULTADO
    mov resultado, ax

    ; SALIDA: mostrar el resultado en pantalla
    mov bx, 10
    xor cx, cx

convertir:
    xor dx, dx
    div bx
    push dx
    inc cx
    cmp ax, 0
    jne convertir

mostrar