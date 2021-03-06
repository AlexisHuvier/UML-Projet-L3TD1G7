import json
import os

class Save:
    def __init__(self, name):
        self.name = name
        self.file_name = os.path.join(os.path.dirname(__file__), "..", "..", "saves", name+".json")
        self.data = {}

    def load(self): # Charge les données dans la variable self.data
        if(os.path.exists(self.file_name)):
            with open(self.file_name, "r") as f:
                self.data = json.load(f)
    
    def save(self): # Sauvegarde les données
        with open(self.file_name, "w") as f:
            json.dump(self.data, f, indent=4)
    
    def get(self, key, default): # Récupère la donnée qui correspond à la clé "key" sinon la valeur par défaut
        keys = key.split(".")
        if len(keys) == 1:
            return self.data.get(key, default)
        else:
            value = self.data
            for i in keys:
                if i != keys[-1]:
                    if i in value:
                        value = value[i]
                    else:
                        return default
                else:
                    value = value.get(i, default)
            return value

    def set(self, key, value): # Défini une valeur pour une clé
        keys = key.split(".")
        if len(keys) == 1:
            self.data[key] = value
        else:
            data = self.data
            for i in keys:
                if i != keys[-1]:
                    if i not in data:
                        data[i] = {}
                    data = data[i]
                else:
                    data[i] = value