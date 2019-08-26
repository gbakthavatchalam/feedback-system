import asyncio
from aiomysql.sa import create_engine
from settings import DB

async def get_engine():
    engine = await create_engine(user=DB["USER"], password=DB["PASSWORD"], host=DB["HOST"], db=DB["DATABASE"])
    return engine


async def get_connection(engine):
    conn = await engine.acquire()
    return conn


async def select(conn, query):
    result = await conn.execute(query)
    rows = await result.fetchall()
    return rows


async def insert(conn, query, params):
    result = await conn.execute(query, params)
    await conn.connection.commit()
    return result.lastrowid
