
def lista(n: int) -> list[str]:
	
	answer = []

	for i in range(1, n + 1):
		if i % 3 == 0 and i % 5 == 0:
			answer.append("FizzBuzz")
		elif i % 3 == 0:
			answer.append("Fizz")
		elif i % 5 == 0:
			answer.append("Buzz")
		else:
			answer.append(str(i))

	return answer
n = int(input("Digite um número inteiro positivo: "))
if n <= 0:
    print("Número inválido. Digite um número inteiro positivo.")    
	
print(lista(n))
