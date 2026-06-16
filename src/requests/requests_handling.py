from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from urllib.parse import urlparse
import requests

def make_request(base_url, headers):

    url = build_request_url(base_url)

    r = requests.get(url=url, headers=headers);
    print(r.status_code)
    print(r.text)

def build_request_url(url):
    url_path = urlparse(url).path
    url_split = url_path.split("/")
    idseance = url_split[-1]
    request_url = "https://www.ticketmaster.fr/api/grille-tarifaire/manifestation/idmanif/" + idseance + "/78768?codLang=FR&codCoMod=WEB&onlyFirstAvailableByDay=false&tokenRecaptchaGoogle="

    return (request_url)

def build_headers(cookies):
     
     ua = UserAgent()
     FullCookie = "";

     for cookie in cookies:
         if (cookie['name'] == "eps_sid"):
            FullCookie += cookie['name'] + '=' + cookie['value'] + ";"
         if (cookie['name'] == "BID"):
            FullCookie += cookie['name'] + '=' + cookie['value'] + ";"
         if (cookie['name'] == "tmpt"):
            FullCookie += cookie['name'] + '=' + cookie['value'] + ";"

     headers = {
        'User-Agent': ua.random,
        'Cookie': FullCookie,
     }

     return (headers)
    

def get_request_headers(url):

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_timeout(5000)
            
            return (build_headers(page.context.cookies()))

        except KeyboardInterrupt:
            print("\nKeyboard interrupt")
            exit
