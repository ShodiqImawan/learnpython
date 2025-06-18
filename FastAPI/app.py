from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from time import perf_counter

from database import get_db, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['https://iridescent-torte-0c7f39.netlify.app'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get('/ping')
def ping(db: Session = Depends(get_db)):
    start = perf_counter()
    user = db.query(models.User).all()
    end = perf_counter()

    return {"query_speed": f"{end - start} detik"}

@app.get("/get")
def get_data(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return [{"id": user.id, "username": user.username} for user in users]

@app.post("/signup")
def signup_user(item: schemas.Signup, db: Session =  Depends(get_db)):
    user_exist = db.query(models.User).filter(models.User.username == item.username).first()

    # Cek apakah password dan konfirmasi sama
    if item.password != item.cpassword:
        raise HTTPException(status_code = 400, detail=  'Password tidak cocok')
    
    # Cek apakah username sudah dipakai
    if user_exist:
        raise HTTPException(status_code = 400, detail = 'Username sudah dipakai')
    
    # Enkripsi password
    hashed_password = pwd_context.hash(item.password)

    # Simpan ke dalam object
    new_user = models.User(
        username = item.username,
        password = hashed_password
    )

    # Simpan ke database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {'msg': 'Signup Successful', 'user_id': new_user.id}

@app.post("/signin")
def signin_user(item: schemas.Signin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == item.username).first()

    if not user:
        raise HTTPException(status_code = 400, detail = 'Username atau password salah')
    
    if not pwd_context.verify(item.password, user.password):
        raise HTTPException(status_code = 400, detail = 'Username atau password salah')
    
    return {'msg': f'Selamat datang kembali {item.username}!'}

@app.post("/delete")
def delete_data(item: schemas.DeleteData, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == item.id).first()

    if not user:
        raise HTTPException(status_code = 404, detail = 'User tidak ditemukan')
    
    db.delete(user)
    db.commit()

    return {'msg': f'User {item.username} berhasil dihapus'}