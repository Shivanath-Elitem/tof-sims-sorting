import aiosqlite
from Database.DatabaseProvisioning import provision_database

db = None

async def database_init():
    print("[SQLite] Starting...")
    global db
    db = await aiosqlite.connect("sqlite.db")
    await provision_database(db)
    
    print("[SQLite] Started!")
    