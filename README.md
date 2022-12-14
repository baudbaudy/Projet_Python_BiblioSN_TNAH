
# Bibliothèque du Souvenir Napoléonien

BiblioSN est un projet d'application Flask.
Celui-ci vise à proposer de parcourir la collection de la Bibliothèque de l'association le Souvenir Napoléonien, une des plus importantes associations culturelles de France sur l'histoire de Premier et Second empire. Actuellement, l'association ne propose d'explorer le contenu de sa bibliothèque qu'à partir d'un simple fichier Excel, ce qui est peu pratique pour l'utilisateur. Aussi, à partir de ce fichier Excel, seul catalogue du lieu disponible en ligne,  nous voulons proposer une application avec une interface qui faciliterait la recherche et la prise d'information sur le contenu des rayons de ladite bibliothèque. Par ailleurs, l'application devra disposer, en plus d'une liste exhaustive des ouvrages disponibles, d'un index des auteurs présents dans les rayons avec un renvoi vers les livres qu'ils ont écrit. Un formulaire est aussi en développement afin de permettre aux membres de l'association de compléter et modifier le catalogue en ligne.

## Installation de l'application

Récupérer le dossier : 
- Depuis votre terminal avec la commande 'git clone https://github.com/baudbaudy/Python_BiblioSN_TNAH' ou télécharger directement le fichier.zip et décompressez le. 
- Vérifier que la version de Python corresponde à Python 3.X : depuis votre terminal taper 'python --version'

- Ensuite, allez vous placer dans le dossier, depuis votre terminal, avec 'cd Python_BiblioSN_TNAH-master/'

- Une fois placé dans le dossier, vous devrez lancer un environnement virtuel.
- Pour se faire, installer l'environnement virtuel avec la commande 'python3 -m venv [nom de votre environnement virtuel]'
- Ensuite vous pouvez lancer votre environnement virtuel avec la commande 'source [nom de votre environnement virtuel]/bin/activate'
- Lancer ensuite la commande 'pip install -r requirements.txt' pour installer les librairies et packages nécessaires au fonctionnement de l'application.
- Lancer enfin l'application avec la commande 'python3 run.py' et depuis votre navigateur internet rendez-vous à l'adresse http://127.0.0.1:5000/



