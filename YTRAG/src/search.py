from typing import List, Any, Optional
from src.vectorstore import FaissVectorStore
from src.embedding import EmbeddingPipeline

class RAGSearch:
    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2", chunk_size: int = 1000, chunk_overlap: int = 200):
        self.vector_store = FaissVectorStore(persist_dir=persist_dir, embedding_model=embedding_model, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.embedding_pipeline = EmbeddingPipeline(model_name=embedding_model, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    
    def build_index(self, documents):
        self.vector_store.build_from_documents(documents)
    
    def search(self, query: str, top_k: int = 5) -> List[Any]:
        return self.vector_store.query(query, top_k=top_k)