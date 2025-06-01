from fastapi import FastAPI
from sqlalchemy import create_engine

# DB 연결 URL
DB_URL = "mysql+pymysql://appuser:apppass@mysql:3306/appdb"
app = FastAPI()

# SQLAlchemy 엔진
engine = create_engine(DB_URL)

# 연결 테스트
with engine.connect() as conn:
    result = conn.execute("SELECT NOW()")
    print(f"📅 현재 시간: {list(result)}")

@app.get("/")
def read_root():
    return {"message": "Hello from Dockerized FastAPI!"}