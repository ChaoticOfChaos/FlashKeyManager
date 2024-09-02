import os
from Criptography import *

# Função Que Verifica Quais Slots Estão Disponíveis
def keySlotSearch() -> list[str]:
    # Cada Char Aqui Representa um Slot Possível
    # C Não Existe Por Significar o Disco Local
    chars = "abdefghijklmnopqrstuvwxyz"
    # Lista Contendo Todos os Slots Disponíveis
    paths = []

    # Verifica Quais Diretórios de Slots Existem
    for char in chars:
        path = f'{char}:/'
        if os.path.exists(path):
            paths.append(path)

    return paths

# Função Que Dá Acesso as Chaves
# É Necessário Passar os Slots em uma lista, um usuário e senha
def keyAcess(slots: list[str], user, password) -> bool:
    for slot in slots:
        # Verifica se em Algum dos Slots Existe um Arquivo key.key
        if "key.key" in os.listdir(slot):

            # Caso Exista, Ele Abre e Verifica se as Credencias Batem
            with open(f"{slot}key.key", "r") as k:
                keyValue = hexadecimalToBinary(k.read())
                keyValue = binaryToString(keyValue)
                if f"user={user}" in keyValue and f"pass={password}" in keyValue:
                    # Se Sim, Retorna Verdadeiro
                    return True

    # Se Não, Retorna Falso
    return False

# Função que Cria as Chaves
# Precisa Passar uma String do Diretório Que a Chave Vai Ser Feita, Um Usuário e Senha
def createKey(slot: str, user: str, password: str) -> None:
    keyText = f'user={user}\npass={password}'
    binString = stringToBinary(keyText)
    hexaString = binaryToHexadecimal(binString)
    with open(f'{slot}key.key', 'w') as k:
        k.write(hexaString)