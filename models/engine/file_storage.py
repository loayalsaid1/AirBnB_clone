#!/usr/bin/python3
"""File storage engine to save objects in a json file"""


from json import dump, load
from os.path import exists

class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the objects in <__objects>"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the <__objects> dictionary in
            format {<obj_classname.obj_id : obj}"""
        FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj.to_dict()})

    def save(self):
        """Serialize <__objects> to the json file in the <__file_path>"""
        with open(FileStorage.__file_path, "w") as f:
            dump(FileStorage.__objects, f)
    
    def reload(self):
        """deserialize the json <__file_path> to <__objects>"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects.update(load(f))
