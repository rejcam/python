import tkinter as tk
from tkinter import messagebox
import time
import threading

# Liste complète des thèmes
themes = [
    "dans une école", "dans une cuisine", "dans un avion", "sur la lune",
    "dans un hôpital", "dans une épicerie", "dans un ascenseur", "dans un musée",
    "sur une plage", "dans une forêt", "dans un centre d’achats", "dans un stade",
    "dans un port", "dans une gare", "dans un château", "dans une maison hantée",
    "objets rouges", "objets brillants", "objets en plastique", "objets qui flottent",
    "objets électroniques", "choses carrées", "objets anciens", "objets dangereux",
    "objets recyclables", "objets pointus", "objets mous", "objets qu’on peut lancer",
    "objets dans une trousse de premiers soins", "objets dans une boîte à outils",
    "animaux marins", "animaux de la ferme", "insectes", "animaux dangereux",
    "animaux mignons", "animaux qu’on peut dresser", "animaux avec des plumes",
    "animaux qui sautent", "animaux nocturnes", "animaux à quatre pattes",
    "fruits exotiques", "plats typiques québécois", "aliments sucrés", 
    "choses qu’on mange au déjeuner", "repas rapides", "ingrédients de pizza",
    "ingrédients de salade", "boissons gazeuses", "épices", "trucs qu’on met sur un hot-dog",
    "chapeaux", "chaussures", "vêtements d’hiver", "accessoires de mode",
    "vêtements pour la pluie", "vêtements pour la plage", "objets en cuir",
    "activités d’été", "activités d’hiver", "choses qu’on fait en vacances",
    "activités à la maison", "activités à l’école", "activités à faire seul",
    "sports d’équipe", "sports de glisse", "jeux de société", "trucs qu’on peut collectionner",
    "pouvoirs magiques", "monstres", "super-héros", "sorts de sorciers",
    "objets dans un jeu vidéo", "éléments d’un conte de fée", "objets d’un film d’horreur",
    "armes médiévales", "créatures fantastiques", "inventions imaginaires",
    "célébrités", "types de métiers", "pays d’Europe", "langues", 
    "émissions de télé", "réseaux sociaux", "fêtes religieuses", "émotions",
    "chansons connues", "danses populaires", "films des années 90", "dessins animés",
    "moyens de transport", "véhicules à roues", "véhicules volants", "véhicules lents",
    "choses qu’on voit sur une route", "parties d’un vélo", "types de bateaux",
    "objets dans une classe", "objets dans un sac à dos", "objets dans un casier",
    "fournitures scolaires", "objets sur un bureau", "matières scolaires", "jeux de récréation",
    "éléments de la nature", "types de fleurs", "arbres", "phénomènes météo",
    "trucs qu’on trouve sur la plage", "choses qu’on voit dans le ciel", "choses dans un jardin",
    "choses qui font peur", "choses qui font rire", "sons qu’on entend",
    "trucs qu’on peut empiler", "choses qu’on peut casser", "trucs qui collent",
    "choses qu’on peut lancer", "choses qui rebondissent", "trucs froids",
    "choses qu’on trouve dans un sac", "choses qui sentent bon", "choses qu’on peut plier",
    "choses qu’on oublie souvent", "trucs qu’on apporte en voyage", 
    "trucs qui tombent du ciel", "choses qui brillent dans le noir"
]

index_theme = 0
timer_thread = None
timer_active = False

# Fonction de génération du thème
def generer_theme():
    global index_theme, timer_active

    theme = themes[index_theme]
    theme_label.config(text=f"Thème : {theme}")
    index_theme = (index_theme + 1) % len(themes)

    # Démarrer le minuteur
    if not timer_active:
        timer_active = True
        threading.Thread(target=lancer_timer).start()

# Fonction du minuteur
def lancer_timer():
    global timer_active
    secondes = 30
    while secondes >= 0:
        timer_label.config(text=f"⏱️ {secondes}")
        time.sleep(1)
        secondes -= 1
    timer_label.config(text="⏱️ Temps écoulé !")
    timer_active = False

# Interface graphique
root = tk.Tk()
root.title("Générateur de Thèmes - Mot pour mot")
root.geometry("800x500")
root.configure(bg="#f4f4f4")

titre = tk.Label(root, text="🎲 Générateur de Thèmes", font=("Arial", 30), bg="#f4f4f4")
titre.pack(pady=20)

theme_label = tk.Label(root, text="Clique sur le bouton pour générer un thème", font=("Arial", 24), wraplength=700, bg="#ffffff", relief="solid", padx=20, pady=20)
theme_label.pack(pady=10)

timer_label = tk.Label(root, text="⏱️ 30", font=("Arial", 28), fg="#d32f2f", bg="#f4f4f4")
timer_label.pack(pady=10)

generer_btn = tk.Button(root, text="🎯 Générer un thème", command=generer_theme, font=("Arial", 20), bg="#4CAF50", fg="white", padx=30, pady=15)
generer_btn.pack(pady=20)

root.mainloop()
