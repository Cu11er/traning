# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали,
# что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.
# Напишите программу, которая получает на вход список цен на товары (вещественные числа,
# список генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.
#
# Пример:
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
# Повышение на первый год: 0
# Повышение на второй год: 10
# Сумма цен за каждый год: 93.83 93.83 103.22

def get_percent_price(percent, price):
    return round(price * (1 + percent / 100), 2)


price_now = [float(input('Цена на товар:')) for _ in range(5)]

first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

price_first = [get_percent_price(first_percent, i_price) for i_price in price_now]
price_second = [get_percent_price(second_percent, i_price) for i_price in price_first]

print('Сумма цен за каждый год:', round(sum(price_now), 2), round(sum(price_first), 2), round(sum(price_second), 2))
