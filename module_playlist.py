import sqlite3
import chemin as c
import Users_accounts as UA
Chemin = c.chemin()
base = sqlite3.connect(Chemin)

def gestion_playlist(name):
    if name == "Favorite@":
        return None
    cursor = base.cursor()
    iduser = UA.Informations_Cookies("Id")
    ch = f"SELECT Name FROM Playlists WHERE IdUser = '{iduser}';"
    liste = cursor.execute(ch)
    liste = liste.fetchall()
    for i in liste:
        if i[0] == name:
            ch = f"DELETE FROM Playlists WHERE Name = '{name}' AND IdUser = '{iduser}';"
            cursor.execute(ch)
            base.commit()
            return "Delete"
    ch = f"INSERT INTO PLaylists(Name,IdUser) VALUES('{name}','{iduser}');"
    cursor.execute(ch)
    base.commit()
    return 'Add'