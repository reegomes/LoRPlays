from sys import exit

OWNER = "ReeGomes"

def help(bot, prefix, cmds):
	bot.send_message("Registered commands: " + ", ".join([f"{prefix}{cmd}" for cmd in sorted(cmds.keys())]))

def about(bot, user ,*args):
	bot.send_message(f"Version 1.0.0. Developed by Renato Souza.")

def hello(bot, user, *args):
	bot.send_message(f"Hey {user['name']}!")
 
def userinfo(bot, user, *args):
	bot.send_message(f"Name: {user['name']}. ID: {user['id']}.")

def shutdown(bot, user, *args):
	if user["name"].lower() == OWNER:
		bot.send_message("Shutting down.")
		bot.disconnect()
		exit(0)
	else:
		bot.send_message("You can't do that.")
def howtoplay(bot, user, *args):
	bot.send_message(f"Em breve")