from .normal_rag import NormalRAG

def get_retriever(retriever_config):
    if retriever_config["type"] == 'normal_rag':
        return NormalRAG(retriever_config)
    else:
        raise ValueError(f"Invalid retriever type: {retriever_config['type']}")