from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
warnings.filterwarnings('ignore')

embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
vectordb = Chroma(persist_directory='./college_db', embedding_function=embeddings)

queries = [
    'What courses does MCOET offer?',
    'Tell me about fees and admission',
    'What is the placement record?'
]

print("\n=== DATABASE RETRIEVAL TEST ===\n")
for q in queries:
    docs = vectordb.similarity_search(q, k=2)
    print("Query:", q)
    print("Found:", len(docs), "documents")
    if docs:
        source = docs[0].metadata.get('source', 'unknown')
        preview = docs[0].page_content[:200]
        print("Source:", source)
        print("Preview:", preview[:100] + "...")
        print()
