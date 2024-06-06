import uuid

from datetime import datetime

class BasicModel:
    def __init__(self) :
        self.id=str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at =datetime.now()


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__
    
        