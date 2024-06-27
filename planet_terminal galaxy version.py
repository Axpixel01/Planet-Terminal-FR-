# Bienvenue sur la version Galaxy du Planet Terminal ! Si vous possédez cette version, c'est que vous êtes quelqu'un de spécial.
# Si vous possédez cette version sans autorisation, des problèmes vous attendent.
# Dernier log de màj Galactique : ajout de la commande /galaxy_version, /galaxy_destroy, /galaxy_power, /galaxy_action, /dieu, /action.
# Si il y à des bugs, contactez moi sur Discord : axpixel01
version = ("Version Bêta 0.0.9")
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
        print("Erreur Try Except n°277 : Arguments non-reconnus")
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
elif commande == ("/version_js"):
    print("La version JavaScript est là pour une meilleure version en ligne grâce au HTML. Elle est disponible sur GitHub : https://github.com/Axpixel01/Planet-Terminal-FR-")
elif commande == ("/galaxy_version"):
    print("La version Galaxy est premium, et reservée aux gens spéciaux. Elle offre l'avantage d'avoir accès à tout en avance, et avoir la bêta.")
elif commande == ("/galaxy_destroy"):
    question_galaxy1 = input("Quelle galaxie voulez-vous détruire ?")
    print("Très bien. Galaxie détruite.")
elif commande == ("/galaxy_power"):
    print("...")
    galaxy_power_quest1 = input("Que faites-vous ici ?")
    print("D'accord...")
    galaxy_power_quest2 = input("Voulez-vous plus de pouvoir ?")
    if galaxy_power_quest2 == ("oui"):
        print("Excellent. Tiens. Je t'offre le pouvoir galactique, uniquement si tu arrive à contacter le créateur sur discord, une fois fait, il te dirat si tu l'as reçu. Dis-lui le mot : Galactic Power. Et attend sa réponse.")
    else:
        print("Tant pis.")
elif commande == ("/galaxy_action"):
    question_galaxy2 = input("Quelle galaxie choisissez-vous ?")
    print("{} à été choisie.".format(question_galaxy2))
    question_galaxy3 = input("Que voulez-vous faire à {} ?".format(question_galaxy2))
    print("Très bien. {}".format(question_galaxy2), "à été {}".format(question_galaxy3))
elif commande == ("/dieu"):
    question9 = input("Qui voulez-vous transformer en dieu ?")
    print("Très bien. {} à été séléctionné(e)".format(question9))
elif commande == ("/action"):
    question10 = input("Que voulez-vous faire ?")
    print("Très bien. Action effectuée.")
elif commande == ("/help"):
    print("Voici le menu d'aide Galactique : \n/tp : Permet de se téléporter dans un pays. \n/nuke : Permet d'anéantir une zone. \n/mute : Permet de mute. \n/kill : Permet d'élminier quelqu'un. \n/play_warframe : Permet de jouer à Warframe. \n/langue : Permet de changer la langue. \n/give : Permet de se donner n'importe quoi. \n/ressusciter : Permet de réssusciter ce que vous voulez. \n/piège : Permet de piéger n'importe quoi. \n/ping : Permet de ping quelqu'un. \n/destroy : Permet de détruire ce que vous souhaitez. \n/galaxy_version : Permet d'avoir des infos sur la version actuelle. \n/galaxy_destroy : Permet de détruire une Galaxie au choix. \n/galaxy_power : Permet d'activer la mini-quête galactique. \n /galaxy_action : Permet d'effectuer une action sur une galaxie. \n/dieu : Permet de transformer quelqu'un en dieu. \n/action : Permet d'effectuer une action. \n/help : Permet d'avoir toutes les commandes.")
elif commande == (""):
    print("Erreur n°101 : Aucun Arguments n'a été mis.")
elif commande == (" "):
    print("Erreur Try Except n°277 : Arguments non-reconnus")
else:
    print("Erreur n°327 : Commande ou argument Inconnu. Si vous avez besoin d'aide, éxécutez la commande /help.")