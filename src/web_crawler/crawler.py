from __future__ import annotations

from collections import deque
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup

from .config import CrawlConfig
from .models import CrawlResult


class DeterministicCrawler:
    """Breadth-first crawler with deterministic URL ordering."""

    def __init__(self, config: CrawlConfig) -> None:
        self._config = config

    def crawl(self) -> list[CrawlResult]:
        origin = str(self._config.seed_url)
        host = self._normalize_host(origin)
        queue: deque[tuple[str, int]] = deque([(origin, 0)])
        visited: set[str] = set()
        output: list[CrawlResult] = []

        headers = {"User-Agent": self._config.user_agent}
        with httpx.Client(timeout=self._config.timeout_seconds, headers=headers) as client:
            while queue and len(output) < self._config.max_pages:
                current_url, depth = queue.popleft()
                if current_url in visited or depth > self._config.max_depth:
                    continue

                visited.add(current_url)
                try:
                    response = client.get(current_url)
                except httpx.RequestError:
                    output.append(
                        CrawlResult(
                            url=current_url,
                            depth=depth,
                            status_code=0,
                            title="",
                        )
                    )
                    continue

                title = self._extract_title(response.text)
                output.append(
                    CrawlResult(
                        url=current_url,
                        depth=depth,
                        status_code=response.status_code,
                        title=title,
                    )
                )

                for child in self._extract_links(response.text, current_url, host):
                    if child not in visited:
                        queue.append((child, depth + 1))

        return output

    def _extract_title(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("title")
        return title.get_text(strip=True) if title else ""

    def _extract_links(self, html: str, base_url: str, host: str) -> list[str]:
        soup = BeautifulSoup(html, "html.parser")
        links: set[str] = set()
        for anchor in soup.find_all("a", href=True):
            href = anchor.get("href")
            if isinstance(href, str) and href:
                links.add(self._normalize_url(urljoin(base_url, href)))
        filtered = [url for url in links if self._normalize_host(url) == host]
        return sorted(filtered)

    def _normalize_url(self, url: str) -> str:
        parsed = urlparse(url)
        path = parsed.path or "/"
        return parsed._replace(fragment="", query="", path=path).geturl()

    def _normalize_host(self, url: str) -> str:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        port = parsed.port
        if port is None:
            return hostname.lower()
        return f"{hostname.lower()}:{port}"
