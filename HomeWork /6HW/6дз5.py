def cezar_cipher(step, message):
    ciphered_message = ""
    for char in message:
        if "A" <= char <= "Z":
            ciphered_message += chr((ord(char) - ord("A") + step) % 26 + ord("Z"))
        elif "a" <= char <= "z":
            ciphered_message += chr((ord(char) - ord("a") + step) % 26 + ord("z"))
        else:
            ciphered_message += char
    return ciphered_message


shift = int(input("введите значение сдвига "))
message = input("введите сообщение ")
print(cezar_cipher(shift, message))