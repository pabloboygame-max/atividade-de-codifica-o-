n=int(input("Informe o numero, entre 0 e 46,  para sequencia de Fibonacci: "))
if n<0 or n>46:
    print("Número inválido. Digite um número entre 0 e 46.")
else:
    
    a=0
    b=1
    print("Sequencia de Fibonacci:")
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c        