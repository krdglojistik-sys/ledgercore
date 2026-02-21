from fastapi import APIRouter, HTTPException
from models import Invoice
from database import invoices_collection
from bson import ObjectId

router = APIRouter(prefix="/api/invoices", tags=["invoices"])

@router.get("/")
async def get_invoices():
    invoices = list(invoices_collection.find())
    for inv in invoices:
        inv["_id"] = str(inv["_id"])
    return invoices

@router.post("/")
async def create_invoice(invoice: Invoice):
    result = invoices_collection.insert_one(invoice.dict())
    return {"id": str(result.inserted_id), **invoice.dict()}

@router.get("/{invoice_id}")
async def get_invoice(invoice_id: str):
    invoice = invoices_collection.find_one({"_id": ObjectId(invoice_id)})
    if invoice:
        invoice["_id"] = str(invoice["_id"])
        return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")
