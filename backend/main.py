from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from database import db, users_collection, contacts_collection, invoices_collection
from models import User, Contact, Invoice

load_dotenv()

app = FastAPI(title="LedgerCore API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "LedgerCore API çalışıyor", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Routes
from routes.auth import router as auth_router
from routes.contacts import router as contacts_router
from routes.invoices import router as invoices_router

app.include_router(auth_router)
app.include_router(contacts_router)
app.include_router(invoices_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
