import random


def text_to_codes(text):
    """Преобразует строку в список кодов символов"""
    codes = []
    for i in range(len(text)):
        codes.append(ord(text[i])) 
    return codes
    
def codes_to_text(codes):
    """Преобразует список кодов обратно в строку"""
    text = ""
    for i in range(len(codes)):
        text += chr(codes[i])
    return text 


def xor(b1, b2):
    """XOR двух списков кодов"""
    if len(b1) != len(b2):
        print("Ошибка: длины не соответсвуют")
        return None
    result = []
    for i in range(len(b1)):
        new = b1[i]^b2[i]
        result.append(new)
    return result

def generate_key(length):
    """Генерирует случайный ключ заданной длины"""
    key = []
    for i in range(length):
        key.append( random.randint(0, 255))
    return key    


# основная программа
plain1 = ("С Новым Годом, друзья!")

plain2 = ("У Слона домов, огого!!")

# генерация ключа
key = generate_key(len(plain1))

# преобразование ключа в коды
plain_codes1 = text_to_codes(plain1)
plain_codes2 = text_to_codes(plain2)

# шифрование
cipher_bytes1 = xor(plain_codes1, key)
cipher_text1 = codes_to_text(cipher_bytes1)

cipher_bytes2 = xor(plain_codes2, key)
cipher_text2 = codes_to_text(cipher_bytes2)

# дешифровка
decrypted_bytes1 = xor(cipher_bytes1, key)
decrypted_text1 = codes_to_text(decrypted_bytes1)

decrypted_bytes2 = xor(cipher_bytes2, key)
decrypted_text2 = codes_to_text(decrypted_bytes2)

print('Открытый текст: ', plain1, "\nКлюч: ", key, '\nШифротекст: ', cipher_text1, '\nИсходный текст: ', decrypted_text1,)
print('Открытый текст: ', plain2, "\nКлюч: ", key, '\nШифротекст: ', cipher_text2, '\nИсходный текст: ', decrypted_text2,)

r = xor(cipher_bytes1, cipher_bytes2) 
print('Расшифровать второй текст, зная первый: ', codes_to_text(xor(plain_codes1, r)))
print('Расшифровать первый текст, зная второй: ', codes_to_text(xor(plain_codes2, r)))