from bs4 import BeautifulSoup
from PageFetcher import PageFetcher
from CSVWriter import CSVWriter

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

        # デバッグ用に抽出した製品情報を出力
        print("Extracted products:", products)

        # 製品情報を返す
        return products

# 使用例
if __name__ == "__main__":
    fetcher = PageFetcher()
    extractor = ProductExtractor()

    # 1ページ目と2ページ目のHTMLコンテンツを取得
    pages_content = fetcher.fetch_pages(1, 2)

    # 各ページの製品名を抽出して表示
    all_products = []
    for content in pages_content:
        products = extractor.extract_products(content)
        all_products.extend(products)

    # 抽出した全製品情報を出力
    print("All extracted products:", all_products)

    # CSVWriterを使用して製品情報をCSVに書き込む
    from CSVWriter import CSVWriter
    csv_writer = CSVWriter()
    csv_writer.write_to_csv(all_products)
