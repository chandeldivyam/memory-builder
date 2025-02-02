from .base import EmbeddingConfig, VectorEmbedding
from typing import Any, Dict, List
import os

from azure.ai.inference import EmbeddingsClient


class AzureOpenAIEmbeddingConfig(EmbeddingConfig):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model_name = config['model_name']
        self.endpoint_url = config['endpoint_url']
        self.key_auth = config['key_auth'] == 'True'


class AzureOpenAIEmbeddingClient(VectorEmbedding):
    def __init__(self, config: AzureOpenAIEmbeddingConfig):
        self.config = config
        self.client = None
        if self.config.key_auth:
            from azure.core.credentials import AzureKeyCredential

            try:
                key = os.environ["AZURE_OPENAI_EMBEDDINGS_KEY"]
                version = os.environ["AZURE_OPENAI_EMBEDDINGS_VERSION"]
            except KeyError:
                print("Missing environment variable 'AZURE_OPENAI_EMBEDDINGS_KEY'")
                print("Set it before running this sample.")
                exit()

            self.client = EmbeddingsClient(endpoint=config.endpoint_url, credential=AzureKeyCredential(key), api_version=version)

        else:
            from azure.identity import DefaultAzureCredential
            self.client = EmbeddingsClient(config.endpoint_url, DefaultAzureCredential())

    def get_embedding(self, text: str):
        response = self.client.embed(text, model_name=self.config.model_name)
        return 
        
    def get_embeddings(self, texts: List[str]):
        response = self.client.embed(texts, model_name=self.config.model_name)
        return response