# Untuk import create_engine dari sqlalchemy
from sqlalchemy import create_engine
# Untuk import dcalartive_base dan sessionmaker dari sqlalchemy.orm
from sqlalchemy.orm import declarative_base, sessionmaker
# Untuk import os
import os
# Untuk import load_dotenv dari dotenv
from dotenv import load_dotenv

# load_dotenv() untuk membaca file .env dan memuat isinya kedalam os.environ
load_dotenv()

# os.getenv(str) mengambil value dari variabel yang sudah di baca dan dimuat di os.environ
# Misal: os.getenv('DB_USER') atau os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Membuat database url untuk membuka koneksi ke database menggunakan sqlalchemy
DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# 
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
