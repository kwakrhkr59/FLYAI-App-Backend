import os
from dotenv import load_dotenv
from mysql.connector import pooling

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    # "port": int(os.getenv("DB_PORT", 3306))
}

db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,  # 최대 10개의 연결
    **dbconfig
)

def get_db():
    db = db_pool.get_connection()
    try:
        yield db
    finally:
        db.close()