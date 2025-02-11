from .memory_layers.layers_factory import get_memory_layer


class MemoryManager:
    def __init__(self, config):
        self.layers = []
        for layer_config in config['layers']:
            self.layers.append(get_memory_layer(layer_config))

    def ingest(self, data):
        for layer in self.layers:
            layer.ingest(data)

    def retrieve(self, query):
        results = []
        for layer in self.layers:
            results.extend(layer.retrieve(query))
        return results

