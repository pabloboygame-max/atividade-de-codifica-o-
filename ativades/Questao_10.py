def resolver_enigma():
    try:
        mensagem = input().strip()
        crib = input().strip()
        
        n_msg = len(mensagem)
        n_crib = len(crib)
        
        possibilidades = 0
        
        for i in range(n_msg - n_crib + 1):
            valido = True
            for j in range(n_crib):
                if crib[j] == mensagem[i + j]:
                    valido = False
                    break
            
            if valido:
                possibilidades += 1
                
        print(possibilidades)
    except EOFError:
        pass

if __name__ == "__main__":
    resolver_enigma()