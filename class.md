# クラス図

## PageFetcherクラス

### メンバー変数
- `base_url`: str
  - 基本URLを保持する。
- `headers`: dict
  - HTTPリクエストヘッダーを保持する。

### メソッド
- `__init__(self)`
  - 基本URLとヘッダーを設定する。
- `fetch_page(self, page_number)`
  - 指定したページ番号の検索結果を取得する。