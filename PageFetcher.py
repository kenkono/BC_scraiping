import requests
import os
from Constants import Constants
import urllib.parse

class PageFetcher:
    def __init__(self):
        # 基本URLとヘッダーを設定する
        self.constants = Constants()
        self.base_url = self.constants.BASE_URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.encoded_query_str = urllib.parse.quote(self.constants.encoded_query) # クエリ文字列をURLエンコードして、encoded_query_strに格納
        # self.cert_path = os.path.join(os.path.dirname(__file__), 'biccamera.pem') # 証明書ファイルのパスを設定

    def fetch_page(self, page_number):
        # 指定したページ番号の検索結果を取得する
        search_url = f"{self.base_url}?q={self.encoded_query_str}&p={page_number}"
        # response = requests.get(search_url, headers=self.headers, verify=self.cert_path) # 証明書パス使用
        response = requests.get(search_url, headers=self.headers, verify=False) # 証明書を無視
        response.raise_for_status()  # エラーチェック
        response.encoding = 'shift_jis'  # 文字化け防止のためShiftJISに設定
        return response.text