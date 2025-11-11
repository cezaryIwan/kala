from sqlmodel import Session, select
from database.database import get_session
from fastapi import Depends, FastAPI, HTTPException, Response
from database.models import Asset
from fastapi.middleware.cors import CORSMiddleware
from schemas import UserCreate
from crud import *
from security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wallet")
def getWallet(session: Session = Depends(get_session)) -> list[Asset]:
    return session.exec(select(Asset)).all()
   
@app.post("/asset/add")
def addNewAsset(asset: Asset, session: Session = Depends(get_session)) -> Asset:
    if not isinstance(asset, Asset):
        raise HTTPException(status_code=400, detail="Could not map sent asset to Asset model.")
    db_asset = session.exec(select(Asset).where(Asset.type == asset.type)).first()
    if db_asset:
        db_asset.balance += asset.balance
        session.commit()
        session.refresh(db_asset)
        return db_asset
    session.add(asset)
    session.commit()
    session.refresh(asset)
    return asset

@app.post("/auth/register", status_code=201, tags=["Auth"])
def register_user(
    *, 
    db: Session = Depends(get_session), 
    user_in: UserCreate
):
    existing_user = get_user_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
        
    create_user(db=db, user=user_in)
    return Response(status_code=201) 

@app.post("/auth/token", tags=["Auth"])
def login_for_access_token(
    db: Session = Depends(get_session), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = get_user_by_email(db, email=form_data.username)
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401, 
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = create_access_token(subject=user.email)
    
    return {"access_token": access_token, "token_type": "bearer"}