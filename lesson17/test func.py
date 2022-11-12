nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [j for i_num in range(len(nice_list))
              for i in range(len(nice_list[i_num]))
              for j in nice_list[i_num][i]]

print('Ответ:', result)
