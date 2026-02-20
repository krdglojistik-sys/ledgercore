from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class User(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()))
    email: str
    password: str
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Contact(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()))
    name: str
    tax_no: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    contact_type: str = "customer"
    balance: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)

class InvoiceItem(BaseModel):
    product_name: str
    quantity: float
    unit_price: float
    total: float

class Invoice(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()))
    invoice_no: str
    contact_id: str
    contact_name: str
    date: datetime
    due_date: Optional[datetime] = None
    items: List[InvoiceItem] = []
    sub_total: float = 0.0
    tax_total: float = 0.0
    total: float = 0.0
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
