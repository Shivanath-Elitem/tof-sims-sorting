import asyncio
from Database.DatabaseConnector import database_init, AsyncDatabase

db = AsyncDatabase("main.py")

print("ToF SIMS Sorting Program")

async def main():
    await database_init()
    await db.execute(
        "INSERT INTO TEST values (`0`)"
    )
    val = await db.execute("SELECT * FROM TEST")
    print(val)
    
    

if __name__ == "__main__": asyncio.run(main())