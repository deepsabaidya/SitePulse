
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


def get_monitoring_stats(website_id):
    connection = get_connection()

    stats = connection.execute("""
        SELECT
            COUNT(*) AS total_checks,
            SUM(CASE WHEN status = 'UP' THEN 1 ELSE 0 END) AS successful_checks,
            AVG(response_time_ms) AS average_response_time
        FROM monitoring_history
        WHERE website_id = ?
    """, (website_id,)).fetchone()

    connection.close()

    total = stats["total_checks"] or 0
    successful = stats["successful_checks"] or 0

    uptime = round((successful / total) * 100, 2) if total else 0

    return {
        "total_checks": total,
        "successful_checks": successful,
        "uptime": uptime,
        "average_response_time": round(stats["average_response_time"], 2)
        if stats["average_response_time"] is not None else 0
    }


def get_dashboard_stats():
    connection = get_connection()

    total_websites = connection.execute(
        "SELECT COUNT(*) FROM websites"
    ).fetchone()[0]

    total_checks = connection.execute(
        "SELECT COUNT(*) FROM monitoring_history"
    ).fetchone()[0]

    connection.close()

    return {
        "total_websites": total_websites,
        "total_checks": total_checks
    }


def get_response_time_data(website_id):
    connection = get_connection()

    records = connection.execute("""
        SELECT checked_at, response_time_ms
        FROM monitoring_history
        WHERE website_id = ?
          AND response_time_ms IS NOT NULL
        ORDER BY id ASC
    """, (website_id,)).fetchall()

    connection.close()

    return [dict(record) for record in records]
