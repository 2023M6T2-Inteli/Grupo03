# ./server.py
import os
from sanic import Sanic
from sqlalchemy.ext.asyncio import create_async_engine
from contextvars import ContextVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sanic.response import json
from models.models import Car, Person

app = Sanic("my_app")

bind = create_async_engine(os.environ.get("DATABASE_URL"), echo=True)

_sessionmaker = sessionmaker(bind, class_=AsyncSession, expire_on_commit=False)
_base_model_session_ctx = ContextVar("session")

@app.middleware("request")
async def inject_session(request):
    request.ctx.session = _sessionmaker()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


@app.middleware("response")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()

@app.post("/user")
async def create_user(request):
    session = request.ctx.session
    async with session.begin():
        car = Car(brand="Tesla")
        person = Person(name="foo", cars=[car])
        session.add_all([person])
    return json(person.to_dict())

@app.get("/user/<pk:int>")
async def get_user(request, pk):
    session = request.ctx.session
    async with session.begin():
        stmt = select(Person).where(Person.id == pk).options(selectinload(Person.cars))
        result = await session.execute(stmt)
        person = result.scalar()

    if not person:
        return json({})

    return json(person.to_dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
