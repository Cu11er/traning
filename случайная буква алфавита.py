import random
def get_random_letter(n):
    return random.choices([chr(i) for i in range(ord('а'), ord('я'))], k=n)


print(get_random_letter(int(input('Сколько случайных букв желаешь: '))))
