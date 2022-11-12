# вытащить вложенные списки в один общий список

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# списковая сборка:
output = [j for each_list in nice_list for each_list2 in each_list for j in each_list2]

# обычный цикл:
# for i_num in range(len(nice_list)):
#     for i in range(len(nice_list[i_num])):
#         for j in nice_list[i_num][i]:
#             nice_list3.append(j)


print('Итог:', output)

