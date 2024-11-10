import pymongo
import gridfs

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]

# Create GridFS instance
fs = gridfs.GridFS(db)

# Insert userID and PDF
user_id = "user123"  # Example userID

# Read the PDF file
with open("your_document.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()

# Store the PDF in GridFS
pdf_id = fs.put(pdf_data, filename="your_document.pdf", user_id=user_id)

# Optionally, store userID and PDF reference in a collection
db.your_collection_name.insert_one({
    "user_id": user_id,
    "pdf_id": pdf_id
})

print(f"PDF inserted with ID: {pdf_id}")
