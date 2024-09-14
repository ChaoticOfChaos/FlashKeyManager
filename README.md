# FlashKeyManager
Sistema Simples de Chaves em Pendrives

# Como Usar:
Espete um Pendrive no Sistema e Execute a Função FlashKey.createKey() Passando os Parâmetros Corretos
Após Quando Você Chamar a Função FlashKey.keyAcess() Passando os Parâmetros Corretos, Caso Exista Uma Chave no Sistema Usando Aquelas Credencias, Ele Retornará True


Caso Queira Usar Criptografias Hash Basta Usar as Funções FlashKey.createKeyHash() e FlashKey.acessKeyHash() no Lugar das Funções FlashKey.createKey() e FlashKey.acessKey() Respectivamente

# Como Usar(Manager):
Para Usar o Gerenciador Basta Usar os Comando e passando os Parâmetros Corretos, Como Por Exemplo: "user=admin" ou "password=1234". Comando de Exemplo: "create.key.hash slot=d: user=admin password=1234"

Para Usar os Acessos de Chaves, Antes é Necessário Usar o Comando "slots.search"
