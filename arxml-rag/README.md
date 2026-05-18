# arxml-rag

RAG + GraphRAG system over AUTOSAR Classic ARXML files.

## Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Package manager | uv |
| API | FastAPI |
| Models | Pydantic v2 |
| Vector store | Qdrant |
| Graph store | Neo4j Community |
| Exact search | DuckDB |
| Embeddings | BGE-m3 |
| Reranker | BGE-reranker-v2-m3 |
| Agents | PydanticAI |
| Observability | LangFuse |
| Evaluation | Ragas + DeepEval |
| Task queue | Arq + Redis |
| Database | Supabase Postgres |

## Quick start

```bash
# 1. Start infrastructure
docker compose up -d

# 2. Install dependencies
uv sync

# 3. Copy and fill env
cp .env.example .env

# 4. Run the API
uv run uvicorn arxml_rag.api:app --reload
```

## Project layout

```
src/arxml_rag/
  config.py        # Pydantic Settings — all env vars in one place
  models/          # Frozen Pydantic domain models (SWC, Port, Signal, …)
  parsers/         # ARXML → typed objects via lxml
  enrichment/      # Typed objects → natural-language descriptions
  indexing/        # Writers for Qdrant, DuckDB, Neo4j
  retrieval/       # Hybrid retriever + BGE reranker
  agents/          # PydanticAI query-router agent
  generation/      # Answer synthesis with citations
  api/             # FastAPI /query and /ingest endpoints
tests/
scripts/           # One-off ingestion & maintenance scripts
data/
  raw/             # gitignored — original ARXML files
  processed/       # gitignored — DuckDB, embeddings cache
```

## Development

```bash
uv run ruff check src tests
uv run mypy
uv run pytest
```
