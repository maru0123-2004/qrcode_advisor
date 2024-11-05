from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "line" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(1024) NOT NULL,
    "company" VARCHAR(1024) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "stop" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(1024) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "line";
        DROP TABLE IF EXISTS "stop";"""
