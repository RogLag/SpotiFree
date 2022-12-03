import sqlite3
import chemin as c
import Users_accounts as UA
import cgi

Chemin = c.chemin()
base = sqlite3.connect(Chemin)

form = cgi.FieldStorage()
iduser = UA.Informations_Cookies("Id")

namep = form.getvalue('selectplaylists').split(":")[0]
idmusic = form.getvalue('selectplaylists').split(":")[1]
test = None

cursor = base.cursor()
iduser = UA.Informations_Cookies("Id")
ch =  f"SELECT IdPlaylist FROM Playlists WHERE Name = '{namep}' AND IdUser = '{iduser}';"
idplaylist = cursor.execute(ch).fetchall()[0][0]
idmusique = idmusic
ch = f"SELECT IdTrack FROM Possède_Posséder_par WHERE IdPlaylist = '{idplaylist}';"
liste = cursor.execute(ch)
liste = liste.fetchall()
for i in liste:
    if i[0] == idmusic:
        ch = f"DELETE FROM Possède_Posséder_par WHERE IdPlaylist = '{idplaylist}' AND IdTrack = '{idmusique}';"
        cursor.execute(ch)
        base.commit()
        print("Delete music")
        test = "non"
if test == None:
    ch = f"INSERT INTO Possède_Posséder_par(IdTrack,IdPlaylist) VALUES('{idmusique}','{idplaylist}');"
    cursor.execute(ch)
    base.commit()
    print('Add music')

