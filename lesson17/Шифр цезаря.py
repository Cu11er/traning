def caesar_cipher(string, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
user_list = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

result = caesar_cipher(user_list, shift)
print('Зашифрованное сообщение:', result)
