"""
クラス名：ProductExtractor
説明：商品名、価格、ポイントを抜き出すクラス
"""
from bs4 import BeautifulSoup

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

            # 商品名を抽出、タグが存在しない場合は 'NA' を設定
            name = name_tag.get_text(strip=True) if name_tag else 'NA'
            # 価格を抽出、タグが存在しない場合は 'NA' を設定
            price = price_tag.get_text(strip=True) if price_tag else 'NA'
            # ポイントを抽出、タグが存在しない場合は 'NA' を設定
            point = point_tag.get_text(strip=True) if point_tag else 'NA'

            product_info = {
                'name': name,
                'price': price,
                'point': point
            }
            products.append(product_info)
        # 製品情報を返す
        return products

