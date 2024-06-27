# Welcome to Planet Terminal Version 0.0.8. Here you can execute some commands which are... Interesting...
# Latest update log: Added the /js_version command
# If there are any bugs, contact me on Discord: axpixel01
version = ("Version 0.0.8")
commande = input("Welcome to Planet Terminal {}. What command will you execute ? Indicate it right here:".format(version))

if commande == ("/tp"):
    question = input("Where do you want to teleport ?")
    if question == ("Russia"):
        print("You have arrived in Russia. Welcome.")
    elif question == ("France"):
        print("You have arrived in France. Welcome.")
    elif question == ("Japan"):
        print("You have arrived in Japan. Welcome.")
    elif question == ("USA"):
        print("You have arrived in the USA. Welcome.")
    elif question == ("South Korea"):
        print("You have arrived in South Korea. Welcome.")
    else:
        print("Try Except error n°277: Unrecognized arguments")
elif commande == ("/nuke"):
    question1 = input("What area do you want to nuke ?")
    print("Alright. Area wiped out.")
elif commande == ("/mute"):
    question2 = input("Who or what do you want to mute ?")
    print("Ok, mute.")
elif commande == ("/kill"):
    question3 = input("Who do you want to eliminate ?")
    print("Ok, person eliminated.")
elif commande == ("/play_warframe"):
    print("https://www.warframe.com/fr/download")
elif commande == ("/language"):
    print("French version available on GitHub (Python only)")
elif commande == ("/give"):
    question4 = input("What do you want to have ?")
    print("Ok, here :", question4)
elif commande == ("/resurrect"):
    question5 = input("Who or what do you want to resurrect ?")
    print("Okay, resurrected.")
elif commande == ("/trap"):
    question6 = input("Who or what do you want to trap ?")
    print("Okay, trapped.")
elif commande == ("/ping"):
    question7 = input("Select a person.")
    print("Okay, the selected person has been pinged.")
elif commande == ("/destroy"):
    question8 = input("Who or what do you want to destroy?")
    print("Ok, {} destroyed.".format(question8))
elif commande == ("/js_version"):
    print("The JavaScript version is available on GitHub (French Only) : https://github.com/Axpixel01/Planet-Terminal-FR-")
elif commande == ("/help"):
    print("Here is the help menu: \n/tp: Allows you to teleport to a country. \n/nuke: Allows you to destroy an area. \n/mute: Allows mute. \n/kill: Allows you to kill someone. \n/play_warframe: Allows you to play Warframe. \n/language: Allows you to change the language. \n/give: Allows you to give anything. \n/resurrect: Allows you to resurrect whatever you want. \n/trap: Allows you to trap anything. \n/ping: Allows you to ping someone. \n/destroy: Allows you to destroy whatever you want. \n/help: Allows you to have all the commands.")
elif commande == (""):
    print("Error n°101: No Arguments were put.")
elif commande == (" "):
    print("Try Except error n°277: Unrecognized arguments")
else:
    print("Error n°327: Unknown Command. If you need help, run the /help command.")

# Traduction by : Axpixel01