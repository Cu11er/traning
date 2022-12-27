class Potato:
    states = {0: 'Пусто', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def growth(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i in self.potatoes:
            i.growth()

    def are_all_ripe(self):
        # for i_potato in self.potatoes:
        #     if not i_potato.is_ripe():
        # можно заменить на:
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела! Можно собирать\n')

    def print_all_state(self):
        for potato in self.potatoes:
            potato.print_state()