import os
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.games import Games
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

# Cria banco de dados caso ele não exista e estabelece conexão
engine = create_async_engine(os.environ.get("DATABASE_URL"), echo=True)

# Estabelece sessão
Session = sessionmaker(bind=engine, class_=AsyncSession)
session = Session()

Base.metadata.create_all(engine)
print("Conexão com o banco de dados estabelecida com sucesso!")