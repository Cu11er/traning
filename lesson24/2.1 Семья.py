# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома»
# и объекты которого могут выполнять следующие действия:
#
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

class Family:
    family_name = 'Common family'
    funds = 100000
    having_a_house = False


    def info(self):
        print(
            'Family name - {}\ntotal money - {}\nhaving a house - {}\n'.format(
                self.family_name, self.funds, self.having_a_house
            )
        )

    def take_money(self, money):
        self.funds += money
        print('Money in family - {}'.format(self.funds))

    def take_a_house(self, prise, discount=0):
        prise -= prise * discount / 100
        print('prise house - {}'.format(prise))
        if self.funds >= prise:
            print('House cashed!')
            self.funds -= prise
            print('Money in family - {}'.format(self.funds))
        else:
            print('dont have a money!')


first_family = Family()
first_family.info()
first_family.take_money(500)
first_family.take_a_house(200000)
first_family.take_money(700)
first_family.take_a_house(101000, 10)
