from email import message
from typing import Optional
import fastapi as _fastapi
import uvicorn 
import addressbook.services as _services,addressbook.schemas as _schemas
import sqlalchemy.orm as _orm
  

_services.create_database()
app = _fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Greetings": "Welcome to Address Book. Please visit /docs to go to Swagger API documentation"}


@app.post("/addressbooks/", response_model=_schemas.AddressBook)
def create_addressbook(addressbook: _schemas._AddressBook,db:_orm.Session = _fastapi.Depends(_services.get_db)):
    db_addressbook = _services.create_addressbook(db,addressbook)
    return db_addressbook


@app.put("/addressbooks/", response_model=_schemas.AddressBook)
def update_addressbook(addressbook: _schemas.AddressBook,db:_orm.Session = _fastapi.Depends(_services.get_db)):
    db_address = _services.get_address_by_id(db=db, id= addressbook.id)
    if db_address:
        return _services.update_addressbook(db,db_address,addressbook)
    else:
        raise _fastapi.HTTPException(status_code = 404,detail = "Sorry this address book doesn't exists")


@app.delete("/addressbooks/{addressbookid}")
def delete_addressbook(addressbookid: int,db:_orm.Session = _fastapi.Depends(_services.get_db)):
    db_address = _services.get_address_by_id(db=db, id= addressbookid)
    if db_address:
        _services.DeleteAddressBook(db,addressbookid)
        return {"message":f"successfully deleted the address with id: {addressbookid}"}
    else:
        raise _fastapi.HTTPException(status_code = 404,detail = "Sorry this address book doesn't exists")


@app.get("/addressbooks/{addressbookid}")
def display_addressbook(addressbookid: Optional[int] = None,db:_orm.Session = _fastapi.Depends(_services.get_db)):
    #if addressbookid:
        db_address = _services.get_address_by_id(db=db, id= addressbookid)
        if db_address:
            return db_address
        else:
            return {"message":f"The address with id: {addressbookid} not found"}
    #else:
     #   return _services.getaddressbooks(db)

@app.get("/addressbooks/",response_model = list[_schemas.AddressBook])
def display_addressbooks(db:_orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.getaddressbooks(db)

if __name__ == "__main__":
    uvicorn.run("main:app",reload = True)