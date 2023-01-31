import sys
import os
import json
if len(sys.argv) < 2:
    print("Specifiy your chatlog file")
    sys.exit(1)
filename = sys.argv[1]
if (not os.path.isfile(filename)):
    print("Could not find the file!")
    sys.exit(1)
print("Loading " + filename)
convoJSON = open(filename)
convoJSON = json.loads(convoJSON.read())
convoJSON["histories"]["histories"]

number = 0
text = []
lastuser = ""
print("Converting....")
text.append("You: ...")
for msg in convoJSON["histories"]["histories"][number]["msgs"]: # [0]["msgs"][0]
    if(msg["src"]["user"]["username"] != "[USERNAME_REDACTED]" and lastuser != "[USERNAME_REDACTED]" and text[len(text) - 1] != "You: ..."):
        text.append("You: ...")

    if (msg["src"]["user"]["username"] != "[USERNAME_REDACTED]"):
        text.append(msg["src"]["user"]["first_name"] + ": " + msg["text"])
    else:
        text.append("You: " + msg["text"])
    lastuser = msg["src"]["user"]["username"]
finaltext = {"chat": text}
converted = open("converted.json", "a")
converted.write(json.dumps(finaltext, sort_keys=True, indent=5))
converted.close()
print("Done!")
