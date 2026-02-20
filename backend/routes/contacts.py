from fastapi import APIRouter, HTTPException
from models import Contact
from database import contacts_collection
from bson import ObjectId

router = APIRouter(prefix="/api/contacts", tags=["contacts"])

@router.get("/")
async def get_contacts():
        contacts = list(contacts_collection.find())
            for c in contacts:
                        c["_id"] = str(c["_id"])
                            return contacts
                            @router.post("/")
                            async def create_contact(contact: Contact):
                                    result = contacts_collection.insert_one(contact.dict())
                                        return {"id": str(result.inserted_id), **contact.dict()}

                                        @router.get("/{contact_id}")
                                        async def get_contact(contact_id: str):
                                                contact = contacts_collection.find_one({"_id": ObjectId(contact_id)})
                                                    if contact:
                                                                contact["_id"] = str(contact["_id"])
                                                                        return Contact    raise HTTPException(status_code=404, detail="Contact not found")
