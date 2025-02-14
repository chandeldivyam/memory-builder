from typing import Generator
from .memory_layers.layers_factory import get_memory_layer
import os
import json


class MemoryManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MemoryManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, config):
        if not hasattr(self, 'initialized'):
            self.layers = []
            for layer_config in config['layers']:
                self.layers.append(get_memory_layer(layer_config))
            self.initialized = True

    def ingest(self, db, data):
        # To be processed parallelly by each layer
        for layer in self.layers:
            layer.ingest(db, data)

    def retrieve(self, db, query):
        # To be processed parallelly
        results = []
        for layer in self.layers:
            results.extend(layer.retrieve(db, query))
        return results

    @classmethod
    def get_instance(cls, config = None):
        if cls._instance is None:
            if config is None:
                raise ValueError("Memory Manager has not been initialized yet.")
            cls._instance = cls(config)

        return cls._instance

def get_memory_manager():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'manager.json')
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
    except (OSError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load configuration: {e}")
    
    return MemoryManager.get_instance(config=config)
