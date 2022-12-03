import sqlite3
import chemin as c

Chemin = c.chemin()
base = sqlite3.connect(Chemin)

def Search(string):
    result = "%"
    for lettre in string:
        result += f"{lettre}%"
    string2 = result
    pointer = base.cursor()
    ch = f'SELECT Name FROM Artists WHERE Name like "%{string}%" ORDER BY Listen LIMIT 1;'
    artist = pointer.execute(ch)
    artist = artist.fetchall()
    ch = f'SELECT Title FROM Scrapbooks WHERE Title like "{string2}" LIMIT 3;'
    albums = pointer.execute(ch)
    albums = albums.fetchall()
    ch = f'SELECT Name FROM Tracks WHERE Name like "{string2}" ORDER BY Listen LIMIT 10;'
    tracks = pointer.execute(ch)
    tracks = tracks.fetchall()
    result = []
    if artist != []:
        ch = f"{artist[0][0]}"
        result.append(ch)
    else:
        result.append("None")
    result.append([])
    if albums != []:
        for i in albums[0]:
            result[1].append(i)
    else:
        result[1].append("None")
    result.append([])
    for i in tracks:
        for y in i:
            result[2].append(f"{y}")
    return result