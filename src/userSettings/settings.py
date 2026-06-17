def load_settings():
    settings = {}
    modified = False
    
    with open("settings.txt", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                if key == "delay":
                    if not value:
                        value = "30"
                        modified = True

                if key == "auto_retry":
                    if not value:
                        value = "True"
                        modified = True

                if key == "discord_webhook_url":
                    if not value:
                        while not value:
                            value = input("Enter your discord webhook url: ").strip()
                            if not value:
                                print("Error: discord webhook url cannot be empty.")
                        modified = True
                
                settings[key] = value
    
    if modified:
        with open("settings.txt", 'w', encoding='utf-8') as file:
            for key, value in settings.items():
                file.write(f"{key}={value}\n")
    
    return settings