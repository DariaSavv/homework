# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_positive_01():
    assert all_division(10, 2) == 5, 'Результат не может быть не 5'


def test_positive_02():
    assert all_division(100, 5, 5, 4) == 1, 'Результат должен быть 1'


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(1, 0), 'Результат деление на 0'


@pytest.mark.negative
def test_division_by_string():
    with pytest.raises(TypeError):
        assert all_division(89, '4'), 'Ошибка на строковое значение'


@pytest.mark.negative
def test_division_by_not_int():
    with pytest.raises(TypeError):
        assert all_division(58, [7, 10]), 'Ошибка на строковое значение'
