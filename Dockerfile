# syntax=docker/dockerfile:1fd

FROM python:3.11

WORKDIR /evergreen-microservices

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app"]