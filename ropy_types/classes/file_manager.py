import os
from ropy_types.classes.generator import Generator

from ropy_types.util.ApiTrackerModel import ApiTracker


class FileManager:
    @classmethod
    def generate_file(cls, api_tracker: ApiTracker):
        # create a file inside generated_types folder
        file = open(os.path.join(os.getcwd(), "generated_types", "types.py"), "w+")
        
        # write the file
        file.write(Generator.generate_string(api_tracker))

        # close the file
        file.close()

    @classmethod
    def generate_folder(cls):
        # create a folder called "generated_types" in the same directory as this file, if it doesn't exist
        folder_name = "generated_types"
        os.makedirs(folder_name, exist_ok=True)

        # empty this folder
        for file in os.listdir(folder_name):
            os.remove(os.path.join(folder_name, file))