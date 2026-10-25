import json

p = 'YTRAG/agenticrag/1-agenticrag.ipynb'
nb = json.load(open(p, encoding='utf-8'))

cell_sources = [
    "import os\nfrom typing import TypedDict, List\nfrom langgraph.graph import StateGraph, END\nfrom langchain_openai import ChatOpenAI, OpenAIEmbeddings\nfrom langchain_community.vectorstores import FAISS\nfrom langchain_text_splitters import RecursiveCharacterTextSplitter\nfrom langchain_core.schema import Document\n",
    "from dotenv import load_dotenv\nload_dotenv()\n",
    "os.environ[\"OPENAI_API_KEY\"] = os.getenv(\"OPENAI_API_KEY\")\n\nllm = ChatOpenAI(\n    model=\"openai/gpt-oss-120b\",\n    temperature=0,\n    base_url=\"https://api.groq.com/openai/v1\",\n    api_key=os.getenv(\"GROQ_API_KEY\"),\n)\nembeddings = OpenAIEmbeddings()\n",
    "llm\n",
    "class AgentState(TypedDict):\n    question: str\n    documents: List[Document]\n    answer: str\n    needs_retrieval: bool\n",
    "sample_texts = [\n    \"LangGraph is a library for building stateful, multi-actor applications with LLMs. It extends LangChain with the ability to coordinate multiple chains across multiple steps of computation in a cyclic manner.\",\n    \"RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with text generation. It retrieves relevant documents and uses them to provide context for generating more accurate responses.\",\n    \"Vector databases store high-dimensional vectors and enable efficient similarity search. They are commonly used in RAG systems to find relevant documents based on semantic similarity.\",\n    \"Agentic systems are AI systems that can take actions, make decisions, and interact with their environment autonomously. They often use planning and reasoning capabilities.\"\n]\n\ndocuments=[Document(page_content=text) for text in sample_texts]\n\n##create vector store\nvectorstore = FAISS.from_documents(documents, embeddings)\nretriever = vectorstore.as_retriever(k=3)\n",
    "def decide_retrieval(state: AgentState) -> AgentState:\n    \"\"\"\n    Decide if we need to retrieve documents based on the question\n    \"\"\"\n    question = state[\"question\"]\n    \n    # Simple heuristic: if question contains certain keywords, retrieve\n    retrieval_keywords = [\"what\", \"how\", \"explain\", \"describe\", \"tell me\"]\n    needs_retrieval = any(keyword in question.lower() for keyword in retrieval_keywords)\n    \n    return {**state, \"needs_retrieval\": needs_retrieval}\n",
    "def retrieve_documents(state: AgentState) -> AgentState:\n    \"\"\"\n    Retrieve relevant documents based on the question\n    \"\"\"\n    question = state[\"question\"]\n    documents = retriever.invoke(question)\n    \n    return {**state, \"documents\": documents}\n",
    "def generate_answer(state: AgentState) -> AgentState:\n    \"\"\"\n    Generate an answer using the retrieved documents or direct response\n    \"\"\"\n    question = state[\"question\"]\n    documents = state.get(\"documents\", [])\n    \n    if documents:\n        context = \"\\n\\n\".join([doc.page_content for doc in documents])\n        prompt = f\"\"\"Based on the following context, answer the question:\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:\"\"\"\n    else:\n        prompt = f\"Answer the following question: {question}\"\n    \n    response = llm.invoke(prompt)\n    answer = response.content\n    \n    return {**state, \"answer\": answer}\n",
]

for i, src in enumerate(cell_sources):
    if i < len(nb['cells']) and nb['cells'][i]['cell_type'] == 'code':
        nb['cells'][i]['source'] = src.splitlines(keepends=True)

json.dump(nb, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
open(p, 'a', encoding='utf-8').write('\n')
print('updated', p)
