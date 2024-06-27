# Bienvenue sur le Planet Terminal Version 0.0.9 . Ici, vous pouvez éxécuter quelques commandes qui sont... Intéréssantes...
# Dernier log de màj : Ajout de la commande /dieu, /action, /amongus, /noob, /arme, /ref, /envie_de...
# Si il y à des bugs, contactez moi sur Discord : axpixel01
version = ("Version 0.0.9")
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
elif commande == ("/dieu"):
    question9 = input("Qui voulez-vous transformer en dieu ?")
    print("Très bien. {} à été séléctionné(e)".format(question9))
elif commande == ("/action"):
    question10 = input("Que voulez-vous faire ?")
    print("Très bien. Action effectuée.")
elif commande == ("/amongus"):
    print("SUS")
elif commande == ("/noob"):
    print(";-;")
elif commande == ("/arme"):
    print("Tiens, ton arme.")
elif commande == ("/ref"):
    print("Y'en à trop...")
elif commande == ("/envie_de..."):
    print("Quoi ?! *TAP* Comment ça mon reuf ?!")
elif commande == ("/help"):
    print("Voici le menu d'aide : \n/tp : Permet de se téléporter dans un pays. \n/nuke : Permet d'anéantir une zone. \n/mute : Permet de mute. \n/kill : Permet d'élminier quelqu'un. \n/play_warframe : Permet de jouer à Warframe. \n/langue : Permet de changer la langue. \n/give : Permet de se donner n'importe quoi. \n/ressusciter : Permet de réssusciter ce que vous voulez. \n/piège : Permet de piéger n'importe quoi. \n/ping : Permet de ping quelqu'un. \n/destroy : Permet de détruire ce que vous souhaitez. \n/dieu : Permet de transformer quelqu'un en dieu. \n/action : Permet d'effectuer une action. \n/amongus : SUS. \n/noob : noob. \n/arme : Permet d'avoir une arme. \n/ref : Ouais j'ai plus trop d'inspi là... \n/envie_de... : HEY COMMENT çA ?! \n/help : Permet d'avoir toutes les commandes.")
elif commande == (""):
    print("Erreur n°101 : Aucun Arguments n'a été mis.")
elif commande == (" "):
    print("Erreur Try Except n°277 : Arguments non-reconnus")
else:
    print("Erreur n°327 : Commande Inconnue. Si vous avez besoin d'aide, éxécutez la commande /help.")