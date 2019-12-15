from work_package import bubble_sort
import pytest


def idfn(p):  # параметр для удобного отображения результатов теста
    return f'list={p[0]}, res={p[1]}'


@pytest.fixture(scope='function', params=[  # декоратор для сокращения повторяющихся assert'ов
    ([], []),
    ([18], [18]),
    ([31, 31], [31, 31]),
    ([18, -18], [-18, 18]),
    ([56, 56, 47], [47, 56, 56]),
    ([12, -42, 108, 12, 52], [-42, 12, 12, 52, 108]),
    ([110, -110, 45, -45], [-110, -45, 45, 110]),
    ([230, - 231, 232, - 233], [-233, - 231, 230, 232]),
    ([17, 25, -67, 74, -89], [-89, -67, 17, 25, 74]),
    ([56, 9, 48, 99, 13, 67], [9, 13, 48, 56, 67, 99])],
                ids=idfn
                )
def param_test_idfn(request):  # запрос данных
    return request.param


def test_div(param_test_idfn):  # инициализация теста
    inp, expext = param_test_idfn
    res = bubble_sort.bubble_sort(inp)
    assert res == expext  # сравнение полученного результата с ожидаемым
