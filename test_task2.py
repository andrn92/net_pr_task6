import pytest
import requests
from task2 import YaDisk


with open('token_ya', 'r') as f:
    token_ya = f.readline().strip()

ya = YaDisk(token=token_ya)
new_folder = '/New_info'


def test_create_folder():
    resp_code = ya.create_folder(new_folder)
    assert resp_code in range(200, 203)

def test_exists_folder():
    data = ya.get_list_files()
    fl_find = False
    for element_info in data['items']:
        if element_info['path'].split(':')[1].split('/')[1] == new_folder[1:]:
            fl_find = True
            break
    assert fl_find == True
     


