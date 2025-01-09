import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path=r'D:\Tejas MSC\MSC Project\Cold Email Generator\app\resources\my_portfolio.csv'):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if self.collection.count() == 0:  # clearer condition check
            documents = self.data["Techstack"].tolist()
            metadatas = [{"links": links} for links in self.data["Links"]]
            ids = [str(uuid.uuid4()) 
            
            for _ in range(len(documents))]  
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )


    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
