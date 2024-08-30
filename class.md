# PageFetcher クラス

## 概要
`PageFetcher` クラスは、指定されたページ番号の検索結果を取得するためのクラスです。

## メソッド

### `__init__()`
- コンストラクタ。基本URLとヘッダーを設定します。

### `fetch_page(page_number)`
- 指定したページ番号の検索結果を取得します。
- **引数**
  - `page_number` (int): 取得するページの番号。
- **戻り値**
  - `str`: ページのHTMLコンテンツ。

### `fetch_multiple_pages(page_numbers)`
- 複数のページ番号の検索結果を同時に取得します。
- **引数**
  - `page_numbers` (list of int): 取得するページ番号のリスト。
- **戻り値**
  - `dict`: 各ページ番号をキーとし、そのページのHTMLコンテンツを値とする辞書。
