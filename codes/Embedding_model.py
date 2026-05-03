import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Load a pre-trained model locally
# The model will download on the first run and be cached for future use.
# 'all-MiniLM-L6-v2' is fast, lightweight, and great for general use.
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define your text data
sentences = [
    "The data analyst processed the large dataset using Python.",
    "A senior lead is evaluating the impact of the new project.",
    "The weather in Ottawa is quite cold today.",
    "Automated reporting pipelines improve organizational efficiency."
]

# 3. Generate Embeddings
# This returns a numpy array of shape (num_sentences, embedding_dimension)
embeddings = model.encode(sentences)

print(f"Embedding Shape: {embeddings.shape}") # (4, 384) for this specific model

# 4. Calculate Similarity using Numpy
def cosine_similarity(a, b):
    # Formula: (a . b) / (||a|| * ||b||)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Compare the first sentence with the rest
query_embedding = embeddings[0]

print("\nSimilarity Scores to Sentence 1:")
for i, emb in enumerate(embeddings):
    score = cosine_similarity(query_embedding, emb)
    print(f"Sentence {i}: {score:.4f} | \"{sentences[i]}\"")