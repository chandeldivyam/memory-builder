from .base import Retriever
from app.models.node import Node
from app.db.base import get_db
from sqlalchemy.sql import func

class NormalRAG(Retriever):
    def __init__(self, config):
        super().__init__("NormalRAG")
        print("retriever config", config)
        self.config = config

    def retrieve(self, db, query_embedding, n_results = 5) -> list[Node]:
        # Retrieve Node Embeddings from the PgVector Database
        nodes = db.query(Node).order_by(
            func.cosine_distance(Node.embedding, query_embedding)
        ).limit(n_results).all()
        return nodes[:n_results]

    def ingest(self, db, texts, data_embeddings) -> bool:
        # Convert data embeddings to Node Embeddings
        # Store Node Embeddings in the PgVector Database
        print("data_embeddings", len(data_embeddings))
        for text, data_embedding in zip(texts, data_embeddings):
            node = Node(text = text, embedding = data_embedding)
            db.add(node)
        db.commit()
        print("Ingested data embeddings")

    def clear(self):
        raise NotImplementedError("The 'clear' method is not implemented yet.")

    def list(self):
        raise NotImplementedError("The 'clear' method is not implemented yet.")