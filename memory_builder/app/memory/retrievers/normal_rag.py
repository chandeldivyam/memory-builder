from .base import Retriever

class NormalRAG(Retriever):
    def __init__(self, config):
        super().__init__("NormalRAG")
        self.config = config

    def retrieve(self, query_embedding, n_results = 5) -> list:
        # Retrieve Node Embeddings from the PgVector Database
        # Return the top n_results Node Embeddings 
        pass

    def store(self, data_embeddings) -> bool:
        # Convert data embeddings to Node Embeddings
        # Store Node Embeddings in the PgVector Database
        pass

    def clear(self):
        raise NotImplementedError("The 'clear' method is not implemented yet.")

    def list(self):
        raise NotImplementedError("The 'clear' method is not implemented yet.")