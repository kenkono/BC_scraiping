from bs4 import BeautifulSoup
from PageFetcher import PageFetcher

class ProductExtractor:
    def __init__(self):
        # 初期化処理（特に必要な場合）
        pass

    def extract_products(self, html_content):
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract all product names within the class 'bcs_item'
        product_names = soup.select('div.bcs_itemBox p.bcs_title a.bcs_item')

        # Print out each product name
        for product in product_names:
            print(product.get_text(strip=True))
# 使用例
if __name__ == "__main__":
    fetcher = PageFetcher()
    html_content = fetcher.fetch_page(1)

    # デバッグ出力: 取得したHTMLの長さを表示
    print("Fetched HTML Length:", len(html_content))

    extractor = ProductExtractor()
    products = extractor.extract_products(html_content)
