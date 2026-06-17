import src.requests.requests_handling as req
import src.userSettings.settings as settings
import time
from datetime import datetime

def loop(base_url):

    user_settings = settings.load_settings()
    while (True):
        ticket_data = req.make_request(base_url, "ticket")
        event_data = req.make_request(base_url, "event")

        if (ticket_data and event_data):

             print(f"Name: {event_data['name']}")
             print(f"Location: {event_data['location']}")
             print(f"ImageUrl: {event_data['urlImage']}")
             print(f"Url: {base_url}")
    
             for session in ticket_data:
                if session['infoCategories']:
                    date = session['dateSeance']
                    date_obj = datetime.fromisoformat(date)
                    french_date = date_obj.strftime("%d %B %Y")
                    print(f"Date: {french_date}")
                    print("Available categories:")
                    for category in session['infoCategories']:
                        if category['nbPlaces'] > 0:
                            print(f"{category['llgCatPl']}: {category['nbPlaces']} places @ {category['priceMin']}€")
                        else:
                            print(f"  {category['llgCatPl']}: SOLD OUT")

             print(f"Sleeping for {user_settings['delay']} seconds...")
             time.sleep(int(user_settings['delay']))
        else:
            print("failure")
            exit(1)

    

