# как найти индекс символа из списка!

result = input('Введите строку: ')

# result = ['g', 'h', 'b', 'd', 'h', 'n', 'h']
answer = [i_words for i_words in range(len(result)) if result[i_words] == 'h']

print('Развернутая последовательность между первым и последним h:', result[max(answer) - 1:min(answer):-1])
