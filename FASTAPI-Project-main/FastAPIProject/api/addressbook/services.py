import imp
import addressbook.database as _database,addressbook.models as _models,addressbook.schemas as _schemas
import sqlalchemy.orm as _orm
def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_addressbook(db: _orm.Session,addressbook: _schemas._AddressBook):
    db_addressbook = _models.AddressBook(
         name= addressbook.name,
        phone = addressbook.phone,
        address = addressbook.address,
        city = addressbook.city,
        state = addressbook.state, 
        country = addressbook.country,
        longitude = addressbook.longitude,
        latitude = addressbook.latitude
    )

    db.add(db_addressbook)
    db.commit()
    db.refresh(db_addressbook)
    return db_addressbook


def get_address_by_id(db: _orm.Session, id: int):
    return db.query(_models.AddressBook).filter(_models.AddressBook.id== id).first()

def update_addressbook(db: _orm.Session,addressbookmodel: _models.AddressBook, addressbookschema : _schemas.AddressBook ):
    
    addressbookmodel.name= addressbookschema.name
    addressbookmodel.phone = addressbookschema.phone
    addressbookmodel.address = addressbookschema.address
    addressbookmodel.city = addressbookschema.city
    addressbookmodel.state = addressbookschema.state 
    addressbookmodel.country = addressbookschema.country
    addressbookmodel.longitude = addressbookschema.longitude
    addressbookmodel.latitude = addressbookschema.latitude
    
    db.commit()
    db.refresh(addressbookmodel)
    return addressbookmodel

def DeleteAddressBook(db: _orm.Session, id: int):
    db.query(_models.AddressBook).filter(_models.AddressBook.id== id).delete()
    db.commit()

def getaddressbooks(db: _orm.session):
    return db.query(_models.AddressBook).all()