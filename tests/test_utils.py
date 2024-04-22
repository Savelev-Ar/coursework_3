from src.utils import get_all_operations, get_executed_operations_from_list, sort_operations_list_by_date, recent_operations_in_list, hide_number, get_list_operations_with_format
import pytest


def test_get_all_operations():
    assert get_all_operations('test_operations.json') == [
                                                         {
                                                         "id": 587085106,
                                                         "state": "EXECUTED",
                                                         "date": "2018-03-23T10:45:06.972075",
                                                         "operationAmount": {
                                                           "amount": "48223.05",
                                                           "currency": {
                                                             "name": "руб.",
                                                             "code": "RUB"
                                                           }
                                                         },
                                                         "description": "Открытие вклада",
                                                         "to": "Счет 41421565395219882431"
                                                         },
                                                         {
                                                         "id": 594226727,
                                                         "state": "CANCELED",
                                                         "date": "2018-09-12T21:27:25.241689",
                                                         "operationAmount": {
                                                           "amount": "67314.70",
                                                           "currency": {
                                                             "name": "руб.",
                                                             "code": "RUB"
                                                           }
                                                         },
                                                         "description": "Перевод организации",
                                                         "from": "Visa Platinum 1246377376343588",
                                                         "to": "Счет 14211924144426031657"
                                                         }
                                                         ])


def test_get_executed_operations_from_list():
    assert get_executed_operations_from_list([]) == []


def test_sort_operations_list_by_date():
    pass


def test_recent_operations_in_list():
    pass


def test_hide_number():
    pass


def test_get_list_operations_with_format():
    pass
