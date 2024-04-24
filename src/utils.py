import json


def get_all_operations(json_path):
    """
    Функция получает на вход путь до файла с данными, возвращает список с данными
    """
    with open(json_path, encoding='utf-8') as file:
        data = file.read()
        all_data = json.loads(data)
    return all_data


def get_executed_operations_from_list(list_):
    """
    Функция возвращает список выполненных операций из списка операций
    """
    result_list = []
    for item in list_:
        if item.get('state') == 'EXECUTED':
            result_list.append(item)
    return result_list


def sort_operations_list_by_date(list_):
    """
    функция возвращает отсортированный по дате список операций
    """
    return sorted(list_, key=lambda operation: operation['date'], reverse=True)


def recent_operations_in_list(list_, count=5):
    """
    Функция возвращает count(по умолчанию 5) операций из списка операций
    """
    return list_[0:count]


def hide_number(string):
    """
    функция скрывает номера карт и счетов
    """
    if string == "...":
        return string
    list_ = string.split()
    if list_[0] == 'Счет':
        list_[-1] = '**' + list_[-1][-4:]
        result = ' '.join(list_)
    else:
        number = ''
        for i in range(len(list_[-1])):
            number = number + '*'
        list_[-1] = (list_[-1][0:6] + number[6:-4] + list_[-1][-4:])
        for i in range(len(list_[-1])):
            if i % 5 == 0:
                list_[-1] = list_[-1][0:i] + ' ' + list_[-1][i:]
        result = ' '.join(list_)
    return result


def get_list_operations_with_format(list_):
    """
    функция возвращает список операций для вывода в установленном формате
    """
    result = []
    for item in list_:
        if item.get("from") is not None:
            from_ = item["from"]
        else:
            from_ = "..."

        date = f'{item["date"][8:10]}.{item["date"][5:7]}.{item["date"][0:4]}'

        result.append(f'{date} {item["description"]}\n{hide_number(from_)} -> {hide_number(item["to"])}\n'
                      f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]} \n')
    return result
