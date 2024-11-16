from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "linestop" DROP CONSTRAINT "linestop_line_id_id_fkey";
        ALTER TABLE "linestop" DROP CONSTRAINT "linestop_stop_id_id_fkey";
        ALTER TABLE "linestop" RENAME COLUMN "line_id_id" TO "line_id";
        ALTER TABLE "linestop" RENAME COLUMN "stop_id_id" TO "stop_id";
        ALTER TABLE "linestop" ADD CONSTRAINT "fk_linestop_stop_af607802" FOREIGN KEY ("stop_id") REFERENCES "stop" ("id") ON DELETE CASCADE;
        ALTER TABLE "linestop" ADD CONSTRAINT "fk_linestop_line_3fef05b2" FOREIGN KEY ("line_id") REFERENCES "line" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "linestop" DROP CONSTRAINT "fk_linestop_line_3fef05b2";
        ALTER TABLE "linestop" DROP CONSTRAINT "fk_linestop_stop_af607802";
        ALTER TABLE "linestop" RENAME COLUMN "line_id" TO "line_id_id";
        ALTER TABLE "linestop" RENAME COLUMN "stop_id" TO "stop_id_id";
        ALTER TABLE "linestop" ADD CONSTRAINT "linestop_stop_id_id_fkey" FOREIGN KEY ("stop_id_id") REFERENCES "stop" ("id") ON DELETE CASCADE;
        ALTER TABLE "linestop" ADD CONSTRAINT "linestop_line_id_id_fkey" FOREIGN KEY ("line_id_id") REFERENCES "line" ("id") ON DELETE CASCADE;"""
