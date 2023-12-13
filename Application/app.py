from fastapi import FastAPI
from routes import home, products, user

app = FastAPI()

# ===== Routes Included ======
app.include_router(home.router)
app.include_router(products.router)
app.include_router(user.router)
