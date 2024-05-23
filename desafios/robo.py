def classificar_numero(numero):
    if numero > 0:
        return 'positivo'
    else:
        return 'negativo'
        
def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break

        print(f'{classificar_numero(numero)}!')

        if classificar_numero(numero) == 'positivo':
            positivos += 1
        else:
            negativos += 1 

    print(f'{positivos} números positivos, {negativos} números negativos.')


if __name__ == "__main__":
    main()
