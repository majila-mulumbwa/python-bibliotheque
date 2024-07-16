import json
from utili_struct import*
from livre_struct import*
# Gestion des Livres

def ajouter_livre(bibliotheque):
    """Ajoute un nouveau livre à la bibliothèque."""
    id = input("Entrez l'ID du livre : ")
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    genre = input("Entrez le genre du livre : ")
    bibliotheque.append(Livre(id, titre, auteur, genre))
    print("Livre ajouté avec succès.")

def supprimer_livre(bibliotheque):
    """Supprime un livre de la bibliothèque."""
    id = input("Entrez l'ID du livre à supprimer : ")
    for i, livre in enumerate(bibliotheque):
        if livre.id == id:
            del bibliotheque[i]
            print("Livre supprimé avec succès.")
            return
    print("Livre non trouvé.")

def lister_livres(bibliotheque):
    """Affiche la liste des livres disponibles."""
    if len(bibliotheque) == 0:
        print("La bibliothèque est vide.")
    else:
        print("Liste des livres disponibles :")
        for livre in bibliotheque:
            if livre.disponible:
                print(f"ID : {livre.id}, Titre : {livre.titre}, Auteur : {livre.auteur}, Genre : {livre.genre}")
