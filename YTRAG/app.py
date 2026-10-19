from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
# from src.vectorstore import FaissVectorStore
# from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    doc=load_all_documents("data")
    chunks=EmbeddingPipeline().chunk_documents(doc)
    chunkvectors=EmbeddingPipeline().embed_chunks(chunks)
    print(chunkvectors)
    