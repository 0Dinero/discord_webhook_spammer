import time
from discord_webhook import DiscordWebhook
i = input("What webhook do you want to spam?: ")
x = input("What message do you want to spam?: ")
ii = input("Are you ready to start spamming?: ")
iii = ii.upper()
l = int(0)
if(iii == "YES"):
    while True:
        time.sleep(0.33)
        try:
            webhook = DiscordWebhook(url=i, content=x)
            response = webhook.execute()
            l += 1
            print("Spam-count = ", l)
        except 429:
            pass
else:
    exit()