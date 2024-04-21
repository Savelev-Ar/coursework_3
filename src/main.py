from utils import *
from config import *
def main():
    list_all_operation = get_all_operations(JSON_PATH)
    executed_operations_list = get_executed_operations_from_list(list_all_operation)
    sorted_by_date_operations = sort_operations_list_by_date(executed_operations_list)
    last_five_operation = recent_operations_in_list(sorted_by_date_operations)
    print_list_operations_with_format(last_five_operation)

if __name__ == '__main__':
    main()
