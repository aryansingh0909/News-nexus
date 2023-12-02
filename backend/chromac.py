import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
chroma_client = chromadb.Client()
data = pd.read_csv('nyt-metadata.csv')
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key="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",
                model_name="text-embedding-ada-002"
            )

client = chromadb.Client()

# Create a collection in Chroma DB
collection = client.create_collection(name="nyt_times_collection")

documents = data['abstract'].tolist()[0:100]  # Assuming 'article_text' is a column in the dataset
documents_embeddings = openai_ef(documents)  
ids = data['web_url'].tolist()[0:100]
collection.add(documents=documents, ids=ids)

# query_embedding = openai_ef(query_document)  # Embedding vector for the query document
similar_documents = collection.query(
    query_texts=["Fifa"],
    n_results=5
)
print(similar_documents)
