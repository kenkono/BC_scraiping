from bs4 import BeautifulSoup
from PageFetcher import PageFetcher

class ProductExtractor:
    def __init__(self):
        # 初期化処理（特に必要な場合）
        pass

    def extract_products(self, html_content):
        products = []

        # BeautifulSoupを使用してHTMLコンテンツを解析する
        soup = BeautifulSoup(html_content, 'html.parser')

        # クラス 'bcs_itemBox' 内の 'bcs_title' を持つすべての製品名を抽出する
        product_names = soup.select('div.bcs_itemBox p.bcs_title a.bcs_item')
        # クラス 'bcs_price' を持つすべての価格を抽出する
        prices = soup.select('p.bcs_price')
        # クラス 'bcs_point' を持つすべてのポイントを抽出する
        points = soup.select('p.bcs_point')

        # 製品名、価格、ポイントをリストに格納する
        for name, price, point in zip(product_names, prices, points):
            product_info = {
                'name': name.get_text(strip=True),
                'price': price.get_text(strip=True),
                'point': point.get_text(strip=True)
            }
            products.append(product_info)

        # 製品情報を返す
        print(products)
        return products




# 使用例
if __name__ == "__main__":
    fetcher = PageFetcher()
    extractor = ProductExtractor()

    # 1ページ目と2ページ目のHTMLコンテンツを取得
    pages_content = fetcher.fetch_pages(1, 3)

    # 各ページの製品名を抽出して表示
    for content in pages_content:
        extractor.extract_products(content)
