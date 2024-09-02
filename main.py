# Importa a Biblioteca
import FlashKey

# Exemplo de Criação de Chave no Slot D:
FlashKey.createKey('d:/', 'admin', '1234')

def main():
    print('Hello World!')

# Mostar Todos os Slots Disponíveis
print(FlashKey.keySlotSearch())

# Exemplo de Acesso Que Busca Por Todos os Slots
if FlashKey.keyAcess(FlashKey.keySlotSearch(), 'admin', '1234'):
    main()

# Exemplo de Acesso Que Busca Exclusivamente Pelo Slot F:
elif FlashKey.keyAcess(['f:/'], 'admin', '1234'):
    main()
else:
    print('Nenhuma Chave Foi Encontrada')