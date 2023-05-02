alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: O que acontece se o usuário inserir um número/símbolo/espaço?
        # Você pode corrigir o código para manter o número/símbolo/espaço quando o texto é codificado/decodificado?
        # por exemplo. start_text = "me encontre às 3"
        # end_text = "•••• •• •• 3"
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Importe e imprima o logotipo do art.py quando o programa iniciar.

# TODO-4: Você consegue descobrir uma maneira de perguntar ao usuário se ele deseja reiniciar o programa de cifra?
# por exemplo. Digite 'sim' se quiser ir novamente. Caso contrário, digite 'não'.
# Se eles digitarem 'sim', peça a direção/texto/deslocamento novamente e chame a função caesar() novamente?
# Dica: tente criar um loop while que continue a executar o programa se o usuário digitar 'yes'.

while True:
    direction = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar: \n")
    text = input("Digite sua mensagem: \n").lower()
    shift = int(input("Digite o número do turno: \n"))

    # TODO-2: E se o usuário inserir um turno maior que o número de letras do alfabeto? Tente executar o programa e
    #  inserir um número de turno de 45. Adicione algum código para que o programa continue funcionando mesmo se o
    #  usuário inserir um número de turno maior que 26. Dica: Pense em como você pode usar o módulo (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    resp = str(input('Deseja reinicar o programa? ')).lower()
    if resp == 'não':
        break
