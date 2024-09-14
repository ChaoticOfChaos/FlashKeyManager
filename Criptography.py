import hashlib

# Sistema de Criptografia das Chaves(Sistema Simples)
def stringToBinary(string: str) -> str:
    return ''.join(format(ord(char), '08b') for char in string)

def binaryToString(binary: str) -> str:
    byte_size = 8
    text = ''.join([chr(int(binary[i:i+byte_size], 2)) for i in range(0, len(binary), byte_size)])
    return text

def binaryToHexadecimal(binary: str) -> str:
    decimal = int(binary, 2)
    return hex(decimal)[2:].upper().zfill(len(binary) // 4)

def hexadecimalToBinary(hexa: str) -> str:
    decimal = int(hexa, 16)
    return bin(decimal)[2:].zfill(len(hexa) * 4)

def criarHashSha256(string: str) -> str:
    sha = hashlib.sha256()
    sha.update(string.encode('utf-8'))
    return sha.hexdigest()