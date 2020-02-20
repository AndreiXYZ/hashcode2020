
import os
import pickle
import json

class DataManager:
    """ tasked with file save and writing as well as os-operations """

    def __init__(self, directory=os.path.join(".", "gitignored_folder")):

        # determines relative disk directory for saving/loading
        self.directory = directory
        os.makedirs(directory, exist_ok=True)
        self.stamp = ""
        self.actual_date = None

    def save_python_obj(self, obj, name, print_success=True):
        """ Saves python object to disk in pickle """

        try:
            filepath = os.path.join(self.directory, f'{name}.pickle')
            with open(filepath, 'wb') as handle:
                pickle.dump(obj, handle, protocol=-1)
                if print_success:
                    print("Saved {}".format(name))
        except Exception as e:
            print(e)
            print("Failed saving {}, continue anyway".format(name))

    def create_dir(self, name: str):
        """ creates directory """
        os.makedirs(os.path.join(self.directory, name), exist_ok=True)

    def load_python_obj(self, name):
        """ Loads python object from disk in pickle """

        try:
            obj = None
            filepath = os.path.join(self.directory, f'{name}.pickle')
            with (open(filepath, "rb")) as openfile:
                obj = pickle.load(openfile)
            print("Loaded {}".format(name))
            return obj
        except Exception as e:
            print(e)
            print("Failed loading {}, continue anyway".format(name))

    def load_json(self, name: str) -> dict:
        if not (name.endswith(".json")):
            name = name + ".json"
        with open(os.path.join(self.directory, name)) as json_file:
            data = json.load(json_file)
            return data

    def save_json(self, name: str, data: dict):
        if not (name.endswith(".json")):
            name = name + ".json"
        with open(os.path.join(self.directory, name), 'w') as outfile:
            json.dump(data, outfile)

    def write_to_file(self, name, content):
        with open(os.path.join(self.directory, name), 'w') as outfile:
            outfile.write(content)

