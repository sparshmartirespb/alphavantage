from sqlalchemy import create_engine
from sqlalchemy import Column, Float, ForeignKey, Index, Integer, Table, Text, text, and_
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
# from project_alphavantage.config.base import (
#     BASE_DIR
# )

SQLITE = 'sqlite'
Base = declarative_base()
metadata = Base.metadata





class StockImport(Base):
    __tablename__ = 'stock_import'
    
    
    date = Column(Text, nullable=False)
    
    close = Column(Float, nullable=False, default=text("0"))
    open = Column(Float, primary_key=True, nullable=False, default=text("0"))
    high = Column(Float, nullable=False, default=text("0"))
    low = Column(Float, nullable=False, default=text("0"))
    volume = Column(Float, nullable=False, default=text("0"))
    stock = Column(Text, nullable=False)
    
    
    @staticmethod
    def save_or_update_stock_imports(date: str, close: float, open:float,high:float,low:float,volume:float,stock: str):
        Session = sessionmaker(bind=AlphaVantageDB(dbtype='sqlite', dbname='alphavantage').db_engine)        
        session = Session()
        stock_import = session.query(StockImport).filter(and_(StockImport.date == date, StockImport.stock == stock))
        try:
            if stock_import.one():
                stock_import.one().close = close            
        except NoResultFound:
            session.add(StockImport(date=date, close=close, open=open,high=high,low=low,volume=volume,stock=stock))
        session.commit()
        session.close()


class AlphaVantageDB(object):
    """
    A class responsible to connect AlphaVantage database and make operations
    ...
    Attr
    db_engine: Engine
    """
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB_PATH}/{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbtype, dbname='', dbpath='C://Users/justmac/Documents/alphavantage.db'):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB='alphavantage.db', DB_PATH='/Users/justmac/Documents/')
            self.db_engine = create_engine(engine_url)                        
        else:
            print("DBType is not found in DB_ENGINE")
