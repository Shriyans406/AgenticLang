from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    docs = load_all_documents("data")
    rag = RAGSearch()
    rag.build_index(docs)
    results = rag.search("What is attention mechanism?")
    print(f"Found {len(results)} results")
    