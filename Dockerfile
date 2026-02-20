FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml README.md /app/
RUN uv sync --no-dev

COPY . /app

EXPOSE 7860

CMD ["uv", "run", "python", "main.py"]
