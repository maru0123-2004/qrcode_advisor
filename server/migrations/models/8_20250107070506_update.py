from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE EXTENSION vector;
        ALTER TABLE "stop" ADD "position" public.vector(2);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "stop" DROP COLUMN "position";"""
