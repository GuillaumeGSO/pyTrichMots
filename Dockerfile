# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get update && apt-get install curl -y

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
