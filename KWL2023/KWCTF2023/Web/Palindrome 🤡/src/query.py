import os
from sqlite3 import Connection


def dbinit(conn: Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT UNIQUE
        );
        """
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS palindromes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            sentence TEXT
        );
        """
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS flags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flag TEXT
        );
        """
    )

    conn.execute(
        f"""
        INSERT INTO flags (flag) VALUES ('{os.environ.get('FLAG')}');
        """
    )


def get_palindromes(conn: Connection, user: str) -> list:
    c = conn.cursor()
    c.execute(f"SELECT * FROM palindromes WHERE user = ?", (user,))
    return c.fetchall()


def insert_palindrome(conn: Connection, user: str, sentence: str) -> None:
    c = conn.cursor()
    c.execute(
        f"INSERT INTO palindromes (user, sentence) VALUES ('{user}', '{sentence}')"
    )
    conn.commit()


def get_user(conn: Connection, token: str) -> str | None:
    c = conn.cursor()
    c.execute(f"SELECT token FROM users WHERE token = ?", (token,))
    return c.fetchone()


def insert_user(conn: Connection, token: str) -> None:
    c = conn.cursor()
    c.execute(f"INSERT INTO users (token) VALUES ( ? )", (token,))
    conn.commit()
