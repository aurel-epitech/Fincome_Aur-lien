import os
import pandas as pd
import uuid

DATA_DIR = "datasets"
os.makedirs(DATA_DIR, exist_ok=True)

class Dataset:
    # Création d'un dictionnaire pour enregistrer les fichiers CSV enregistré en mémoire
    datasets = {}
    
    # Permet d'enregistrer les CSV
    @classmethod
    def save_dataset(cls, file, filename):
        dataset_id = str(uuid.uuid4())
        file_path = os.path.join(DATA_DIR, f"{dataset_id}.csv")

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        df = pd.read_csv(file_path)
        cls.datasets[dataset_id] = {"filename": filename, "df": df}

        return dataset_id
    
    # Permet de récupérer un dataset en mémoire à partir de son dataset_id
    @classmethod
    def get_dataset(cls, dataset_id):
        return cls.datasets.get(dataset_id, None)
    
    # Permet de supprimer un dataset à la fois en mémoire et du disque
    @classmethod
    def delete_dataset(cls, dataset_id):
        if dataset_id in cls.datasets:
            os.remove(os.path.join(DATA_DIR, f"{dataset_id}.csv"))
            del cls.datasets[dataset_id]
            return True
        return False
