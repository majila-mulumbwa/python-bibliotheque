import json
from class_livre import*
from class_utilisateur import*
from gestion_livre import*

# Gestion des Utilisateurs

def ajouter_utilisateur(utilisateurs):
    """Ajoute un nouvel utilisateur."""
    id = input("Entrez l'ID de l'utilisateur : ")
    nom = input("Entrez le nom de l'utilisateur : ")
    email = input("Entrez l'email de l'utilisateur : ")
    utilisateurs.append(Utilisateur(id, nom, email))
    print("Utilisateur ajouté avec succès.")

def supprimer_utilisateur(utilisateurs):
    """Supprime un utilisateur."""
    id = input("Entrez l'ID de l'utilisateur à supprimer : ")
    for i, utilisateur in enumerate(utilisateurs):
        if utilisateur.id == id:
            del utilisateurs[i]
            print("Utilisateur supprimé avec succès.")
            return
    print("Utilisateur non trouvé.")

def lister_utilisateurs(utilisateurs):
    """Affiche la liste des utilisateurs."""
    if len(utilisateurs) == 0:
        print("Il n'y a pas d'utilisateurs.")
    else:
        print("Liste des utilisateurs :")
    for utilisateur in utilisateurs:
            print(f"ID : {utilisateur.id}, Nom : {utilisateur.nom}, Email : {utilisateur.email}")
