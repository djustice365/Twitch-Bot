import re
from hastam.twitch.utils import utils
import time
from urllib.request import urlopen
from hastam.twitch.configuration import config
import urllib.request
import json
from time import sleep
import _thread
from hastam.twitch.ValueObjects import commandlist


class Chat:
    chatmsg = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

    def readchat(self, s):
        _thread.start_new_thread(self.threadfilloplist, ())
        utils.chat(s, "Hi Errybody!")

        while True:
            response = s.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            else:
                username = re.search(r"\w+", response).group(0)
                res = self.chatmsg.sub("", response).strip().split(" ", 1)
                command = res[0]
                message = res[1] if len(res) > 1 else ""
                print(response)
                print("Message: " + message)

                # Hardcoded Commands
                if command == "!commands":
                    utils.chat(s, "Commands: {}".format(commandlist.commandList))
                if command in commandlist.commands:
                    utils.chat(s, "{}".format(commandlist.commands[command]))
            sleep(1)

    # Fill OPList
    # In a separate thread, fill OP List
    @staticmethod
    def threadfilloplist():
        while True:
            try:
                url = "http://tmi.twitch.tv/group/user/" + config.CHAN + "/chatters"
                headers = {
                    "accept": "*/*"
                }
                req = urllib.request.Request(url, headers)
                response = urllib.request.urlopen(req).read()
                if response.find("502 Bad Gateway") == -1:
                    config.oplist.clear()
                    data = json.loads(response)
                    for user in data["chatters"]["moderators"]:
                        config.oplist[user] = "mod"
                    for user in data["chatters"]["global_mods"]:
                        config.oplist[user] = "global_mod"
                    for user in data["chatters"]["admins"]:
                        config.oplist[user] = "admin"
                    for user in data["chatters"]["staff"]:
                        config.oplist[user] = "staff"
            except:
                'do nothing'
            sleep(5)
