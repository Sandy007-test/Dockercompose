FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN useradd -m appuser

RUN chown +x app.py

COPY app.py .

USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
