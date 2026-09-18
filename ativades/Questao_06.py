r=0
a=0
g=0
d=0

while r!=4:

    r=int(input("1.Álcool \n2.Gasolina \n3.Diesel \n4.Fim \n"))
     
    if r<1 or r>4:
        print("Opção inválida. Tente novamente.")

        r= int(input("1.Álcool \n2.Gasolina \n3.Diesel \n4.Fim \n"))

        if r==1:
            a=a+1 

        elif r==2:
            g=g+1

        elif r==3:
            d=d+1

        elif r==4:
            print()
            print("Álcool: ", a)
            print("Gasolina: ", g)
            print("Diesel: ", d)
            break    

    else :
        
        if r==1:
            a=a+1 

        elif r==2:
            g=g+1

        elif r==3:
            d=d+1

        elif r==4:
            print()
            print("Álcool: ", a)
            print("Gasolina: ", g)
            print("Diesel: ", d)
            break

 