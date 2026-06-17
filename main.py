import src.requests.requests_handling as req
import src.userSettings.settings as settings
import src.monitor.monitor as monitor

def main():

    base_url = ""
    while not (base_url):
        base_url = input("Enter the url to monitor: ").strip()
        if not (base_url):
            print("Error: url cannot be empty")

    monitor.loop(base_url);

if __name__ == "__main__":
    main()