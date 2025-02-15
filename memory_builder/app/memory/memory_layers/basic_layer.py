from .base import MemoryLayer

class BasicLayer(MemoryLayer):
    def __init__(self, config):
        super().__init__("BasicLayer", config)

    def convert_to_embedding(self, data):
        chunked_data = self.chunker(data)
        return chunked_data, [self.embedding_client(text) for text in chunked_data]

    def ingest(self, db, data):
        chunked_data, data_embedding = self.convert_to_embedding(data)
        self.retriever.ingest(db, chunked_data, data_embedding)

    def retrieve(self, db, query) -> list:
        query_embedding = self.embedding_client(query)
        return self.retriever.retrieve(db, query_embedding)