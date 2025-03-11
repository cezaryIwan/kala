from sqlmodel import Session, select
from database.database import get_session
from fastapi import Depends, FastAPI, HTTPException
from database.models import Asset
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Zezwól na dostęp z wszystkich źródeł, możesz dodać swoje domeny
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
