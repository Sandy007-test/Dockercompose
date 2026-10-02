FROM python:3.9-slim
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt



RUN useradd -m appuser

COPY --chown=appuser:appuser app.py .



USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
