import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import configparser

app = FastAPI()

config = configparser.ConfigParser()
config.read("database.ini")
host = config.get("database", "host")
user = config.get("database", "user")
password = config.get("database", "password")
port = config.get("database", "port")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    try:
        with psycopg2.connect(
            host=host, user=user, password=password, port=port
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                row = cur.fetchone()
                return {"val": row[0]}
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return {"val": "ERROR"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
