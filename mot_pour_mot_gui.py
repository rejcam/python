import tkinter as tk
import random

# Données des catégories et thèmes
categories = {
    "lieux": [
        "dans une école", "dans une cuisine", "dans un aéroport", "dans un musée", 
        "dans une ferme", "dans un parc d’attractions"
    ],
    "activités": [
        "qu’on fait en vacances", "qu’on fait à l’école", "qu’on fait au travail", 
        "qu’on fait quand il pleut", "qu’on fait en famille"
    ],
    "personnes/métiers": [
        "métiers", "célébrités", "personnages de fiction", "types de sportifs", 
        "métiers qu’on rêvait de faire enfant"
    ],
    "objets": [
        "objets technologiques", "objets coupants", "objets qu’on trouve dans une salle de bain", 
        "objets en plastique", "objets anciens"
    ],
    "autres": [
        "choses qui font peur", "choses qui font rire", "sons qu’on entend souvent", 
        "trucs qu’on trouve dans un sac à dos", "trucs qu’on mange au petit déjeuner"
    ]
}

# Fonction pour générer un thème
def generer_theme():
    categorie = random.choice(list(categories.keys()))
    theme = random.choice(categories[categorie])
    theme_label.config(text=f"Thème : {theme}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de Thèmes - Mot pour Mot")
fenetre.geometry("400x200")
fenetre.resizable(False, False)

# Style de base
fenetre.config(bg="#f2f2f2")

# Titre
titre = tk.Label(fenetre, text="🎲 Générateur de Thèmes", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
titre.pack(pady=10)

# Zone d’affichage du thème
theme_label = tk.Label(fenetre, text="Cliquez sur le bouton pour générer un thème", font=("Helvetica", 12), wraplength=350, bg="#f2f2f2")
theme_label.pack(pady=10)

# Bouton pour générer un thème
generer_btn = tk.Button(fenetre, text="🎯 Générer un thème", font=("Helvetica", 12), command=generer_theme, bg="#4caf50", fg="white", padx=10, pady=5)
generer_btn.pack()

# Lancement de la boucle principale
fenetre.mainloop()
