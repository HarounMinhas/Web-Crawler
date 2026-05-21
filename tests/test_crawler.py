from web_crawler.config import CrawlConfig
from web_crawler.crawler import DeterministicCrawler


def test_extract_links_sorted_and_same_host() -> None:
    crawler = DeterministicCrawler(CrawlConfig(seed_url="https://example.com"))
    html = """
    <html><body>
      <a href='/b'>B</a>
      <a href='/a'>A</a>
      <a href='https://example.com/c?x=1'>C</a>
      <a href='https://other.com/nope'>Nope</a>
    </body></html>
    """
    links = crawler._extract_links(html, "https://example.com", "example.com")
    assert links == [
        "https://example.com/a",
        "https://example.com/b",
        "https://example.com/c",
    ]


def test_normalize_url_removes_fragment_and_query() -> None:
    crawler = DeterministicCrawler(CrawlConfig(seed_url="https://example.com"))
    assert crawler._normalize_url("https://example.com/path?x=1#here") == "https://example.com/path"
