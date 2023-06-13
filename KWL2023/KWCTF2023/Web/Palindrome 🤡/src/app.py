import sqlite3
import uuid

from flask import (
    Flask,
    render_template,
    request,
    make_response,
    flash,
    get_flashed_messages,
    redirect,
)

from utils import *
from query import *

app = Flask(__name__)
app.debug = os.environ.get("FLASK_DEBUG", True)
app.secret_key = str(uuid.uuid4())

conn = sqlite3.connect(
    "app.db", check_same_thread=False, isolation_level=None, timeout=30
)


@app.route("/")
def home():
    response = make_response(render_template("home.html"))
    check_token(request, response, conn)
    return response


@app.route("/palindromes")
def list_palindromes():
    response = make_response()
    token = check_token(request, response, conn)

    palindromes = get_palindromes(conn, token)
    messages = dict(get_flashed_messages(True))

    response.set_data(
        render_template("palindromes.html", palindromes=palindromes, messages=messages)
    )

    return response


@app.route("/submit_palindrome", methods=["POST"])
def submit_palindrome():
    response = make_response()
    token = check_token(request, response, conn)

    sentence = request.form.get("sentence")
    isPalindrome = check_palindrome(sentence)

    if not isPalindrome:
        flash("Kata - kata bukan palindrome!", "error")
    else:
        insert_palindrome(conn, token, sentence)
        flash("Kata - kata berhasil ditambahkan!", "success")

    return redirect("/palindromes")


if __name__ == "__main__":
    dbinit(conn)
    app.run("0.0.0.0", 1337)
