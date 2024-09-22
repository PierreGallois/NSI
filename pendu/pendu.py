import turtle as t
import tkinter as tk
from tkinter import simpledialog

# setup de la fenêtre
fenetre = t.Screen()
fenetre.setup(width=400, height=400, startx=-1, starty=0)
t.title("Jeu de pendu")

# Dessiner la potence
t.up()
t.goto(0,0)
t.forward(10)
t.down()
t.forward(100)
t.backward(50)
t.left(90)
t.forward(170)
t.right(90)
t.forward(70)

# Générateur pour dessiner peu à peu la potence
def dessiner_potence():
    t.right(90)
    t.forward(20)
    yield
    t.right(90)
    t.circle(25)
    t.up()
    t.left(90)
    t.forward(50)
    t.down()
    yield
    t.right(45)
    t.forward(30)
    t.backward(30)
    yield
    t.left(90)
    t.forward(30)
    t.backward(30)
    yield
    t.right(45)
    t.forward(40)
    yield
    t.right(45)
    t.forward(35)
    t.backward(35)
    yield
    t.left(90)
    t.forward(35)
    t.backward(35)
    yield

# variables de base
mot = "independance"
nb_essais = 7
dejadonnee = {list(mot)[0]} # Set dans lequel on garde les entrées déjà essayées
potence = dessiner_potence() # Instance du générateur
mot_montre = "".join(["."]*len(mot)) # String à afficher à l'écran avec ce que l'on a déjà trouvé

def montrer_plus_du_mot(chara):
    global mot_montre

    mot_montre = "".join([chara if list(mot)[i] == chara else list(mot_montre)[i] for i in range(len(mot))]) # Remplace les . par les lettres là où il faut
    tk.Label(ROOT, text=mot_montre).grid(row = 2)
    if mot_montre == mot: # Condition de fin où le joueur a trouvé tout le ot en énumérant ses lettres
        tk.messagebox.showinfo(ROOT, message="Bravo ! Le mot était {}".format(mot))
        ROOT.quit()


def gerer_entree(entree):
    global nb_essais
    global potence

    if nb_essais == 1: # Cas de fin où le joueur n'a plus d'essais
        next(potence) # Fix bizarre pour que le dessin se finisse
        tk.messagebox.showinfo(ROOT, message="Vous avez perdu ! Le mot était {}".format(mot))
        ROOT.quit()
    elif entree == "" or (len(entree) < len(mot) and len(entree) > 1) or entree in dejadonnee: # Ne pas supporter de mettre plusieurs lettre sauf si c'est le mot entier, ne pas rien faire si deja essayé
        pass
    else: # Autres cas
        if len(entree) == 1 and entree not in dejadonnee and entree in mot: # Si l'utilisateur entre une lettre
            montrer_plus_du_mot(entree)
            dejadonnee.union(entree)
        elif entree == mot: #S'il entre un mot
            tk.messagebox.showinfo(ROOT, message="Bravo ! Le mot était {}".format(mot))
            ROOT.quit()
        else: # Si il a faux
            nb_essais -= 1
            tk.Label(ROOT, text="Il vous reste {} essais".format(str(nb_essais))).grid(row=0)
            next(potence)

# Fonction qui reprend l'entrée de tkinter
def entrer_lettre_ou_mot():
    gerer_entree(entry.get().lower())
    entry.delete(0, tk.END)

# setup de tkinter pour l'input
ROOT = tk.Tk()

tk.Label(ROOT, text="Il vous reste {} essais".format(str(nb_essais))).grid(row=0)
tk.Label(ROOT, text="Lettre ou mot : ").grid(row=1)

entry = tk.Entry(ROOT) # Boite d'entrée
entry.grid(row=1, column=1)

tk.Button(ROOT, text="Entrer", command=entrer_lettre_ou_mot).grid(row=3, column = 0, sticky = tk.W, pady = 4)
tk.Button(ROOT, text="Quitter", command=ROOT.quit).grid(row=3, column = 1, sticky = tk.W,pady = 4)

montrer_plus_du_mot(list(mot)[0]) # Affiche la première lettre du mot et toutes les lettres identiques

ROOT.mainloop()