from .base import MemoryLayer

class BasicLayer(MemoryLayer):
    def __init__(self, config):
        super().__init__("BasicLayer", config)

    def ingest(self, data):
        pass

    def retrieve(self, query):
        pass