site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код
import copy


def display_struct(struct, spaces=1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(' ' * spaces, key)
            display_struct(value, spaces + 3)
        else:
            print('{}{} : {}'.format(' ' * spaces, key, value))


def create_site(site, total, phone=None, copy_site={}):
    if total == 0:
        return
    phone = input('Введите название продукта для нового сайта: ')
    total -= 1

    site['html']['head']['title'] = 'Куплю/продам {} недорого'.format(phone)
    site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(phone)
    new_site = copy.deepcopy(site)
    copy_site.update({'\nСайт для {}:'.format(phone): site})
    display_struct(copy_site)
    create_site(new_site, total)
    return


total_site = int(input('Сколько сайтов: '))
create_site(site, total_site)
# задача оказалась для меня сложной, с выводом как в примере так и не справился...