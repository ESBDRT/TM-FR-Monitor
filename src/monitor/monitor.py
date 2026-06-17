import src.requests.requests_handling as req
import src.userSettings.settings as settings
import time

def loop(base_url):

    user_settings = settings.load_settings()
    while (True):
        ticket_data = req.make_request(base_url, "ticket")
        event_data = req.make_request(base_url, "event")
        if (ticket_data and event_data):
            print("Double req success")
            exit(0)
        else:
            print("failure")
            exit(1)

    
#             print(f"Sleeping for {user_settings['delay']} seconds...")
