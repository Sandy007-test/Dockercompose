FROM python:3.12-slim

ENV PYTHONBUFFERED=1 \
	 PIP_NO_CACHE_DIR=1



WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt



RUN useradd -m appuser

COPY --chown=appuser:appuser app.py .



USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
