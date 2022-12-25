# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
# но и записывают эту ошибку в файл. Таким образом проще сформировать отчёт об ошибках, а значит,
# программисту будет проще их исправить. Это называется логированием ошибок.
#
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов, из которых можно
# получить палиндром (привет предыдущим модулям). Если в строке встречается число, то программа выдаёт ошибку ValueError
# и записывает эту ошибку в файл errors.log
def check_palindrome(word):
    return word == word[::-1]

words = None
log_file = None
count = 0
try:
    words = open('words.txt', 'r', encoding='utf8')
    log_file = open('log_file.txt', 'w', encoding='utf8')
    for line in words:
        clear_line = line.rstrip()
        if clear_line.isalpha():
            count += check_palindrome(clear_line)
        else:
            raise ValueError

except FileNotFoundError as exc:
    print('Файл "words.txt" не найден!')
    log_file.write(str(type(exc)))
except ValueError as exc:
    print('строка состоит из букв не полностью!')
    log_file.write(str(type(exc)))
finally:
    words.close()
    log_file.close()

print('Палиндромов:', count)
