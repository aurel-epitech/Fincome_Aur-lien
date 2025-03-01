from models.dataset_model import Dataset
from fastapi import HTTPException
import os
from fastapi.responses import FileResponse

DATA_DIR = "datasets"

class DatasetController:
    @staticmethod
    def hello():
        return {"Hello world"}
    


    # Permet de récupérer la liste des datasets enregistrés en mémoire
    @staticmethod
    def list_datasets():
        return [{"id": dataset_id, "filename": data["filename"]} for dataset_id, data in Dataset.datasets.items()]
    
    # Permet de gérer l'upload d'un fichier CSV en appelant save_dataset() dans /models/dataset_model.py 
    @staticmethod
    def upload_dataset(file):
        return {"id": Dataset.save_dataset(file, file.filename), "filename": file.filename}
    
    #  permet de récupérer les informations d'un dataset enregistré via son dataset_id
    @staticmethod
    def get_dataset_info(dataset_id):
        dataset = Dataset.get_dataset(dataset_id)
        if not dataset:
            raise HTTPException(status_code=404, detail="Dataset non trouvé")

        file_path = os.path.join(DATA_DIR, f"{dataset_id}.csv")
        file_size = os.path.getsize(file_path)
        return {"filename": dataset["filename"], "size": file_size}
    
    #  Permet de supprimer un dataset enregistré via son dataset_id  en appelant delete_dataset() dans /models/dataset_model.py 
    @staticmethod
    def delete_dataset(dataset_id):
        if Dataset.delete_dataset(dataset_id):
            return {"message": "Dataset supprimé"}
        raise HTTPException(status_code=404, detail="Dataset non trouvé")
    
    # Permet d'obtenir des statistiques descriptives d'un dataset enregistré via son dataset_id en appelant describe().to_dict() sur le DataFrame stocké en mémoire dans /models/dataset_model.py.
    @staticmethod
    def get_dataset_stats(dataset_id):
        dataset = Dataset.get_dataset(dataset_id)
        if not dataset:
            raise HTTPException(status_code=404, detail="Dataset non trouvé")
        return dataset["df"].describe().to_dict()
    
    # Permet de créer un fichier excel 
    @staticmethod
    def export_to_excel(dataset_id):
        dataset = Dataset.get_dataset(dataset_id)
        if not dataset:
            raise HTTPException(status_code=404, detail="Dataset non trouvé")

        excel_path = os.path.join(DATA_DIR, f"{dataset_id}.xlsx")
        dataset["df"].to_excel(excel_path, index=False)
        return FileResponse(excel_path, filename=f"{dataset['filename'].split('.')[0]}.xlsx")