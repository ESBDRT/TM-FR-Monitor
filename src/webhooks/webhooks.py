from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore, Style
import src.utils.utils as utils
import time

def send_webhook(base_url, webhook_url, ticket_data, event_data):
    
    webhook = DiscordWebhook(url=webhook_url)

    title = event_data['name'] + ' - ' + event_data['location']
    embed = DiscordEmbed(
        title=title, 
        description=f"**{utils.format_date(event_data['startDate'])}**", 
        color="03b2f8", 
        url=base_url
    )

    image_url = f"https://www.ticketmaster.fr/{event_data['urlImage']}"
    embed.set_thumbnail(url=image_url)
    
    embed.set_footer(text="TM-FR-Monitor by @ESBDRT")

    table = "```\nCATEGORY           TICKETS      PRICE\n"
    table += "─" * 45 + "\n"

    for session in ticket_data:
        if session.get('infoCategories'):
            for category in session['infoCategories']:
                name = category['llgCatPl'][:15].ljust(15)
                tickets = str(category['nbPlaces']).rjust(7)
                price = f"{category['priceMin']:.2f}€".rjust(17)
                table += f"{name}{tickets}{price}\n"

    table += "```"

    embed.add_embed_field(
        name="Available Tickets",
        value=table,
        inline=False
    )

    webhook.add_embed(embed)

    for retries in range(3):
        try:
            response = webhook.execute()
            if response.status_code == 200:
                print(Fore.GREEN + "Tickets available, webhook sent !" + Style.RESET_ALL)
                break
        except Exception as e:
            print(f"Try {retries + 1} failed: {e}")
    if retries < 2:
        time.sleep(2)
    
    return response