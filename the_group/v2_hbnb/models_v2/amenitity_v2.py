from models.base_model import BaseModel
from datetime import datetime

class Amenity(BaseModel):
    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
