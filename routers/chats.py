import sqlite3
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

DB_PATH = "app.db"

router = APIRouter(prefix="/chats", tags=["chats"])

templates = Jinja2Templates(directory="templates/")

@router.get("/{username}")
async def get_user(request: Request, username: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute("""
                with lists AS (
                    SELECT
                    ROW_NUMBER() OVER (PARTITION BY min(from_username, to_username), max(from_username, to_username) ORDER BY created_at DESC) as rnk,
                    *
                    FROM messages
                    WHERE from_username = ? OR to_username = ?
                )
                SELECT from_username, to_username, text
                FROM lists
                WHERE rnk=1""",
                (username, username)
            )

        msgs = []
        for from_username, to_username, text in cursor:
            msgs.append({"from_username": from_username, "to_username": to_username, "text": text})

        return templates.TemplateResponse(
            request=request, name="chats.html", context={"msgs": msgs, "username": username}
        )
    except:
        print("BAD CASE")
        return None

@router.get("/{username_from}/{username_to}")
async def get_chat(request: Request, username_from: str, username_to: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute("""
            SELECT from_username, to_username, text
            FROM messages WHERE (from_username = ? AND to_username = ?) OR (to_username = ? AND from_username = ?)
            ORDER BY created_at ASC""",
            (username_from, username_to, username_from, username_to)
        )

        msgs = []
        for from_username, to_username, text in cursor:
            msgs.append({"from_username": from_username, "to_username": to_username, "text": f"{from_username}:\n{text}"})

        return templates.TemplateResponse(
                request=request, name="chat.html", context={"msgs": msgs, "username": username_from, "to_username": username_to}
        )
    except:
        print("BAD CASE")
        return None

@router.post("/{username_from}/{username_to}/send")
async def send_message(username_from: str, username_to: str, text: str = Form(...)):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO messages(from_username, to_username, text) VALUES (?, ?, ?)",
        (username_from, username_to, text)
    )
    conn.commit()
    return RedirectResponse(url=f"/chats/{username_from}/{username_to}", status_code=303)
