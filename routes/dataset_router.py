from fastapi import APIRouter, UploadFile, File
from controllers.dataset_controller import DatasetController

router = APIRouter()

@router.get("/")
def read_root():
    return DatasetController.hello()