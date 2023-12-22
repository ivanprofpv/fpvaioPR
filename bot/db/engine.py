from typing import Union

import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: Union[URL, str]) -> sqlalchemy.ext.asyncio.AsyncEngine:
    """

    :param url:
    :return:
    """
    return _create_async_engine(url=url, echo=True, pool_pre_ping=True)


async def proceed_schemas(engine: sqlalchemy.ext.asyncio.AsyncEngine, metadata: MetaData) -> None:
    """

    :param engine:
    :param metadata:
    """
    # async with engine.begin() as conn:
    #     await conn.run_sync(metadata.create_all)
    ...


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)
