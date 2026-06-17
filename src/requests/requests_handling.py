from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from urllib.parse import urlparse
import requests
import time

def make_request(base_url, settings):
    url = build_request_url(base_url)
    headers = get_headers(base_url);

    for retry in range(5):
        try:
            r = requests.get(url=url, headers=headers, timeout=10)
            r.raise_for_status()
            print(r.status_code)
            print(r.text)
            return (0)
        except requests.exceptions.HTTPError:
            if r.status_code == 403:
                print("403 received, refreshing headers...")
                headers = get_headers(base_url)

            elif r.status_code >= 500:
                print(f"Server error {r.status_code}, retrying in 10 seconds...")

            else:
                raise

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}, retrying in 10 seconds...")

        time.sleep(10)

    raise RuntimeError("Maximum retries exceeded")

def build_request_url(url):
    url_path = urlparse(url).path
    url_split = url_path.split("/")
    idseance = url_split[-1]
    request_url = "https://www.ticketmaster.fr/api/grille-tarifaire/manifestation/idmanif/" + idseance + "/78768?codLang=FR&codCoMod=WEB&onlyFirstAvailableByDay=false&tokenRecaptchaGoogle="

    return (request_url)

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
