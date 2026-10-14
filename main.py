from fastapi import FastAPI
from routers.chats import router as chats_router
import sqlite3

DB_PATH = "app.db"

def create_database():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_username TEXT NOT NULL,
                to_username TEXT NOT NULL,
                text TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
    except:
        print("ERROR Creating Database")


app = FastAPI()
app.include_router(chats_router)

@app.on_event("startup")
def startup():
    create_database()
