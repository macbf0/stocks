FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV FLASK_APP=manage.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
