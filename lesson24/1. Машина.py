# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200
import random

class Toyota:
    color = 'красный'
    price = 1000000  # или 1e6
    max_speed = 200
    speed = 0

car1 = Toyota()  # экземпляр класса
car1.speed = random.randint(0, 200)
car2 = Toyota()
car2.speed = random.randint(0, 200)
car3 = Toyota()
car3.speed = random.randint(0, 200)

print(car1.speed)
print(car2.speed)
print(car3.speed)


