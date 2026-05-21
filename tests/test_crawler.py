import httpx

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


def test_extract_links_treats_hostname_case_insensitive() -> None:
    crawler = DeterministicCrawler(CrawlConfig(seed_url="https://example.com"))
    html = """
    <html><body>
      <a href='https://EXAMPLE.com/a'>A</a>
      <a href='https://Example.Com/b'>B</a>
    </body></html>
    """
    links = crawler._extract_links(html, "https://example.com", "example.com")
    assert links == ["https://EXAMPLE.com/a", "https://Example.Com/b"]


def test_normalize_url_removes_fragment_and_query() -> None:
    crawler = DeterministicCrawler(CrawlConfig(seed_url="https://example.com"))
    assert crawler._normalize_url("https://example.com/path?x=1#here") == "https://example.com/path"


def test_crawl_continues_after_request_error() -> None:
    crawler = DeterministicCrawler(CrawlConfig(seed_url="https://example.com", max_pages=10, max_depth=2))

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/":
            return httpx.Response(
                200,
                text="<a href='/ok'>ok</a><a href='/bad'>bad</a>",
                request=request,
            )
        if request.url.path == "/ok":
            return httpx.Response(200, text="<title>OK</title>", request=request)
        raise httpx.ConnectError("boom", request=request)

    transport = httpx.MockTransport(handler)
    original_client = httpx.Client

    def build_client(*args: object, **kwargs: object) -> httpx.Client:
        kwargs["transport"] = transport
        return original_client(*args, **kwargs)

    httpx.Client = build_client  # type: ignore[assignment]
    try:
        results = crawler.crawl()
    finally:
        httpx.Client = original_client  # type: ignore[assignment]

    assert [result.url for result in results] == [
        "https://example.com/",
        "https://example.com/bad",
        "https://example.com/ok",
    ]
    assert results[1].status_code == 0
    assert results[2].status_code == 200
