from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CrawlResult:
    url: str
    depth: int
    status_code: int
    title: str
