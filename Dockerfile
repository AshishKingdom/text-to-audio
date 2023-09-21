FROM python:3.10-alpine

WORKDIR /usr/local/src

RUN apk add libsndfile-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]