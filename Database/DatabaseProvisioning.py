from aiomysql import Cursor

async def provision_database(db: Cursor):
    
    
    await db.execute(
        "CREATE TABLE IF NOT EXISTS `TEST` ("
        "`col1` int NOT NULL)"
    )