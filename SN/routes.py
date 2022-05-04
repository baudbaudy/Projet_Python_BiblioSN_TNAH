# Fichier permettant l'import des modules et packages permettant le bon fonctionnement des routes

from flask import render_template, flash, request
from .app import app
from .modeles.donnees import SN 
from SN.app import app
from .modeles.donnees import SN


#Les routes sont déclarées par le décorateur @app.route
#et permettent de retourner la réponse à une requête


@app.route("/")
def accueil():
    livres = SN.query.all()
    return render_template("pages/accueil.html", nom="SN", livres=livres)
 
# Cette route permet l'affichage de la page d'accueil


@app.route("/SN/<int:ENTREE>")
def livre(ENTREE):
    un_livre = SN.query.get(ENTREE)
    return render_template("pages/catalogue.html", nom="SN", livre=un_livre)

#Cette route permet l'affichage de la page catalogue
 


@app.route("/recherche")
def recherche():
    
    #Cette route permet l'exécution d'une recherche simple
    


    # .get permet de se passer d'un if long en mettant les conditions de la requête entre parenthèses
    motclef = request.args.get("keyword", None)

    # Liste vide de résultat (restera vide par défaut en l'absence de mots-clés)
    resultats = []
    
    titre = "Recherche"
    if motclef:
        resultats = SN.query.filter(
            SN.TITRE.like("%{}%".format(motclef))
        ).all()
        titre = "Sortie pour " + motclef
    return render_template("pages/recherche.html", nom="SN", resultats=resultats, titre=titre)

@app.route("/index_auteurs")
def index_auteurs():
    
    #Cette route permet l'affichage de la page index auteurs
    #la requête permet d'afficher l'ensemble des auteurs par ordre alphabétique et sans doublons
   
    auteurs = SN.query.order_by(SN.AUTEUR).distinct(SN.AUTEUR).all()
    return render_template("pages/index_auteurs.html", nom="SN", auteurs=auteurs)
    
@app.route("/savoir")
def savoir():
    
   # Cette route permet l'affichage de la page en savoir plus
    
    return render_template("pages/savoir.html")    




# Cette route permet l'ajout de données dans la base de données

@app.route("/page_formulaire", methods=["GET", "POST"])
def page_formulaire():
  
    #Cette route permet l'affichage de la page d'accueil pour l'ajout de données
 
    return render_template("pages/page_formulaire.html", nom="SN")


@app.route("/nouveau_livre", methods=["GET", "POST"])
def ajout_livre():
    
    # Cette route permettant l'ajout d'un livre dans la base de données
   
    if request.method == "POST":
        statut,livre_donnees = SN.ajouter_un_livre(
            nouvelle_entree=request.form.get("nouvelle_entree", None),
            nouveau_titre=request.form.get("nouveau_titre", None),
            nouvel_auteur=request.form.get("nouvel_auteur", None),
            lettre_serie=request.form.get("lettre_serie", None),
            numero_cote=request.form.get("numero_cote", None),
            maison_edition=request.form.get("maison_edition", None),
            commentaire=request.form.get("commentaire", None),
            theme_ouvrage=request.form.get("theme_ouvrage", None),
            type_ouvrage=request.form.get("type_ouvrage", None))

        if statut is True:
            flash("Livre enregistré", "Merci pour votre participation et VIVE L'EMPEREUR!")
            return render_template("pages/nouveau_livre.html", nom="SN")
        #sortie de nouveau_livre.html
        else:
            flash("Problèmes rencontrées : " + ", ".join(livre_donnees))
            return render_template("pages/nouveau_livre.html")

    return render_template("pages/nouveau_livre.html", nom="SN")


