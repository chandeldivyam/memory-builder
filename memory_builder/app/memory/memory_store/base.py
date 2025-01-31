from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..memory_nodes.base import MemoryNode

class MemoryStore(ABC):
    """Base class for memory stores."""
    
    @abstractmethod
    async def add_node(self, node: MemoryNode) -> str:
        """Add a node to the store and return its ID."""
        pass
    
    @abstractmethod
    async def get_node(self, node_id: str) -> Optional[MemoryNode]:
        """Retrieve a node by its ID."""
        pass
    
    @abstractmethod
    async def search_nodes(
        self, 
        query_embedding: List[float], 
        limit: int = 10,
        filter_criteria: Optional[Dict[str, Any]] = None
    ) -> List[MemoryNode]:
        """Search for nodes using embedding similarity."""
        pass