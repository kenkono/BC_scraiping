import requests
from Constants import Constants

class PageFetcher:
    def __init__(self):
        # 基本URLとヘッダーを設定する
        self.constants = Constants()
        self.base_url = self.constants.BASE_URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def fetch_page(self, page_number):
        # 指定したページ番号の検索結果を取得する
        search_url = f"{self.base_url}?q=冷蔵庫&page={page_number}"
        response = requests.get(search_url, headers=self.headers, verify=False)
        response.raise_for_status()  # エラーチェック
        return response.text