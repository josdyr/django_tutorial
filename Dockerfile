FROM python:3-alpine
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .

RUN apk --no-cache add \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
  && pip install -r requirements.txt 

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
