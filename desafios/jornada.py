def prever_fruta(peso, textura, cor):
    if peso >= 150 and textura == 'suave' and cor == 'vermelha':
        return 'A fruta é um morango!'
    elif peso >= 150 and textura == 'áspera' and cor == 'amarela':
        return 'A fruta é uma banana!'  
    elif peso >= 120 and textura == 'suave' and cor == 'laranja':
        return 'A fruta é uma laranja!'
    elif peso >= 130 and textura == 'áspera' and cor == 'vermelha':
        return 'A fruta é uma maçã!'
    else:
        return 'Não foi possível classificar a fruta.'

peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

print(resultado)
