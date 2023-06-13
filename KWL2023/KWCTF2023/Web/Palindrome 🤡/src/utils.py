from sqlite3 import Connection
import random
import string

from flask import Request, Response

from query import get_user, insert_user


def generate_token() -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=32))


def check_token(request: Request, response: Response, conn: Connection) -> str:
    token = request.cookies.get("token")

    if not token or len(token) != 32:
        token = generate_token()
        insert_user(conn, token)
        response.set_cookie(
            "token", token
        )

    elif get_user(conn, token) is None:
        insert_user(conn, token)
        response.set_cookie(
            "token", token
        )

    return token


def check_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "").strip()
    return s == s[::-1]
