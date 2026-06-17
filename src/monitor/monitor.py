import src.requests.requests_handling as req
import src.userSettings.settings as settings
import time

def loop(base_url):

    user_settings = settings.load_settings()
    while (True):
        if (req.make_request(base_url, user_settings) == 0):
            print(f"Sleeping for {user_settings['delay']} seconds...")
        else:
            input("Press enter to quit...")
            exit()
    
