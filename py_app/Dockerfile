FROM python:3.12-slim

WORKDIR /app

# uv 설치
RUN pip install uv

# 필요한 라이브러리 설치 (예: FastAPI, httpx 등)
COPY pyproject.toml .
RUN uv pip install --system -r pyproject.toml

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
