import src.requests.requests_handling as req
import src.userSettings.settings as settings
import src.webhooks.webhooks as webhook
import src.utils.utils as utils
import time
from datetime import datetime

def loop(base_url):

    user_settings = settings.load_settings()
    while (True):
        ticket_data = req.make_request(base_url, "ticket")
        event_data = req.make_request(base_url, "event")

        if (ticket_data and event_data):    
             available = False
             for session in ticket_data:
                if session['infoCategories']:
                    for category in session['infoCategories']:
                        if category['nbPlaces'] > 0:
                            available = True
             if (available):
                webhook.send_webhook(base_url, user_settings['discord_webhook_url'], ticket_data, event_data)
             else:
                 print("No tickets available")
             print(f"Sleeping for {user_settings['delay']} seconds...")
             time.sleep(int(user_settings['delay']))
        else:
            print("failure")
            exit(1)

    

