
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, LargeBinary
from sqlalchemy import create_engine, MetaData
from datetime import datetime
from pytz import timezone
Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payment'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    pinnumber = Column(Integer, nullable=False)
    visa = Column(Float, nullable=False)
    vpay = Column(Float, nullable=False)
    mastercard = Column(Float, nullable=False)
    maestro = Column(Float, nullable=False)
    registration_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))
    updated_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')), onupdate=datetime.now(timezone('Europe/Amsterdam')))
    

    def __repr__(self):
        return f"Payment('{self.id}','{self.pinnumber}', '{self.visa}', '{self.vpay}', '{self.mastercard}', '{self.maestro}', '{self.updated_date}')"
    

class Invoice(Base):
    __tablename__ = 'invoice'
    
    id = Column(Integer, autoincrement=True,primary_key=True)
    contact = Column(String(200),nullable=False)
    email = Column(String(200),nullable=False)
    amount = Column(Float,nullable=False)
    bussiness_name = Column(String(200),nullable=False)
    bussiness_code = Column(String,nullable=False)
    description = Column(String(500),nullable=False)
    status = Column(String(200),nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))
    updated_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')), onupdate=datetime.now(timezone('Europe/Amsterdam')))

    def __repr__(self):
        return f"Invoice('{self.id}','{self.contact}', '{self.email}', '{self.amount}', '{self.bussiness_name}', '{self.bussiness_code}', '{self.description}', '{self.status}', '{self.updated_date}')"


class GiftCard(Base):
    __tablename__ = 'gift_card'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(200))
    amount = Column(Float,nullable=False)
    description = Column(String(500))
    date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))
    updated_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')), onupdate=datetime.now(timezone('Europe/Amsterdam')))

    def __repr__(self):
        return f"GiftCard('{self.id}','{self.source}', '{self.amount}', '{self.description}', '{self.date}', '{self.updated_date}')"

class ExternalPayment(Base):
    __tablename__ = 'external_payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(200))
    amount = Column(Float,nullable=False)
    description = Column(String(500))
    date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))
    updated_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')), onupdate=datetime.now(timezone('Europe/Amsterdam')))

    def __repr__(self):
        return f"ExternalPayment('{self.id}','{self.source}', '{self.amount}', '{self.description}', '{self.date}', '{self.updated_date}')"

class VaultCash(Base):
    __tablename__ = 'vault_cash'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount100 = Column(Integer)
    amount50 = Column(Integer)
    amount20 = Column(Integer)
    amount10 = Column(Integer)
    amount5 = Column(Integer)
    amount2 = Column(Integer)
    amount1 = Column(Integer)
    amount050 = Column(Integer)
    amount020 = Column(Integer)
    amount010 = Column(Integer)
    amount005 = Column(Integer)
    date = Column(Date, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))
    updated_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')), onupdate=datetime.now(timezone('Europe/Amsterdam')))



    def __repr__(self):
        return f"VaultCash('{self.id}','{self.amount100}', '{self.amount50}', '{self.amount20}', '{self.amount10}', '{self.amount5}', '{self.amount2}', '{self.amount1}', '{self.amount050}', '{self.amount020}', '{self.amount010}', '{self.amount005}', '{self.date}', '{self.updated_date}')"
    
class KassaStrook(Base):
    __tablename__ = 'kassa_strook'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Hoofdgerechten_8000 = Column(Float)
    Nagerechten_8030 = Column(Float)
    Gebak_8040 = Column(Float)
    Kleine_kaart_8010 = Column(Float)
    Dagschotels_8020= Column(Float)
    Dranken_hoog_8100 = Column(Float)
    Frisdranken_overig_8200 = Column(Float)
    Koffie_8300 = Column(Float)
    Cultuurkaarten_4760 = Column(Float)
    Dagschotelabonnementer_2200 = Column(Float)
    Omzet_kadobonnen_2220 = Column(Float)
    Catering_8050 = Column(Float)
    Zaalhuur_8400 = Column(Float)
    date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))
    updated_date = Column(DateTime, nullable=False, default=datetime.now(timezone('Europe/Amsterdam')), onupdate=datetime.now(timezone('Europe/Amsterdam')))
    
    def __repr__(self):
        return f"KassaStrook('{self.id}','{self.Hoofdgerechten_8000}', '{self.Nagerechten_8030}', '{self.Gebak_8040}', '{self.Kleine_kaart_8010}', '{self.Dagschotels_8020}', '{self.Dranken_hoog_8100}', '{self.Frisdranken_overig_8200}', '{self.Koffie_8300}', '{self.Cultuurkaarten_4760}', '{self.Dagschotelabonnementer_2200}', '{self.Omzet_kadobonnen_2220}', '{self.Catering_8050}', '{self.Zaalhuur_8400}', '{self.date}', '{self.updated_date}')"

class EG(Base): # ! DONE
    __tablename__ = 'eg'
    id = Column(Integer, primary_key=True)
    EG_dranken_hoog = Column(Float)
    EG_dranken_laag = Column(Float)
    EG_Koffie = Column(Float)
    EG_Grote_kaart = Column(Float)
    EG_Kleine_kaart = Column(Float)
    EG_Dagschotels = Column(Float)
    EG_Nagerechten = Column(Float)
    EG_Gebak = Column(Float)
    date = Column(String(200), nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))


    def __repr__(self):
        return f"EG('{self.EG_dranken_hoog}', '{self.EG_dranken_laag}', '{self.EG_Koffie}', '{self.EG_Grote_kaart}', '{self.EG_Kleine_kaart}', '{self.EG_Dagschotels}', '{self.EG_Nagerechten}', '{self.EG_Gebak}', '{self.date}')"

class REPR(Base): # ! DONE
    __tablename__ = 'repr'
    id = Column(Integer, primary_key=True)
    REPR_dranken_hoog = Column(Float)
    REPR_dranken_laag = Column(Float)
    REPR_Koffie = Column(Float)
    REPR_Grote_kaart = Column(Float)
    REPR_Kleine_kaart = Column(Float)
    REPR_Dagschotels = Column(Float)
    REPR_Nagerechten = Column(Float)
    REPR_Gebak = Column(Float)
    date = Column(String(200), nullable=False, default=datetime.now(timezone('Europe/Amsterdam')))


    def __repr__(self):
        return f"REPR('{self.REPR_dranken_hoog}', '{self.REPR_dranken_laag}', '{self.REPR_Koffie}', '{self.REPR_Grote_kaart}', '{self.REPR_Kleine_kaart}', '{self.REPR_Dagschotels}', '{self.REPR_Nagerechten}', '{self.REPR_Gebak}', '{self.date}')"

# Define the database connection
engine = create_engine('sqlite:///samsam.db', echo=True)  # Change the URL according to your database type and credentials

# Create the table
Base.metadata.create_all(engine)
