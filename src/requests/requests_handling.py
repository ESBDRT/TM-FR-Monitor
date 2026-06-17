from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from urllib.parse import urlparse
import requests
import json
import time

def make_request(base_url, data_type):
    url = build_request_url(base_url, data_type)
    headers = get_headers(base_url);

    for retry in range(5):
        try:
            r = requests.get(url=url, headers=headers, timeout=10)
            r.raise_for_status()
            return (json.loads(r.text))
        except requests.exceptions.HTTPError:
            if r.status_code == 403:
                print("Error 403 (flagged cookies/ip), updating..")
                headers = get_headers(base_url)

            elif r.status_code >= 500:
                print(f"Server error {r.status_code}, retrying in 10 seconds...")

            else:
                raise

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}, retrying in 10 seconds...")

        time.sleep(10)

    raise RuntimeError("Maximum retries exceeded")

def build_request_url(url, data_type):
    ticket_data_url = urlparse(url).path
    ticket_data_url_split = ticket_data_url.split("/")
    idseance = ticket_data_url_split[-1]

    event_data_full_url = "https://www.ticketmaster.fr/api/manifestations/idmanif/" + idseance + "?responseGroup=ManifestationDetailDto&idTiers=78768&codlang=FR&userCountry=FR&codCoMod=WEB"

    ticket_data_full_url = "https://www.ticketmaster.fr/api/grille-tarifaire/manifestation/idmanif/" + idseance + "/78768?codLang=FR&codCoMod=WEB&onlyFirstAvailableByDay=false&tokenRecaptchaGoogle="

    if (data_type == "ticket"):
        return (ticket_data_full_url)
    elif (data_type == "event"):
        return (event_data_full_url)

def get_headers(url):

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_timeout(5000)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt")
            exit()
            
        cookies = page.context.cookies();
        FullCookie = ""
        for cookie in cookies:
         if (cookie['name'] == "eps_sid"):
            FullCookie += cookie['name'] + '=' + cookie['value'] + ";"
         if (cookie['name'] == "BID"):
            FullCookie += cookie['name'] + '=' + cookie['value'] + ";"
         if (cookie['name'] == "tmpt"):
            FullCookie += cookie['name'] + '=' + cookie['value'] + ";"

        ua = UserAgent()
        headers = {
            'User-Agent': ua.random,
            'Cookie': FullCookie,
        }

        page.close()

        return (headers)
