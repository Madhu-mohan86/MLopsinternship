from langflow import load_flow_from_json
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import pymongo
from bson import ObjectId

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["your_database_name"]
collection = db["Results"]

flow = load_flow_from_json("/home/sirius/ex.json")

# Get user input
prompt = input("Enter your question : ")

# Run the flow with the input prompt
result = flow([prompt])

print("the answer is",result)

# Generate a unique ID using ObjectId
unique_id = str(ObjectId())

# Prepare the result item for database insertion
result_item = {
    '_id': unique_id,
    'input': prompt,
    'output': result,
}

# Insert result into the database
collection.insert_one(result_item)

# Retrieve texts from the database for embeddings
docs = list(collection.find())

texts = [doc['input'] for doc in docs]


# Initialize OpenAI model for embeddings
llm = OpenAI(temperature=0.7)  # Adjust temperature as needed
embeddings = OpenAIEmbeddings(llm=llm)
embeddings = embeddings.embed_documents(texts)

# Create Chroma vector store and persist it
db = Chroma.from_documents(docs, embeddings, persist_directory="db")
db.persist()

