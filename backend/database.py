from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database()

# Koleksiyonlar
users_collection = db.users
contacts_collection = db.contacts
invoices_collection = db.invoices
products_collection = db.products
transactions_collection = db.transactions
