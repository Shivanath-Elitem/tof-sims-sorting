import aiosqlite
from Database.DatabaseProvisioning import provision_database

db = None

async def database_init():
    print("[SQLite] Starting...")
    global db
    db = await aiosqlite.connect("sqlite.db")
    
    await provision_database(db)
    
    print("[SQLite] Started!")


class AsyncDatabase:
    
    def __init__(self, file):
        self.file = file
    
    
    '''execute()
    exec_cmd: str = SQL command to execute
    p: bool = Print SQL command before executing
    '''
    async def execute(self, exec_cmd: str, p=False):
        if p: print(exec_cmd)
        
        if exec_cmd.startswith("SELECT"):
            val = await db.execute_fetchall(exec_cmd)
            if len(val) == 1:
                if len(val[0]) == 1:
                    return val[0][0]
            return val
        else:
            await db.execute(exec_cmd)
            await db.commit()
    
    def exists(self, rows):
        return rows > 0