from fbchat import Client
from fbchat.models import *
import os

client = Client(os.getenv('EMAIL'), os.getenv('PASSWORD'))

print("Own id: {}".format(client.uid))

messages = client.fetchThreadMessages(thread_id="2032883473507719", limit=1)
replied_to = messages['reply_to_id']
client.logout()