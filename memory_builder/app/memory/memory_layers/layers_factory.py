from .basic_layer import BasicLayer

def get_memory_layer(layer_config: dict):
    if layer_config["type"] == 'basic':
        return BasicLayer(layer_config)
    else:
        raise ValueError(f"Invalid layer type: {layer_config['type']}")