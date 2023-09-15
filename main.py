import asyncio
import os
from Database.DatabaseConnector import database_init, Database

db = Database("main.py")

print("ToF SIMS Sorting Program")

async def main():
    database_init()
    val = db.execute("SELECT * FROM TEST")
    print(val)
    

try: asyncio.run(main())
except Exception as e: print(e)