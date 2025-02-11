from .normal_rag import NormalRag

def get_retriever(retriever_config):
    if retriever_config["type"] == 'normal_rag':
        return NormalRag(retriever_config)
    else:
        raise ValueError(f"Invalid retriever type: {retriever_config['type']}")