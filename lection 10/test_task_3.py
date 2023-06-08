# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('test_positive, test_skip, result', [
    pytest.param(99, 10, 9.9, marks=pytest.mark.smoke),
    pytest.param(-89, 8, 93, marks=pytest.mark.skip),
    (-22, -2, 11)],
                         ids=['positive', 'skip', 'negative'])
def test(test_positive, test_skip, result):
    assert all_division(test_positive, test_skip) == result


