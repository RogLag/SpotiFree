import sys
import codecs
import Users_accounts as UA
import sqlite3
import chemin as c

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

Chemin = c.chemin()
base = sqlite3.connect(Chemin)

Musique = UA.Informations_Cookies("Ecoute")
Musique = Musique.split(":")
Musique = Musique[0]
IdUser = UA.Informations_Cookies("Id")
IdMusique = UA.Information_BDD("Tracks","IdTrack",Musique,"Name")

pointer = base.cursor()
ch = f'SELECT Playlists.Name FROM Playlists INNER JOIN Users ON(Playlists.IdUser=Users.IdUser) WHERE Playlists.IdUser = "{IdUser}" AND Playlists.Name = "Favorite@";'
liste = pointer.execute(ch)
liste = liste.fetchall()
if liste == []:
    ch = f'INSERT INTO Playlists(Name,IdUser) VALUES("Favorite@","{IdUser}");'
    pointer.execute(ch)
    base.commit()
    ch = f'SELECT IdPlaylist FROM Playlists WHERE Name = "Favorite@";'
    IdPlaylist = pointer.execute(ch)
    IdPlaylist = IdPlaylist.fetchall()
    IdPlaylist = IdPlaylist[0][0]
    ch = f'INSERT INTO Possède_Posséder_par(IdTrack,IdPlaylist) VALUES("{IdMusique}","{IdPlaylist}");'
    pointer.execute(ch)
    base.commit()
    print("True")
else: 
    ch = f'SELECT IdPlaylist FROM Playlists WHERE Name = "Favorite@";'
    IdPlaylist = pointer.execute(ch)
    IdPlaylist = IdPlaylist.fetchall()
    IdPlaylist = IdPlaylist[0][0]
    ch = f'SELECT IdTrack FROM Possède_Posséder_par WHERE IdTrack = "{IdMusique}";'
    liste = pointer.execute(ch)
    liste = liste.fetchall()
    if liste == []:
        ch = f'INSERT INTO Possède_Posséder_par(IdTrack,IdPlaylist) VALUES("{IdMusique}","{IdPlaylist}");'
        pointer.execute(ch)
        base.commit()
        print("True")
    else:
        ch = f'DELETE FROM Possède_Posséder_par WHERE IdTrack = "{IdMusique}";'
        pointer.execute(ch)
        base.commit()
        print("False")
        
print("Content-type: text/html; charset=utf-8\n")
