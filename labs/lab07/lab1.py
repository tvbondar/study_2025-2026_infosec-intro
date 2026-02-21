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
plain = ("С Новым Годом, друзья!")
print(f"Открытый текст: {plain}")

# генерация ключа
key = generate_key(len(plain))
print(f"Ключ: {key}")

# преобразование ключа в коды
plain_codes = text_to_codes(plain)

# шифрование
cipher_bytes = xor(plain_codes, key)
cipher_text = codes_to_text(cipher_bytes)
print(f"Зашифрованный текст: {cipher_text}")

# дешифровка
decrypted_bytes = xor(cipher_bytes, key)
decrypted_text = codes_to_text(decrypted_bytes)
print(f"Расшифровано: {decrypted_text}")


# поиск ключа
target = ("С Новым Годом, друзья!")
print(f"Искомый текст: {target}")
target_bytes = text_to_codes(target)

possible_key = xor(cipher_bytes, target_bytes)
print(f"Найденный ключ: {possible_key}")
