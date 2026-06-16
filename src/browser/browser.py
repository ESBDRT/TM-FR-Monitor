from playwright.sync_api import sync_playwright
import time

def open_browserless_win(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt")
