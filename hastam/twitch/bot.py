# bot.py

from hastam.twitch.configuration import config
from hastam.twitch.chatter import chat
import socket


def main():
    s = socket.socket()
    __connect(s)

    chatter = chat.Chat()
    chatter.readchat(s)


def __connect(s):
    s.connect((config.HOST, config.PORT))
    s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))


if __name__ == "__main__":
    main()
