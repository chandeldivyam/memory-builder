from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..memory.memory_nodes.base import MemoryNode


class MemoryRetriever(ABC):
    """Base class for memory retrievers."""
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY

    @abstractmethod
    async def retrieve(
        self,
        query: str,
        limit: int = 10,
        filter_criteria: Optional[Dict[str, Any]] = None
    ) -> List[MemoryNode]:
        """Retrieve relevant memory nodes for a query."""
        pass 