# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки.
# Однако при выводе был обнаружен баг: собаки с наибольшим и наименьшим количеством очков поменялись местами!
# Нужно это исправить.
#
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

total_dogs = int(input('Введите кол-во собак: '))
dogs_list = []
for dog in range(total_dogs):
    print('Сколько очков у', dog + 1, 'собаки:', end=' ')
    dog_score = int(input())
    dogs_list.append(dog_score)

min = dogs_list[0]
max = dogs_list[0]

min_index = 0
max_index = 0


for i_dogs in range(total_dogs):
    if dogs_list[i_dogs] < min:
        min = dogs_list[i_dogs]
        min_index = i_dogs

    if dogs_list[i_dogs] > max:
        max = dogs_list[i_dogs]
        max_index = i_dogs

print('мин число:', min)
print('макс число:', max)
print(dogs_list)
dogs_list[min_index], dogs_list[max_index] = dogs_list[max_index], dogs_list[min_index]
print(dogs_list)