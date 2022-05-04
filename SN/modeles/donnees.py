#Import d'informations depuis un fichier
from .. app import db

#Défénition de la table SN
class SN(db.Model):
    ENTREE = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    TITRE = db.Column(db.Text)
    AUTEUR = db.Column(db.Text)
    SERIE = db.Column(db.Text)
    COTE = db.Column(db.Text)
    EDITION = db.Column(db.Text)
    COMMENTAIRES = db.Column(db.Text)
    THEME_OUVRAGE = db.Column(db.Text)
    TYPE_OUVRAGE = db.Column(db.Text)



    @staticmethod
    def ajouter_un_livre(nouvelle_entree, nouveau_titre, nouvel_auteur, lettre_serie, numero_cote, maison_edition, commentaire, theme_ouvrage, type_ouvrage):
       #Fonction qui permet d'ajouter un livre au catalogue de la bibliothèque
        
        erreurs = []
        if not nouvelle_entree:
            erreurs.append("le champ 'ENTREE' doit etre rempli")
        if not nouveau_titre:
            erreurs.append("le champ 'TITRE' doit etre rempli")
        if not nouvel_auteur:
            erreurs.append("le champ 'AUTEUR' doit etre rempli")
        if not maison_edition:
            erreurs.append("le champ 'EDITION' doit etre rempli")
        if not(lettre_serie):
            erreurs.append("le champ 'SERIE' doit etre rempli")
        if not(numero_cote):
            erreurs.append("le champ 'COTE' doit etre rempli")
        if len(erreurs) > 0:
            return False, erreurs
        #Erreurs provoquées si les champs obligatoires ne sont pas remplis

        
        nv_ouvrage = SN(ENTREE=nouvelle_entree,
                        TITRE=nouveau_titre,
                        AUTEUR=nouvel_auteur,
                        SERIE=lettre_serie,
                        COTE=numero_cote,
                        EDITION=maison_edition,
                        COMMENTAIRES=commentaire,
                        THEME_OUVRAGE=theme_ouvrage, 
                        TYPE_OUVRAGE=type_ouvrage)
        # Ajout d'un nouveau livre dans la bibliothèque

        try:
            db.session.add(nv_ouvrage)
            # Données ajoutées au catalogue
            db.session.commit()
            # Confirmation de l'ajout au catalogue
            return True, nv_ouvrage

        except Exception as erreur:
            return False, [str(erreur)]
        # Si erreur, la modification du catalogue n'est pas effectuée
