import chromadb
from chromadb.utils import embedding_functions

# 1. Initialize the persistent client (saves data to your local disk)
client = chromadb.PersistentClient(path="./chroma_data")

# 2. Define the embedding model (using the same one from your README)
# This uses the SentenceTransformer library under the hood locally.
model_name = "all-MiniLM-L6-v2"
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

# 3. Create or get a collection (like a table in SQL)
collection = client.get_or_create_collection(
    name="project_docs", 
    embedding_function=embedding_func
)

# 4. Prepare data with metadata (for advanced filtering)
documents = [
    "Mei handles PDF extraction and calendar sync in OpenClaw.",
    "John is responsible for research and technical troubleshooting.",
    "Sam specializes in financial intelligence and market trends.",
    "The system uses ChromaDB for persistent vector storage."
]

metadatas = [
    {"agent": "Mei", "type": "automation"},
    {"agent": "John", "type": "research"},
    {"agent": "Sam", "type": "finance"},
    {"agent": "System", "type": "infrastructure"}
]

ids = ["agent_01", "agent_02", "agent_03", "sys_01"]

# 5. Add documents (Chroma handles the embedding generation automatically)
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

# 6. Perform a Semantic Query
results = collection.query(
    query_texts=["Who deals with financial data?"],
    n_results=1
)

print(f"Top Match: {results['documents'][0][0]}")
print(f"Metadata: {results['metadatas'][0][0]}")