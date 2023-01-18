alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direcao = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar: ")

text = input("Digite sua mensagem: ").lower()
shift = int(input("Digite o número do turno: "))

def encriptar(texto, qtd):
    txt_encriptado = ""
    for letra in texto:
        posicao = alphabet.index(letra)
        nova_posicao = posicao + qtd
        nova_letra = alphabet[nova_posicao]
        txt_encriptado += nova_letra
    print(f'Msg encriptada {txt_encriptado}')


def desencriptar(texto_encriptado, qtd):
    txt_desencriptado = ""
    for letra in texto_encriptado:
        posicao = alphabet.index(letra)
        nova_posicao = posicao - qtd
        txt_desencriptado += alphabet[nova_posicao]
    print(f'Mensagem desencriptada {txt_desencriptado}')


if direcao == "encode":
    encriptar(texto=text, qtd=shift)
elif direcao == "decode":
    desencriptar(texto_encriptado=text, qtd=shift)



