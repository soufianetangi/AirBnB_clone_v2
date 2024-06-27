# /AirBnB_clone_v2/models/base_model.py

class BaseModel:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"BaseModel(name={self.name})"
