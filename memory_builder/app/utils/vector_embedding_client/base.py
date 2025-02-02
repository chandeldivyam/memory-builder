from abc import ABC, abstractmethod

class EmbeddingConfig(ABC):
    def __init__(self, config: dict):
        self.type = config['type']

    @abstractmethod
    def create_embedding(self):
        pass

class VectorEmbedding(ABC):
    @abstractmethod
    def get_embedding(self, text):
        pass

    def __call__(self, text):
        return self.get_embedding(text)