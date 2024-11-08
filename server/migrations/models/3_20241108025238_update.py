from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "line" ADD "odpt_id" VARCHAR(512) NOT NULL;
        ALTER TABLE "stop" ADD "odpt_id" VARCHAR(512) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "line" DROP COLUMN "odpt_id";
        ALTER TABLE "stop" DROP COLUMN "odpt_id";"""
