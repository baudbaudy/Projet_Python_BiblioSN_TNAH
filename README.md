
# Biblionthèque du Souvenir Napoléonien

BiblioSN est une application Flask réalisée dans le cadre du M2 "Technologies Numériques Appliquées à l'Histoire" de l'École Nationale des Chartes.

Celle-ci vise à proposer de parcourir la collection de la Bibliothèque de l'association le Souvenir Napoléonien, la plus grande association culturelle de France sur l'histoire de Premier et Second empire. A partir d'un fichier Excel fourni par la bibliothèque, seule catalogue du lieu disponible en ligne,  nous avons voulu proposer une application avec une interface qui facilerait la recherche et la prise d'information sur le contenu des rayons de ladite bibliothèque. Par ailleurs, l'application dispose, en plus d'une liste exhaustive des ouvrages disponibles, d'un index des auteurs présents dans les rayons avec un renvoi vers les livres qu'ils ont écrit. Un formulaire est aussi en développement afin de permettre aux membres de l'association de compléter et modifier le catalogue en ligne.

## Installation de l'application

Récupérer le dossier : depuis votre terminal avec la commande 'git clone https://github.com/baudbaudy/Python_BiblioSN_TNAH' ou télécharger directement le fichier.zip et décompressez le. 
Vérifier que la version de Python corresponde à Python 3.X : depuis votre terminal taper 'python --version'
Ensuite, allez vous placer dans le dossier, depuis votre terminal, avec 'cd Python_BiblioSN_TNAH-master/'
Une fois placé dans le dossier, vous devrez lancer un environnement virtuel.
Pour se faire, installer l'environnement virtuel avec la commande 'python3 -m venv [nom de votre environnement virtuel]'
Ensuite vous pouvez lancer votre environnement virtuel avec la commande 'source [nom de votre environnement virtuel]/bin/activate'
Lancer ensuite la commande 'pip install -r requirements.txt' pour installer les librairies et packages nécessaires au fonctionnement de l'application.
Lancer enfin l'application avec la commande 'python3 run.py' et depuis votre navigateur internet rendez-vous à l'adresse http://127.0.0.1:5000/

Vous y êtes enfin ! Bonne visite !




