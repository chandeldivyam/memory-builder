from .raw_chunker import RawChunker, RawChunkerConfig

def get_chunker(config : dict):
    if config["type"] == "raw":
        return RawChunker(RawChunkerConfig(config))
    else:
        raise ValueError("Unknown chunker type")