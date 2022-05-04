#Import de Flask et de la fonction render_template depuis le
#module flask
from flask import Flask
#Import de SQLAlchemy depuis la version flask_sqlalchemy pour interagir avec la base de données
from flask_sqlalchemy import SQLAlchemy
#Import SECRET_KEY depuis constantes.py
from .constantes import SECRET_KEY
# Import du package os permettant d'agir avec les différents systèmes d'exploitation 
import os


#Définition des chemins:
#Stockage du chemin du fichier courant
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
# Stockage du chemin vers le dossier templates
templates = os.path.join(chemin_actuel, "templates")
# Stockage du chemin vers le dossier static
statics = os.path.join(chemin_actuel, "static")

#Création de l'application en tant qu'instance de la classe Flask
#Le nommage de l'application est obligatoire dans Flask pour pouvoir faire tourner
#plusieurs applications sur le même serveur. 
app = Flask("Application",
            template_folder=templates,
            static_folder=statics
            )

#Configuration de la base de données 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./SN.sqlite'

#Initiation de l'extension
db = SQLAlchemy(app)

#Importation des pages depuis le fichier routes.py
from .routes import accueil, livre, recherche, index_auteurs, savoir, ajout_livre, page_formulaire
