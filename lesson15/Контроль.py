worker = int(input('Кол-во сотрудников в офисе: '))
worker_ID = []

for _ in range(worker):
    id = int(input('ID сотрудника: '))
    worker_ID.append(id)
search_ID = int(input('Какой ID ищем? '))

if search_ID in worker_ID:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')