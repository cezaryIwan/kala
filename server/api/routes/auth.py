from fastapi import APIRouter, Depends, HTTPException, Response
from sqlmodel import Session
from database.database import get_session
from schemas import UserCreate
from crud import get_user_by_email, create_user
from security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", status_code=201)
def register_user(
    *, 
    db: Session = Depends(get_session), 
    user_in: UserCreate
):
    existing_user = get_user_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    create_user(db=db, user=user_in)
    return Response(status_code=201)


@router.post("/token")
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
