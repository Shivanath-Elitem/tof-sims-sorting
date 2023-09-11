import asyncio
from Database.DatabaseConnector import database_init

print("ToF SIMS Sorting Program")

async def main():
    await database_init()

if __name__ == "__main__": asyncio.run(main())