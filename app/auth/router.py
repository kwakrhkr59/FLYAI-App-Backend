from fastapi import APIRouter, Depends
from ..database import get_db
from .service import view_all, login_user, signup_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/view")
def signup(db=Depends(get_db)):
    return view_all(db)

@router.post("/login")
def login(username: str, password: str, db=Depends(get_db)):
    return login_user(username, password, db)

@router.post("/signup")
def signup(username: str, password: str, db=Depends(get_db)):
    return signup_user(username, password, db)