from abc import ABC, abstractmethod

class Retriever(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def retrieve(self, query_embedding, n_results)  -> list:
        pass

    @abstractmethod
    def ingest(self, data_embeddings) -> bool:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def list(self):
        pass