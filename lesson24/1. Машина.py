# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200

class Toyota:

    def __init__(self, color='red', price=1000000, max_speed=300, speed=60):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.speed = speed

    def info(self):
        print(
            'Color {}\nprice {}\nmax_speed {}\ncurrent speed {}\n'.format(
            self.color, self.price, self.max_speed, self.speed
            )
        )

    def curspeed(self, speed):
        self.speed = speed


car1 = Toyota('зеленый', 1200000, 270, 190)

car1.info()
car1.curspeed(210)
car1.info()
car2 = Toyota()
car2.info()



