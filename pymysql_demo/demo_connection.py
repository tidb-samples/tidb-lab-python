import os

from dotenv import load_dotenv

import pymysql
from pymysql.connections import Connection

def get_connection(autocommit: bool = True) -> Connection:
    load_dotenv()
    db_conf = {
        "host": os.getenv("TIDB_HOST"),
        "port": int(os.getenv("TIDB_PORT")),
        "user": os.getenv("TIDB_USER"),
        "password": os.getenv("TIDB_PASSWORD"),
        "database": os.getenv("TIDB_DB_NAME"),
        "ssl": {"verify_cert": True},  # PyMySQL uses a different SSL config structure
        "autocommit": autocommit,
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,  # Default to dictionary cursor similar to original
    }

    return pymysql.connect(**db_conf)


if __name__ == "__main__":
    with get_connection() as conn:
        print(f"Connected to {conn.host}:{conn.port} as {conn.user} (Connection ID: {conn.thread_id})")
        # Get server info using a cursor since PyMySQL doesn't have a direct get_server_info method
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION() as version")
            version = cursor.fetchone()
            print(f"The server is running MySQL {version['version']}") 