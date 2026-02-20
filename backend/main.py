from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.contacts import router as contacts_router
from routes.invoices import router as invoices_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
<<<<<<< HEAD
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
=======
def root():
    return {"message": "LedgerCore API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(contacts_router, prefix="/contacts", tags=["contacts"])
app.include_router(invoices_router, prefix="/invoices", tags=["invoices"])
>>>>>>> c01cda3fbf4e6c5a8e3903e80e1096366fbaa8e9
