import json

def get_all_operations(json_path):
    with open(json_path) as file:
        data = file.read()
        all_data = json.loads(data)
    return all_data

def get_executed_operations_from_list(list):
    result_list = []
    for item in list:
        if item.get('state') == 'EXECUTED':
            result_list.append(item)
    return result_list

def sort_operations_list_by_date(list):
    return sorted(list, key=lambda operation: operation['date'], reverse=True )

def recent_operations_in_list(list, count = 5):
    return list[0:count]

def print_list_operations_with_format(list):
    for item in list:
        if item.get("from") != None:
            from_ = item["from"]
        else:
            from_ = "..."
        print (f'{item["date"]} {item["description"]}\n'
               f'{from_} -> {item["to"]}\n'
               f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]} \n')