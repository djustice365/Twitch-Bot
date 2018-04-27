# utils.py
# Utility functions for twitch bot
from urllib.request import urlopen

from hastam.twitch.configuration import config
import urllib.request
import json
from time import sleep


# Send a twitch message to the server
# Parameters:
# socket - the socket over which to send the command
# message - the message to send
def chat(socket, message):
    socket.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, message).encode("utf-8"))


# Ban a user from the channel
# Parameters:
# socket - the socket over which to send the command
# user - the user to ban
def ban(socket, user):
    chat(socket, ".ban {}".format(user))


# timeout a user
# Parameters:
# socket - the socket over which to send the command
# user - the user to timeout
# seconds - the length of time in seconds
def timeout(socket, user, seconds=60):
    chat(socket, ".timeout {} :{}".format(user, seconds))


# check if user is in the op list
def isop(user):
    return user in config.oplist
