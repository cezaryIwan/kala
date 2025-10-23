from sqlmodel import Session, select
from database.database import get_session
from fastapi import Depends, FastAPI, HTTPException, Response
from database.models import Asset
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.user import UserCreate
from app.crud import user as crud_user
from app.core.security import verify_password, create_access_token
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
    user_in: UserCreate # Dane wejściowe to schemat Pydantic
):
    """
    Rejestruje nowego użytkownika. Zwraca status 201 (Created) po pomyślnej rejestracji.
    """
    existing_user = crud_user.get_user_by_email(db, email=user_in.email)
    if existing_user:
        # Używamy numerycznego kodu 400
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
        
    crud_user.create_user(db=db, user=user_in)
    # Zwrócenie obiektu Response z kodem 201 (został poprawnie zaimportowany)
    return Response(status_code=201) 

@app.post("/auth/token", tags=["Auth"])
def login_for_access_token(
    db: Session = Depends(get_session), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Uwierzytelnia użytkownika (za pomocą e-maila i hasła) i zwraca token dostępowy JWT.
    """
    user = crud_user.get_user_by_email(db, email=form_data.username)
    
    # Walidacja użytkownika i hasła
    if not user or not verify_password(form_data.password, user.hashed_password):
        # Używamy numerycznego kodu 401
        raise HTTPException(
            status_code=401, 
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Tworzenie tokena JWT
    access_token = create_access_token(subject=user.email)
    
    # Zwrócenie tokena i typu tokena (bearer)
    return {"access_token": access_token, "token_type": "bearer"}