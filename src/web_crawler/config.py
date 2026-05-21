from pydantic import BaseModel, Field, HttpUrl


class CrawlConfig(BaseModel):
    seed_url: HttpUrl
    max_pages: int = Field(default=50, ge=1, le=10_000)
    max_depth: int = Field(default=2, ge=0, le=20)
    user_agent: str = "WebCrawlerBot/0.1"
    timeout_seconds: float = Field(default=10.0, gt=0, le=60)
