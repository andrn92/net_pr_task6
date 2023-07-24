
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_check_list(list_in:list) -> list:
    i = 0
    run = True
    while run:
        for country in list_in[i].values():
            if 'Россия' not in country:
                list_in.remove(list_in[i])
                if i == len(list_in):
                    run = False
                    break
            elif 'Россия' in country and i < len(list_in) - 1:
                i += 1
            elif 'Россия' in country and i == len(list_in) - 1:
                run = False
                break

    return list_in


def get_unique_values(d:dict) -> list:
    list_out = []
    for numbers in d.values():
        for number in numbers:
            if number not in list_out:
                list_out.append(number)
                
    return list_out


def get_max_sales(d:dict) -> str:
    max_value = -1
    for name, value in d.items():
        if value > max_value:
            max_value = value
            company = name
    
    return company


if __name__ == '__main__':

    list_geo_data = get_check_list(geo_logs)
    print(list_geo_data)
    list_numbers = get_unique_values(d=ids)
    print(list_numbers)
    company = get_max_sales(stats)
    print(company)




    