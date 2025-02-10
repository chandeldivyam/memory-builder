from .azure_openai_embedding_client import AzureOpenAIEmbeddingConfig, AzureOpenAIEmbeddingClient

def get_embedding_client(config: dict):
    if config['type'] == 'azure_openai':
        return AzureOpenAIEmbeddingClient(AzureOpenAIEmbeddingConfig(config))
    else:
        raise ValueError("Unknown embedding client type")