from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from models.dataset_model import Dataset
DATA_DIR = "datasets"

class DatasetController:
    @staticmethod
    def hello():
        return {"message": "Hello"}

    @staticmethod
    def list_datasets():
        return [{"id": dataset_id, "filename": data["filename"]} for dataset_id, data in Dataset.datasets.items()]

    @staticmethod
    def upload_dataset(file: UploadFile):
        dataset_id = Dataset.save_dataset(file, file.filename)
        return {"id": dataset_id, "filename": file.filename}
