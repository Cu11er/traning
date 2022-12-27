# Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут передаваться
# пользовательские значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите метод, который предоставляет информацию о ней.
# Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.
#
# Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.

class Object:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Object.count += 1

    def print_info(self):
        print('Coordinates x - {}, t - {}'.format(self.x, self.y))


test = Object(5, 10)
test.print_info()
test1 = Object()
test1.print_info()
