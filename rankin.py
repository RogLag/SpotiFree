import sqlite3
import chemin as c
import Users_accounts as UA

def listen(liste):
    nb_listen = UA.Information_BDD("Artists","Listen","Name",liste[1])
    if nb_listen == None:
        nb_listen == 0
    UA.modif_BDD2("Artits",liste[1],"Listen",int(nb_listen)+1)