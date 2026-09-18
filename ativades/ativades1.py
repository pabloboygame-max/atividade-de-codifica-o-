# Lê os dois valores inteiros
A, B = map(int, input().split())

# Evita divisão por zero e verifica se um número é múltiplo do outro
if A == 0 or B == 0:
    print("Nao sao Multiplos")
elif A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")