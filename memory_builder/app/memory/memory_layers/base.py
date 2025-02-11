from abc import ABC, abstractmethod
from ..retrievers.retriever_factory import get_retriever
from utils.chunker.chunker_factory import get_chunker
from utils.vector_embedding_client.embedding_factory import get_embedding_client

class MemoryLayer(ABC):
    def __init__(self, name, config):
        self.name = name
        self.retriever = get_retriever(config['retriever_config'])
        self.chunker = get_chunker(config['chunker_config'])
        self.embedding_client = get_embedding_client(config['embedding_config'])

    @abstractmethod
    def ingest(self, data):
        pass

    @abstractmethod
    def retrieve(self, query):
        pass
