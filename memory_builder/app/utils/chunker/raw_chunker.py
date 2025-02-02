from .base_chunker import BaseChunker, ChunkerConfig
from typing import List

class RawChunkerConfig(ChunkerConfig):
    def __init__(self, config: dict):
        super().__init__(config)
        self.max_len = config['max_len']

class RawChunker(BaseChunker):
    def __init__(self, config: RawChunkerConfig):
        self.config = config

    def chunk_text(self, text: str) -> List[str]:
        max_len = self.config.max_len
        return [text[i:i + max_len] for i in range(0, len(text), max_len)]