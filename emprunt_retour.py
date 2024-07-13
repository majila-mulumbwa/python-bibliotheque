import json
from class_utilisateur import*
from class_livre import*
from gestion_livre import*
from gestion_utilisateur import*

# Emprunt et Retour des Livres

def emprunter_livre(bibliotheque, utilisateurs):
    """Permet à un utilisateur d'emprunter un livre."""
    id_utilisateur = input("Entrez l'ID de l'utilisateur : ")
    id_livre = input("Entrez l'ID du livre à emprunter : ")
    for i, livre in enumerate(bibliotheque):
        if livre.id == id_livre and livre.disponible:
            utilisateur = next((u for u in utilisateurs if u.id == id_utilisateur), None)
            if utilisateur:
                livre.disponible = False
                print(f"Le livre '{livre.titre}' a été emprunté par {utilisateur.nom}.")
                return
            else:
                print("Utilisateur non trouvé.")
                return
    print("Livre non trouvé ou indisponible.")

def retourner_livre(bibliotheque):
    """Permet à un utilisateur de retourner un livre."""
    id_livre = input("Entrez l'ID du livre à retourner : ")
    for i, livre in enumerate(bibliotheque):
        if livre.id == id_livre:
            livre.disponible = True
            print(f"Le livre '{livre.titre}' a été retourné.")
            return
    print("Livre non trouvé.")

# Sauvegarde des données

def sauvegarder_donnees(bibliotheque, utilisateurs, fichier_bibliotheque="bibliotheque.json", fichier_utilisateurs="utilisateurs.json"):
    """Sauvegarde les données dans des fichiers JSON."""
    livres_json = [{"id": livre.id, "titre": livre.titre, "auteur": livre.auteur, "genre": livre.genre, "disponible": livre.disponible} for livre in bibliotheque]
    utilisateurs_json = [{"id": utilisateur.id, "nom": utilisateur.nom, "email": utilisateur.email} for utilisateur in utilisateurs]

    with open(fichier_bibliotheque, 'w') as f:
        json.dump(livres_json, f, indent=4)

    with open(fichier_utilisateurs, 'w') as f:
        json.dump(utilisateurs_json, f, indent=4)

    print("Données sauvegardées avec succès.")

def charger_donnees(fichier_bibliotheque="bibliotheque.json", fichier_utilisateurs="utilisateurs.json"):
    """Charge les données depuis des fichiers JSON."""
    bibliotheque = []
    utilisateurs = []

    try:
        with open(fichier_bibliotheque, 'r') as f:
            livres_json = json.load(f)
            for livre in livres_json:
                bibliotheque.append(Livre(livre["id"], livre["titre"], livre["auteur"], livre["genre"], livre["disponible"]))

        with open(fichier_utilisateurs, 'r') as f:
            utilisateurs_json = json.load(f)
            for utilisateur in utilisateurs_json:
                utilisateurs.append(Utilisateur(utilisateur["id"], utilisateur["nom"], utilisateur["email"]))

        print("Données chargées avec succès.")
        return bibliotheque, utilisateurs
    except FileNotFoundError:
        print("Fichiers de données non trouvés. Initialisation de la bibliothèque vide.")
        return [], []
