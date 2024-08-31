from bs4 import BeautifulSoup
from PageFetcher import PageFetcher

class ProductExtractor:
    def __init__(self):
        # 初期化処理（特に必要な場合）
        pass

    def extract_products(self, html_content):
        products = []
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract all product names within the class 'bcs_item'
        product_names = soup.select('div.bcs_itemBox p.bcs_title a.bcs_item')

        for product in product_names:
            products.append(product.get_text(strip=True))
        # 製品名を返す
        print(products)
        return products




# 使用例
if __name__ == "__main__":
    fetcher = PageFetcher()
    extractor = ProductExtractor()

    # 1ページ目と2ページ目のHTMLコンテンツを取得
    pages_content = fetcher.fetch_pages(1, 2)

    # 各ページの製品名を抽出して表示
    for content in pages_content:
        extractor.extract_products(content)
