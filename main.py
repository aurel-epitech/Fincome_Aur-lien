from fastapi import FastAPI
from routes.dataset_router import router
import uvicorn


# Permet la création de l'app
app = FastAPI()  
#  Permet d'inlure les routes
app.include_router(router)  

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
