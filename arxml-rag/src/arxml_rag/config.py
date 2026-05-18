from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Qdrant
    qdrant_url: str = Field(default="http://localhost:6333")
    qdrant_collection: str = Field(default="arxml_rag")

    # Neo4j
    neo4j_uri: str = Field(default="bolt://localhost:7687")
    neo4j_user: str = Field(default="neo4j")
    neo4j_password: str = Field(default="password")

    # DuckDB
    duckdb_path: str = Field(default="data/processed/arxml.duckdb")

    # Embedding model
    embedding_model: str = Field(default="BAAI/bge-m3")
    embedding_dim: int = Field(default=1024)

    # Reranker
    reranker_model: str = Field(default="BAAI/bge-reranker-v2-m3")
    rerank_top_k: int = Field(default=5)

    # LLM
    openai_api_key: str = Field(default="")
    anthropic_api_key: str = Field(default="")
    llm_model: str = Field(default="claude-sonnet-4-6")

    # LangFuse
    langfuse_public_key: str = Field(default="")
    langfuse_secret_key: str = Field(default="")
    langfuse_host: str = Field(default="https://cloud.langfuse.com")

    # Supabase
    supabase_url: str = Field(default="")
    supabase_key: str = Field(default="")

    # Redis / Arq
    redis_url: str = Field(default="redis://localhost:6379")

    # API
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)
    log_level: str = Field(default="info")


settings = Settings()
