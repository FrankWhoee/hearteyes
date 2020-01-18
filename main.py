from fbchat import log, Client
import os
from fbchat import MessageReaction

# Subclass fbchat.Client and override required methods
class hearteyes_bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        target_id = message_object.reply_to_id

        if message_object.reply_to_id and str(message_object.text)[-1] + str(message_object.text)[0] == "::":
            type = str(message_object.text)[1:-1]
            print("REACT activated of type: " + str(message_object.text)[1:-1])
            if type.__contains__("love") or type.__contains__("eyes"):
                client.reactToMessage(target_id, MessageReaction.LOVE)
            elif type.__contains__("heart"):
                client.reactToMessage(target_id, MessageReaction.HEART)
            elif type.__contains__("anger") or type.__contains__("angry") or type.__contains__("amgery"):
                client.reactToMessage(target_id, MessageReaction.ANGRY)
            elif type.__contains__("happy") or type.__contains__("laugh") or type.__contains__("funny") or type.__contains__("smile"):
                client.reactToMessage(target_id, MessageReaction.SMILE)
            elif type.__contains__("cry") or type.__contains__("sad") or type.__contains__("tears") or type.__contains__("unhappy") or type.__contains__("happyn't"):
                client.reactToMessage(target_id, MessageReaction.SAD)
            elif type.__contains__("amazed") or type.__contains__("wow") or type.__contains__("tears") or type.__contains__("truck"):
                client.reactToMessage(target_id, MessageReaction.WOW)
            elif type.__contains__("down") or type.__contains__("no"):
                client.reactToMessage(target_id, MessageReaction.NO)
            elif type.__contains__("up") or type.__contains__("yes"):
                client.reactToMessage(target_id, MessageReaction.YES)

client = hearteyes_bot(os.getenv('EMAIL'), os.getenv('PASSWORD'))
client.listen()
