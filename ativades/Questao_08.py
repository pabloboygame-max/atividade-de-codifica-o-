reclamacao= (int(input("Quantas reclamações deseja registrar?(0-100):  ")))
if reclamacao<0 or reclamacao>100:
    print("Número inválido. Digite um número entre 0 e 100.")   
else:    
    if reclamacao==0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")    