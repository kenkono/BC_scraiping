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

        # <li data-item="data-item"> タグをすべて抽出する
        items = soup.select('li[data-item="data-item"]')

        # 各アイテムから商品名、価格、ポイントを抽出する
        for item in items:
            name_tag = item.select_one('p.bcs_title a.bcs_item')
            price_tag = item.select_one('p.bcs_price')
            point_tag = item.select_one('p.bcs_point')

            name = name_tag.get_text(strip=True) if name_tag else 'NA'
            price = price_tag.get_text(strip=True) if price_tag else 'NA'
            point = point_tag.get_text(strip=True) if point_tag else 'NA'

            product_info = {
                'name': name,
                'price': price,
                'point': point
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
