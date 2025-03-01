
from fastapi import HTTPException
from fastapi.responses import FileResponse

DATA_DIR = "datasets"

class DatasetController:
  @staticmethod
  def hello():
    return {"message": "Hello"}