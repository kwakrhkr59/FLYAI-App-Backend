# import bcrypt
from fastapi import HTTPException

# def hash_password(password: str) -> str:
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def view_all(db):
    with db.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
    return {"results": results}
    
def login_user(username: str, password: str, db):
    with db.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
    # if not user or not verify_password(password, user["password"]):
    #     raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user": {"id": user["id"], "username": user["username"]}}

def signup_user(username: str, password: str, db):
    with db.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        # hashed_password = hash_password(password)
        # cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
    return {"message": "Signup successful"}
