from .base import MemoryLayer

class BasicLayer(MemoryLayer):
    def __init__(self, config):
        super().__init__("BasicLayer", config)

    def convert_to_embedding(self, data):
        data = self.chunker(data)
        return [self.embedding_client(text) for text in data]

    def ingest(self, data):
        data_embedding = self.convert_to_embedding(data)
        self.retriever.ingest(data_embedding)

    def retrieve(self, query) -> list:
        query_embedding = self.embedding_client(query)
        return self.retriever.retrieve(query_embedding)