FROM python:slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_DEBUG=0
ENV FLAG=KWCTF{sql_1n73ction_w1th_p4lindr0m3_char4ct3r}

EXPOSE 1337

CMD ["python", "app.py"]
