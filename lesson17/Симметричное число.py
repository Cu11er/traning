# улучшение кода

def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False

total_num = int(input('Кол-во чисел: '))
number_list = []
answer = []

for num in range(total_num):
    num = int(input('Число: '))
    number_list.append(num)

for i_num in range(0, len(number_list)):
    if is_palindrome(number_list[i_num:len(number_list)]):
        answer = number_list[:i_num]
        answer.reverse()
        print('Последовательность:', number_list)
        if len(answer) == 0:
            print('Уже является палиндромом!')
            break
        print('Нужно приписать чисел:', len(answer))
        print('Сами числа:', answer)
        break
