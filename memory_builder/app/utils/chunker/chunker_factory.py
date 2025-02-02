from memory_builder.app.utils.chunker.raw_chunker import RawChunker, RawChunkerConfig

def get_chunker(config : dict):
    if config["chunker_type"] == "raw":
        return RawChunker(RawChunkerConfig(config))
    else:
        raise ValueError("Unknown chunker type")