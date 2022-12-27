# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
#
# У картошки есть её номер в грядке, а также стадия зрелости.
# Она может предоставлять информацию о своей зрелости и расти.
# Всего у картошки может быть четыре стадии зрелости.
#
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# а также предоставлять информацию о зрелости всей картошки на своей территории.
#
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.

from Garden import Garden

my_garden = Garden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()

potato = Potato(2)
potato.print_state()
