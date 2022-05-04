from warnings import warn

#Variable générant des clés d'encryptage
SECRET_KEY = "Vive l'Empereur!"

if SECRET_KEY == "Vive l'Empereur !":
	warn("Le régime impérial, c'est dépassé, comme votre clé secrète! Pensez à la changer", Warning)
