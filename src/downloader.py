import os
import requests

class IBGEDownloader:
    def __init__(self, base_url, download_dir):
        self.base_url = base_url
        self.download_dir = download_dir
        os.makedirs(self.download_dir, exist_ok=True)

    def download_all_files(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            for arquivo in response.json():
                final_path = os.path.join(self.download_dir, f'{arquivo["name"]}.xlsx')
                self.download_file(arquivo['url'], final_path)
        else:
            print(f"Failed to retrieve data from {self.base_url}. Status code: {response.status_code}")

    def download_file(self, url, path):
        response_download = requests.get(url)
        with open(path, 'wb') as new_file:
            new_file.write(response_download.content)
            print(f'Download Finalizado! Arquivo salvo em {path}')
