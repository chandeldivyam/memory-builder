from abc import ABC, abstractmethod

class ChunkerConfig (ABC): 
    def __init__(self, config : dict):
        self.type = config['type']


class BaseChunker(ABC):
    @abstractmethod
    def chunk_text(self, text):
        pass

    def __call__(self, text):
        return self.chunk_text(text)
