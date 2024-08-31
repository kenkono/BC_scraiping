from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

class PageFetcher:
    def __init__(self):
        # ChromeOptionsを設定してヘッドレスモードを有効にする
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # WebDriverの設定
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.base_url = "https://www.biccamera.com/bc/main/"

    def fetch_page(self):
        try:
            # 指定されたURLにアクセス
            self.driver.get(self.base_url)
            
            # 検索窓を見つけて「冷蔵庫」を入力し、Enterキーを押す
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.send_keys("冷蔵庫")
            search_box.send_keys(Keys.RETURN)
            
            # 検索結果のページがロードされるのを待つ
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".productList"))
            )
            
            # 検索結果のHTMLを取得
            html_content = self.driver.page_source
            
            # BeautifulSoupを使用してHTMLをパース
            soup = BeautifulSoup(html_content, 'html.parser')
            
            return soup.prettify()
        
        finally:
            # ブラウザを閉じる
            self.driver.quit()

# 使用例
if __name__ == "__main__":
    fetcher = PageFetcher()
    html_content = fetcher.fetch_page()
    
    # デバッグ出力: 取得したHTMLの長さを表示
    print("Fetched HTML Length:", len(html_content))
    
    # 取得したHTMLの一部を表示
    print(html_content[:1000])  # 最初の1000文字を表示