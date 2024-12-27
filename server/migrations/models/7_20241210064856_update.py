from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "stop" ADD "odpt_ids" TEXT[] NOT NULL  DEFAULT '{}';
        ALTER TABLE "stop" DROP COLUMN "odpt_id";
        ALTER TABLE "stop" DROP COLUMN "pole_number";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "stop" ADD "odpt_id" VARCHAR(512) NOT NULL;
        ALTER TABLE "stop" ADD "pole_number" VARCHAR(512) NOT NULL;
        ALTER TABLE "stop" DROP COLUMN "odpt_ids";"""
