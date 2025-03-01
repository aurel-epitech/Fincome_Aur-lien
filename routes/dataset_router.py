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

# Permet d'obtenir les infos d'un dataset filename et size
@router.get("/datasets/{dataset_id}/")
def get_dataset_info(dataset_id: str):
    return DatasetController.get_dataset_info(dataset_id)

# Permet de supprimer un dataset en fonction d'un ID
@router.delete("/datasets/{dataset_id}/")
def delete_dataset(dataset_id: str):
    return DatasetController.delete_dataset(dataset_id)

# Permet de retourner les statistiques générées à l'aide de pandas.
@router.get("/datasets/{dataset_id}/stats/")
def get_dataset_stats(dataset_id: str):
    return DatasetController.get_dataset_stats(dataset_id)

# Permet de créer un fichier excel 
@router.get("/datasets/{dataset_id}/excel/")
def export_to_excel(dataset_id: str):
    return DatasetController.export_to_excel(dataset_id)
