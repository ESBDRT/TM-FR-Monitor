from datetime import datetime

green="00ff00"
red="ff0000"
yellow="ffff00"
blue="03b2f8"

def format_date(date):
    datef = date
    date_obj = datetime.fromisoformat(date)
    french_date = date_obj.strftime("%d %B %Y")
    return (french_date)