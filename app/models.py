
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent.parent / "sitepulse.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS websites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS monitoring_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            status_code INTEGER,
            response_time_ms REAL,
            error TEXT,
            checked_at TEXT NOT NULL,
            FOREIGN KEY (website_id) REFERENCES websites(id)
        )
    """)

    connection.commit()
    connection.close()


def add_website(url):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "INSERT INTO websites (url) VALUES (?)",
            (url,)
        )
        connection.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None
    finally:
        connection.close()


def get_websites():
    connection = get_connection()

    websites = connection.execute(
        "SELECT * FROM websites ORDER BY id DESC"
    ).fetchall()

    connection.close()
    return [dict(website) for website in websites]


def save_monitoring_result(website_id, result):
    connection = get_connection()

    connection.execute("""
        INSERT INTO monitoring_history
        (website_id, status, status_code,
         response_time_ms, error, checked_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        website_id,
        result["status"],
        result["status_code"],
        result["response_time_ms"],
        result["error"],
        result["checked_at"]
    ))

    connection.commit()
    connection.close()


def get_monitoring_history(website_id):
    connection = get_connection()

    history = connection.execute("""
        SELECT * FROM monitoring_history
        WHERE website_id = ?
        ORDER BY id DESC
    """, (website_id,)).fetchall()

    connection.close()
    return [dict(record) for record in history]
