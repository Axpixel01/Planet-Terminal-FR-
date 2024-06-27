# Bienvenue sur le Planet Terminal Version 0.0.7 . Ici, vous pouvez éxécuter quelques commandes qui sont... Intéréssantes...
# Dernier log de màj : Ajout de la commande /destroy
# Si il y à des bugs, contactez moi sur Discord : axpixel01
version = ("Version 0.0.7")
commande = input("Bienvenue sur le Planet Terminal {}. Quelle commande allez-vous éxécuter ? Indiquez là juste ici :".format(version))

if commande == ("/tp"):
    question = input("Ou voulez vous vous téléporter ?")
    if question == ("Russie"):
        print("Vous êtes arrivé en Russie. Bienvenue.")
    elif question == ("France"):
        print("Vous êtes arrivé en France. Bienvenue.")
    elif question == ("Japon"):
        print("Vous êtes arrivé au Japon. Bienvenue.")
    elif question == ("USA"):
        print("Vous êtes arrivé aux USA. Bienvenue.")
    elif question == ("Corée du Sud"):
        print("Vous êtes arrivé en Corée du Sud. Bienvenue.")
    else:
        print("Erreur n°001-X : Argument Inconnu.")
elif commande == ("/nuke"):
    question1 = input("Quelle zone voulez-vous nuke ?")
    print("Très bien. Zone anéantie.")
elif commande == ("/mute"):
    question2 = input("Qui ou qu'est-ce que vous voulez mute ?")
    print("Ok, mute.")
elif commande == ("/kill"):
    question3 = input("Qui voulez-vous éliminer ?")
    print("Ok, personne éliminée.")
elif commande == ("/play_warframe"):
    print("https://www.warframe.com/fr/download")
elif commande == ("/langue"):
    print("Version anglaise disponible sur GitHub (Python uniquement)")
elif commande == ("/give"):
    question4 = input("Que voulez-vous avoir ?")
    print("Ok, tenez :", question4)
elif commande == ("/ressusciter"):
    question5 = input("Qui ou qu'est-ce que vous voulez réssusciter ?")
    print("Ok, réssuscité.")
elif commande == ("/piège"):
    question6 = input("Qui ou qu'est-ce que vous voulez piéger ?")
    print("Ok, piégé.")
elif commande == ("/ping"):
    question7 = input("Séléctionnez une personne.")
    print("Ok, personne ping.")
elif commande == ("/destroy"):
    question8 = input("Qui ou qu'est-ce que vous voulez détruire ?")
    print("Ok, {} détruit(e).".format(question8))
elif commande == ("/help"):
    print("Voici le menu d'aide : \n/tp : Permet de se téléporter dans un pays. \n/nuke : Permet d'anéantir une zone. \n/mute : Permet de mute. \n/kill : Permet d'élminier quelqu'un. \n/play_warframe : Permet de jouer à Warframe. \n/langue : Permet de changer la langue. \n/give : Permet de se donner n'importe quoi. \n/ressusciter : Permet de réssusciter ce que vous voulez. \n/piège : Permet de piéger n'importe quoi. \n/ping : Permet de ping quelqu'un. \n/destroy : Permet de détruire ce que vous souhaitez. \n/help : Permet d'avoir toutes les commandes.")
else:
    print("Erreur n°001 : Commande Inconnue. Si vous avez besoin d'aide, éxécutez la commande /help.")