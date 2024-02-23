import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import addressbook.database as _database

class AddressBook(_database.Base):
    __tablename__ = "Address Books"
    id = _sql.Column(_sql.Integer , primary_key = True, index = True)
    name = _sql.Column(_sql.String(length=50),nullable = False)
    phone = _sql.Column(_sql.String(length=14))
    address = _sql.Column(_sql.String(length=50))
    city = _sql.Column(_sql.String(length=50))
    state = _sql.Column(_sql.String(length=50))
    country = _sql.Column(_sql.String(length=50))
    longitude = _sql.Column(_sql.String(length=50))
    latitude = _sql.Column(_sql.String(length=50))

    def __repr__(self):
        return f'{self.name},{self.phone},{self.address}'