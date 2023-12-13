from fastapi import FastAPI
from routes import home, products, user
from __init__ import Database, Models

app = FastAPI()


Models.Base.metadata.create_all(bind = Database.engine)

# ===== Routes Included ======
app.include_router(home.router)
app.include_router(products.router)
app.include_router(user.router)
