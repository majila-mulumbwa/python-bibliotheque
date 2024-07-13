import json
from class_utilisateur import*
from class_livre import*
from gestion_livre import*
from gestion_utilisateur import*
from emprunt_retour import*

# Interface Utilisateur

def menu_principal():
    """Affiche le menu principal."""
    print("\nMenu principal :")
    print("1. Gérer les livres")
    print("2. Gérer les utilisateurs")
    print("3. Emprunter/Retourner des livres")
    print("4. Quitter")
    choix = input("Choisissez une option : ")
    return choix

# Implémentation des Structures Conditionnelles

def gerer_livres(bibliotheque):
    """Gère les opérations sur les livres."""
    while True:
        print("\nGestion des livres :")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Lister les livres")
        print("4. Retour au menu principal")
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_livre(bibliotheque)
        elif choix == '2':
            supprimer_livre(bibliotheque)
elif choix == '3':
            lister_livres(bibliotheque)
        elif choix == '4':
            break
        else:
            print("Choix invalide.")

def gerer_utilisateurs(utilisateurs):
    """Gère les opérations sur les utilisateurs."""
    while True:
        print("\nGestion des utilisateurs :")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Lister les utilisateurs")
        print("4. Retour au menu principal")
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_utilisateur(utilisateurs)
        elif choix == '2':
            supprimer_utilisateur(utilisateurs)
        elif choix == '3':
            lister_utilisateurs(utilisateurs)
        elif choix == '4':
            break
        else:
            print("Choix invalide.")

def emprunter_retourner_livres(bibliotheque, utilisateurs):
    """Gère les opérations d'emprunt et de retour."""
    while True:
        print("\nEmprunter/Retourner des livres :")
        print("1. Emprunter un livre")
        print("2. Retourner un livre")
        print("3. Retour au menu principal")
        choix = input("Choisissez une option : ")
        if choix == '1':
            emprunter_livre(bibliotheque, utilisateurs)
        elif choix == '2':
            retourner_livre(bibliotheque)
        elif choix == '3':
            break
        else:
            print("Choix invalide.")

# Implémentation des Itérations

# (Déjà implémenté dans les fonctions lister_livres et lister_utilisateurs)

# Fonctionnalités Avancées

def rechercher_livre(bibliotheque):
    """Recherche un livre par titre ou auteur."""
    critere = input("Entrez le titre ou l'auteur du livre à rechercher : ")
    trouve = False
    for livre in bibliotheque:
        if critere.lower() in livre.titre.lower() or critere.lower() in livre.auteur.lower():
            print(f"ID : {livre.id}, Titre : {livre.titre}, Auteur : {livre.auteur}, Genre : {livre.genre}")
            trouve = True
    if not trouve:
        print("Livre non trouvé.")

# (Implémentation de l'historique des emprunts et des alertes de retard laissée en exercice)

# Fonction principale
if __name__ == "__main__":
    bibliotheque, utilisateurs = charger_donnees()

    while True:
        choix = menu_principal()
        if choix == '1':
            gerer_livres(bibliotheque)
        elif choix == '2':
            gerer_utilisateurs(utilisateurs)
        elif choix == '3':
            emprunter_retourner_livres(bibliotheque, utilisateurs)
        elif choix == '4':
            sauvegarder_donnees(bibliotheque, utilisateurs)
            break
        else:
            print("Choix invalide.")