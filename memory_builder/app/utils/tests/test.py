from ..chunker.chunker_factory import get_chunker
from ..vector_embedding_client.embedding_factory import get_embedding_client

def get_chunker_and_embedding(config: dict):
    chunker = get_chunker(config["chunker_config"])
    embedding_client = get_embedding_client(config["embedding_config"])
    return chunker, embedding_client

config = {
    "chunker_config": {
        "type": "raw",
        "max_len": 10
    },
    "embedding_config": {
        "type": "azure_openai",
        "model_name": "text-embedding-3-large",
        "key_auth": True
    }
}

if __name__ == "__main__":
    chunker, embedding_client = get_chunker_and_embedding(config)

    print(chunker.chunk_text("This is a test, this is only a test. If this were a real emergency, you would be instructed to... do something else."))
    print(embedding_client.get_embedding("This is a test, this is only a test. If this were a real emergency, you would be instructed to... do something else."))