# Importa a Biblioteca
import FlashKey

# Exemplo de Criação de Chave no Slot D:
FlashKey.createKey('d:/', 'admin', '1234')

def main():
    print('Hello World!')

# Mostar Todos os Slots Disponíveis
print(FlashKey.keySlotSearch())


# Exemplo de Acesso Que Busca Exclusivamente Pelo Slot F:
if FlashKey.keyAcess(['f:/'], 'admin', '1234'):
    main()

# Exemplo de Acesso Que Busca Por Todos Slots Disponíveis
elif FlashKey.keyAcess(FlashKey.keySlotSearch(), 'admin', '1234'):
    main()

else:
    print('Nenhuma Chave Foi Encontrada')




# Criar Chave Com Criptografia Hash
FlashKey.createKeyHash('e:/', 'user', 'password')


# Exemplo de Acesso Que Busca Exclusivamente Pelo Slot E:
if FlashKey.keyAcessHash(['e:/'], 'user', 'password'):
    main()

# Exemplo de Acesso Que Busca Por Todos Slots Disponíveis
elif FlashKey.keyAcessHash(FlashKey.keyAcessHash(), 'user', 'password'):
    main()

else:
    print('Nenhuma Chave Com Criptografia Hash Foi Encontrada')