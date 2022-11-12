# Мы поддерживаем свой киносайт и хотим сделать так, чтобы пользователи после регистрации могли создать
# собственный рейтинг фильмов из тех, которые есть на сайте.

def chek_film(film, films):
    for i_film in films:
        if i_film == film:
            return True
    else:
        return False


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица', 'Не грози южному централу'
]
user_films = []

while True:
    print('Ваш текущий топ фильмов:', user_films)
    print('\nНазвание фильма: ', end='')
    film = input()
    if chek_film(film, films):
        print('Команды: добавить, вставить, удалить')
        user_comand = input('Введите команду: ')
        if user_comand == 'добавить':
            if chek_film(film, user_films):
                print('Этот фильм уже есть в вашем списке.')
            else:
                user_films.append(film)
        if user_comand == 'вставить':
            if chek_film(film, user_films):
                print('Этот фильм уже есть в вашем списке.')
            else:
                user_index = int(input('На какое место: '))
                user_films.insert(user_index - 1, film)
        if user_comand == 'удалить':
            user_films.remove(film)
        else:
            print('Вы ввели неверную команду!')
    else:
        print('Такого фильма на сайте нет')
