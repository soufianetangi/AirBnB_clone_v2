# /AirBnB_clone_v2/models/state.py
from models.base_model import BaseModel

class State(BaseModel):
    def __init__(self, name, state_code):
        super().__init__(name)
        self.state_code = state_code

    def __repr__(self):
        return f"State(name={self.name}, state_code={self.state_code})"
