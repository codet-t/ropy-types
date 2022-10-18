from requests import request

from ropy_types.util.ApiTrackerModel import ApiTracker

def main():
    url_api_tracker = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/Mini-API-Dump.json"
    request_api_tracker = request("GET", url_api_tracker)
    api_tracker: ApiTracker = request_api_tracker.json()
    print(api_tracker["Classes"].__class__.__name__)