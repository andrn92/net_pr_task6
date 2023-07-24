import requests
import json


class YaDisk:
    """Working with Yandex Disk"""

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
    
    def get_list_files(self):
        url = self.host + 'v1/disk/resources/files/'
        response = requests.get(url, headers=self.get_headers())
        return response.json()

    def create_folder(self, name_folder):
        url = self.host + 'v1/disk/resources/'
        params = {'path': name_folder}
        response = requests.put(url, headers=self.get_headers(), params=params)
        return response.status_code

    def upload_from_internet(self, file_url, disk_file_name):
        url = self.host + 'v1/disk/resources/upload/'
        params = {'path': '{}'.format(disk_file_name), 'url': file_url}
        response = requests.post(url, headers=self.get_headers(), params=params)
        print(response.status_code)
       

if __name__ == '__main__':
    with open('token_ya', 'r') as f:
        token_ya = f.readline().strip()

    ya = YaDisk(token_ya)
    new_folder = '/New_info'
    resp_code = ya.create_folder(new_folder)
    
    data = ya.get_list_files()
   

