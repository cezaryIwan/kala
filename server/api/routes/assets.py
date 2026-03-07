from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.database import get_session
from database.models import Asset

router = APIRouter()

@router.post("/add")
def add_new_asset(asset: Asset, session: Session = Depends(get_session)) -> Asset:
    if not isinstance(asset, Asset):
        raise HTTPException(status_code=400, detail="Invalid Asset model")

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

@router.get("/list")
def getWallet(session: Session = Depends(get_session)) -> list[Asset]:
    return session.exec(select(Asset)).all()