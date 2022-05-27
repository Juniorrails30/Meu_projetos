secreta = '' # aqui você coloca, a palavra que você desejar que o jogador adivinhe
digitadas = []
while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra. ')
        continue
    digitadas.append(letra)
    if letra in secreta:
        print(f'Ahhh a letra {letra} está em palavra!!')
    else:
        print(f'AFFF a letra {letra} não está em palavra secreta!!')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreta:
        print(f'Você ganhou, Parabéns!! A palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temp}')
