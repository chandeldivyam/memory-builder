from .base import Retriever
from app.models.node import Node, N_DIM
from app.db.base import get_db
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from sqlalchemy import cast
from app.schemas.node import Node as PydanticNode
from app.schemas.query import QueryResponse, QueryResult
import uuid

class NormalRAG(Retriever):
    def __init__(self, config):
        super().__init__("NormalRAG")
        print("retriever config", config)
        self.similarity_threshold = config["similarity_threshold"]
        self.config = config

    def retrieve(self, db, query_embedding, n_results = 1) -> list[Node]:
        query_embedding_vector = cast(query_embedding, Vector(N_DIM))
        # Compute the cosine similarity between the query embedding and the Node Embeddings
        nodes = db.query(Node, func.cosine_distance(Node.embedding, query_embedding_vector).label('distance')).filter(
        func.cosine_distance(Node.embedding, query_embedding_vector) < self.similarity_threshold).order_by('distance').limit(n_results).all()
        
        results = [
            QueryResult(node=PydanticNode.from_orm(node), distance=distance)
            for node, distance in nodes
        ]

        return QueryResponse(results=results)

    def ingest(self, db, texts, data_embeddings) -> bool:
        # Convert data embeddings to Node Embeddings
        # Store Node Embeddings in the PgVector Database
        print("data_embeddings", len(data_embeddings))
        for text, data_embedding in zip(texts, data_embeddings):
            node = Node(id=str(uuid.uuid4()), text = text, embedding = data_embedding)
            db.add(node)
        db.commit()
        print("Ingested data embeddings")

    def clear(self):
        raise NotImplementedError("The 'clear' method is not implemented yet.")

    def list(self):
        raise NotImplementedError("The 'clear' method is not implemented yet.")