import json
from models.user import User
from datetime import datetime
class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    def save(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        obj.updated_at = datetime.now()
        self.__objects[key] = obj.to_dict()
        self._save_to_file()
    def get(self, obj_id, obj_type):
        key = f'{obj_type}.{obj_id}'
        return self.__objects.get(key)
    def get_all(self, obj_type):
        return [obj for key, obj in self.__objects.items() if key.startswith(obj_type)]
    def delete(self, obj_id, obj_type):
        key = f'{obj_type}.{obj_id}'
        if key in self.__objects:
            del self.__objects[key]
            self._save_to_file()
    def _save_to_file(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
    def _load_from_file(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            self.__objects = {}
