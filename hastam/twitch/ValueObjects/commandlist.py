# commandlist
# contains a list of hard coded commands for easy maintenance

commands = {
    "!test1": "test1",
    "!test2": "test2",
    "!test3": "test3",
    "!test4": "test4",
    "!test5": "test5"
}


def getformattedcommandlist():
    keylist = ""
    for key in commands.keys():
        keylist = keylist + " " + str(key)
    keylist = keylist.lstrip(" ")
    keylist = keylist.replace(" ", ", ")
    return keylist


commandList = getformattedcommandlist()
