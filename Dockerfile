# App online di CICATRICI (POC). Build: docker build -t cicatrici . ; run: docker run -p 8000:8000 cicatrici
FROM python:3.12-slim
WORKDIR /srv
COPY requirements-app.txt .
RUN pip install --no-cache-dir -r requirements-app.txt
COPY sim sim
COPY app app
ENV PORT=8000 PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["python", "-m", "app.server"]
