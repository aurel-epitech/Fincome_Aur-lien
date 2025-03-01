from fastapi import APIRouter, UploadFile, File
from controllers.dataset_controller import DatasetController

router = APIRouter()

# Route de test pour tester hello world
@router.get("/")
def read_root():
    return DatasetController.hello()
#  Permet de lister tous les datasets uploadés
@router.get("/datasets/")
def list_datasets():
    return DatasetController.list_datasets()
# Permet d'envoyer un dataset csv
@router.post("/datasets/")
def upload_dataset(file: UploadFile = File(...)):
    return DatasetController.upload_dataset(file)
