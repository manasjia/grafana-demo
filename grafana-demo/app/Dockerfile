FROM python:3.9-alpine
WORKDIR /app

COPY Requirements.txt .

RUN pip install --no-cache-dir -r Requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

