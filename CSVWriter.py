"""
クラス名：CSVWriter
説明：CSV出力クラス。ファイル名の区別をつけるために日付とversion情報をファイル名につけるようにしています。
"""
import csv
from datetime import datetime
import os
import re

class CSVWriter:
    def __init__(self):
        # 現在の日付を取得
        self.date_str = datetime.now().strftime('%Y%m%d')
        self.filename = self.generate_filename()

    def generate_filename(self):
        # ファイル名のパターンを定義
        pattern = re.compile(rf'ver(\d+)_{self.date_str}_products\.csv')
        version = 1

        # カレントディレクトリのファイルをチェック
        for file in os.listdir('.'):
            match = pattern.match(file)
            if match:
                current_version = int(match.group(1))
                if current_version >= version:
                    version = current_version + 1

        # 新しいファイル名を生成
        return f'ver{version}_{self.date_str}_products.csv'

    def write_to_csv(self, products):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'point'])
            writer.writeheader()
            for product in products:
                writer.writerow(product)
