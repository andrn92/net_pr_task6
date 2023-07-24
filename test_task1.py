import pytest

from task1 import geo_logs, ids, stats 
from task1 import get_check_list, get_unique_values, get_max_sales


def test_check_result():
    expected = 'Россия'
    for country in get_check_list(geo_logs):
        for value in country.values():
            assert expected in value


def test_unique_values():
    res = get_unique_values(ids)
    new_list = []
    for list_value in ids.values():
        new_list += list_value
    assert len(set(new_list)) == len(res)

    


def test_max_sales():
    res = get_max_sales(stats)
    max_value = sorted(stats.values(), reverse=True)[0]
    assert stats[res] == max_value
