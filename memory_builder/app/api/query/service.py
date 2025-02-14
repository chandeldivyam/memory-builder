from app.memory.manager import get_memory_manager

#class for NodeService
class QueryService:
    def get_nodes(self, db, query):
        manager = get_memory_manager()
        return manager.retrieve(db, query)