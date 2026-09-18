a1= int(input("Quantas pessoas trabalham no primeiro andar? "))
a2= int(input("Quantas pessoas trabalham no segundo andar? "))
a3= int(input("Quantas pessoas trabalham no terceiro andar? "))
a=int(input("Qual andar deseja fazer o teste de deixar a maquina de cafe? "))

if a==1:
    tempo=(a2*2)+(a3*4) #Pessoas do segundo andar levam 2 minutos, pois 1 min para descer e 1 min para subir.
    print(tempo)

elif a==2:
    tempo=(a1*2)+(a3*2)
    print(tempo)

elif a==3:
    tempo=(a1*4)+(a2*2)
    print(tempo)   