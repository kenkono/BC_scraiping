# クラス図

```mermaid
classDiagram
    class Constants {
        +string BASE_URL
        +string ENCODED_QUERY
    }

    class ProductExtractor {
        +list extract_products(string html_content)
        +string extract_name(BeautifulSoup item)
        +string extract_price(BeautifulSoup item)
        +string extract_point(BeautifulSoup item)
    }

    class PageFetcher {
        +string fetch_page(int page_number)
        +list fetch_pages(int start_page, int end_page)
    }

    class CSVWriter {
        +void write_to_csv(list products, string filename)
    }

    class Main {
        +void main()
    }

    PageFetcher --> Constants : uses
    Main --> ProductExtractor : uses
    Main --> PageFetcher : uses
    Main --> CSVWriter : uses