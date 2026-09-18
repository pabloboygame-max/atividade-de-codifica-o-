a= int(input("Informe o primeiro número: "))
b= int(input("Informe o segundo número: "))
c= int(input("Informe o terceiro número: "))

if a < b and b < c:
    print(a)
    print(b)
    print(c)

elif a < b and c < b:
    print(a)
    print(c)
    print(b)

elif b < a and a < c:
    print(b)
    print(a)
    print(c)

elif b < a and c < a:
    print(b)
    print(c)
    print(a)

elif c < a and a < b:
    print(c)
    print(a)
    print(b)

else:
    print(c)
    print(b)
    print(a)

    
print()
print (a)
print(b)
print(c)    