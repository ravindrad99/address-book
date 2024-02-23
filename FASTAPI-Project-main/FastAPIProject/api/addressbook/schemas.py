import pydantic as _pydantic

class _AddressBook(_pydantic.BaseModel):
    name: str
    phone: str
    address: str
    city: str
    state: str
    country: str
    longitude: str 
    latitude: str

class AddressBook(_AddressBook):
    id: int

    class Config:
        orm_mode=True