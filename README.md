# Web-Crawler

Production-ready foundation for a deterministic, testable web crawler.

## Local development

```bash
./scripts/bootstrap.sh
source .venv/bin/activate
ruff check .
mypy src
pytest
```

## Architecture

- Core package: `src/web_crawler/`
- ADRs: `docs/adr/`
- CI checks: `.github/workflows/ci.yml`

Determinism constraints are documented in ADR 0002.
