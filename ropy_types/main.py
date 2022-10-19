from requests import request

from ropy_types.util.ApiTrackerModel import ApiTracker
from ropy_types.classes.file_manager import FileManager
from ropy_types.util.DataTypeManager import DataTypeManager

def main():
    url_api_tracker = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/Mini-API-Dump.json"
    request_api_tracker = request("GET", url_api_tracker)
    api_tracker: ApiTracker = request_api_tracker.json()

    api_tracker["DataTypes"] = DataTypeManager.get(api_tracker)
    
    FileManager.generate_folder();
    FileManager.generate_file(api_tracker);