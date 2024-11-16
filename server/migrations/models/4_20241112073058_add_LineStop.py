from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "linestop" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "order" INT NOT NULL,
    "line_id_id" UUID NOT NULL REFERENCES "line" ("id") ON DELETE CASCADE,
    "stop_id_id" UUID NOT NULL REFERENCES "stop" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "linestop";"""
