from src.utils import get_all_operations, get_executed_operations_from_list, sort_operations_list_by_date, recent_operations_in_list, hide_number, get_list_operations_with_format
import pytest


test_list = [
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
]
def test_get_all_operations():
    assert get_all_operations('test_operations.json') == test_list


def test_get_executed_operations_from_list():
    assert get_executed_operations_from_list([]) == []


def test_sort_operations_list_by_date():
    assert sort_operations_list_by_date(test_list) == [
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
      },
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
    ]


def test_recent_operations_in_list():
    assert recent_operations_in_list(test_list, 1) == [
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
  }
    ]


def test_hide_number():
    assert hide_number('Счет 41421565395219882431') == 'Счет **2431'


def test_get_list_operations_with_format():
    assert get_list_operations_with_format(test_list) == ['09.12.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб. ',
                                                          '08.03.2018 Открытие вклада\n... -> Счет **2431\n48223.05 руб. \n']
