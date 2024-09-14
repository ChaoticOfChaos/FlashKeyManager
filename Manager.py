import FlashKey

def getParams(prompt: str, param: str) -> str:
    params = prompt.split(' ')
    for paramKey in params:
        if f'{param}=' in paramKey:
            return paramKey.split('=')[1]

def Help():
    print('? - Help')
    print('close - Close Key Manager')
    print('create.key - Create a Key. Params(slot, user, password)')
    print('create.key.hash - Create a Key With Hash. Params(slot. user, password)')
    print('exit - Close Key Manager')
    print('help - Help')
    print('key.acess - Verify All Slots And Show Whats Have Credentials. Params(user, password)')
    print('key.acess.hash - Verify All Slots and Show Whats Have Hash Credentials. Params(user, password)')
    print('quit - Close Key Manager')
    print('slot.search - Search All Slot Available')

slots = []
slotSearch = False
while True:
    userInput = input('-> ')

    if userInput.lower().startswith('create.key.hash'):
        FlashKey.createKeyHash(
            getParams(userInput, 'slot'),
            getParams(userInput, 'user'),
            getParams(userInput, 'password')
        )

    elif userInput.lower().startswith('create.key'):
        FlashKey.createKey(
            getParams(userInput, 'slot'),
            getParams(userInput, 'user'),
            getParams(userInput, 'password')
        )

    elif userInput.lower().startswith('key.acess.hash'):
        if slotSearch:
            for slot in slots:
                if FlashKey.keyAcessHash(
                    [slot],
                    getParams(userInput, 'user'),
                    getParams(userInput, 'password')
                ):
                    print(f'{slot} : {True}')

                else:
                    print(f'{slot} : {False}')

        else:
            print('Error. First Use Command "slots.search"')

    elif userInput.lower().startswith('key.acess'):
        if slotSearch:
            for slot in slots:
                if FlashKey.keyAcess(
                    [slot],
                    getParams(userInput, 'user'),
                    getParams(userInput, 'password')
                ):
                    print(f'{slot} : {True}')

                else:
                    print(f'{slot} : {False}')

        else:
            print('Error. First Use Command "slots.search"')

    elif userInput.lower() == 'slots.search':
        slots = FlashKey.keySlotSearch()
        for slot in slots:
            print(slot, end=' ')

        print(' ')
        slotSearch = True

    elif userInput.lower() == 'help' or userInput.lower() == '?':
        Help()

    elif userInput.lower() == 'close' or userInput.lower() == 'exit' or userInput.lower() == 'quit':
        break

    else:
        print('Error. Command Not Found')

    print('\n')