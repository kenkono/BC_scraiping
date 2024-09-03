"""
クラス名：main
説明：メイン処理を行うクラス
"""
from PageFetcher import PageFetcher
from ProductExtractor import ProductExtractor
from CSVWriter import CSVWriter


def main():
    fetcher = PageFetcher()
    extractor = ProductExtractor()

    # 1ページ目と2ページ目のHTMLコンテンツを取得
    pages_content = fetcher.fetch_pages(1, 2)

    # 各ページの製品名を抽出して表示
    all_products = []
    for content in pages_content:
        products = extractor.extract_products(content)
        all_products.extend(products)

    # CSVWriterを使用して製品情報をCSVに書き込む
    csv_writer = CSVWriter()
    csv_writer.write_to_csv(all_products)

if __name__ == "__main__":
    main()