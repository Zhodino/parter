import os

class Config:
    SECRET_KEY = 'our_secret_key'
    SUPER_USERS = {'ivan': '12345', 'roman': '54321'}
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") \
                              or 'postgresql+psycopg2://' \
                              + 'postgres:annaanna' \
                              + '@localhost:5432/Combat'
