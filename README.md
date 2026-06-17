# Ticketmaster FR Monitor

A Ticketmaster FR monitor that checks for available tickets on concert events and notifies you instantly via Discord webhook.

## Overview

This Ticketmaster monitor automatically checks for available tickets on concert events. When tickets become available, a Discord webhook notification is sent so you can secure your tickets as fast as possible.

## Requirements

- Python 3.8 or higher
- See `requirements.txt` for dependencies

## Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/ESBDRT/TM-FR-Monitor.git
   cd TM-FR-Monitor
```

2. **Create a virtual environment:**
```bash
   python -m venv venv
```

3. **Activate the virtual environment:**
   - **On macOS/Linux:**
```bash
     source venv/bin/activate
```
   - **On Windows:**
```bash
     venv\Scripts\activate
```

4. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

## Usage

1. **Start the program:**
```bash
   python main.py
```

2. **Enter the Ticketmaster concert URL** when prompted

3. **Configure Discord webhook** (if not already set in `settings.txt`):
   - You'll be prompted to enter your Discord webhook URL
   - To get one, see [Discord Webhook Setup](#discord-webhook-setup)

4. **Adjust delay settings:**
   - Default delay: 30 seconds
   - ⚠️ **Warning:** Setting the delay too low may flag your IP/cookies (a proxy switching system will be implemented in the future)

5. **Monitor runs automatically:**
   - The program fetches event and ticket data at your configured interval
   - When tickets become available, a Discord notification is sent instantly


## Discord Webhook Setup

1. Go to your Discord server settings
2. Navigate to **Integrations** → **Webhooks**
3. Click **New Webhook**
4. Give it a name (e.g., "Ticketmaster Monitor")
5. Click **Copy Webhook URL**
6. Add it to your `settings.txt` or when prompted by the program
