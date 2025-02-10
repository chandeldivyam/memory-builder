from .base import EmbeddingConfig, VectorEmbedding
from typing import Any, Dict, List
import os

from openai import AzureOpenAI
from app.core.config import settings

class AzureOpenAIEmbeddingConfig(EmbeddingConfig):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model_name = config['model_name']
        self.key_auth = config['key_auth'] == True


class AzureOpenAIEmbeddingClient(VectorEmbedding):
    def __init__(self, config: AzureOpenAIEmbeddingConfig):
        self.config = config
        self.client = None
        if self.config.key_auth:
            try:
                key =settings.AZURE_OPENAI_EMBEDDINGS_KEY
                version =settings.AZURE_OPENAI_EMBEDDINGS_VERSION
                endpoint_url = settings.AZURE_OPENAI_EMBEDDINGS_ENDPOINT_URL
            except KeyError:
                print("Missing environment variable 'AZURE_OPENAI_EMBEDDINGS_KEY'")
                print("Set it before running this sample.")
                exit()
            self.client = AzureOpenAI(
                            api_key = key,  
                            api_version = version,
                            azure_endpoint = endpoint_url
                            )
        else:
            Exception ("Not supported yet")

    def get_embedding(self, text: str):
        response = self.client.embeddings.create(input=[text], model=self.config.model_name).data[0].embedding
        return response