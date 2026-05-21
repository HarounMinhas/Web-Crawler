"""Web crawler package."""

from .config import CrawlConfig
from .crawler import DeterministicCrawler

__all__ = ["CrawlConfig", "DeterministicCrawler"]
