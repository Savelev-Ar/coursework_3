from utils import *
from config import *


def main():
    # Получаем список всех операций
    list_all_operation = get_all_operations(JSON_PATH)
    # Получаем из списка всех операций список выполненных операций
    executed_operations_list = get_executed_operations_from_list(list_all_operation)
    # Сортируем список выполненных операций по дате
    sorted_by_date_operations = sort_operations_list_by_date(executed_operations_list)
    # Получаем из отсортированного списка последние пять операций
    last_five_operation = recent_operations_in_list(sorted_by_date_operations)
    # Выводим список в установленном формате
    for operation in get_list_operations_with_format(last_five_operation):
        print(operation)


if __name__ == '__main__':
    main()
