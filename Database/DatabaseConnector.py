import sqlite3
from Database.DatabaseProvisioner import provision_database

db = None

def database_init():
    print("[SQLite] Starting...")
    global db
    db = sqlite3.connect("sqlite.db")
    
    provision_database(db)
    
    print("[SQLite] Started!")


class Database:
    
    def __init__(self, file):
        self.file = file
    
    
    '''execute()
    exec_cmd: str = SQL command to execute
    p: bool = Print SQL command before executing
    '''
    def execute(self, exec_cmd: str, p=False):
        if p: print(exec_cmd)
        
        if exec_cmd.startswith("SELECT"):
            val = db.execute(exec_cmd)
            val = val.fetchall()
            if len(val) == 1:
                if len(val[0]) == 1:
                    return val[0][0]
            return val
        else:
            db.execute(exec_cmd)
            db.commit()
    
    def exists(self, rows):
        return rows > 0