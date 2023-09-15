from aiomysql import Cursor

def provision_database(db: Cursor):
    
    
    db.execute(
        "CREATE TABLE IF NOT EXISTS `TEST` ("
        "`col1` int NOT NULL)"
    )